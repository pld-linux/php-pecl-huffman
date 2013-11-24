%define		php_name	php%{?php_suffix}
%define		modname	huffman
%define		status		stable
Summary:	%{modname} - lossless compression algorithm
Summary(pl.UTF-8):	%{modname} - bezstratny algorytm kompresji
Name:		%{php_name}-pecl-%{modname}
Version:	0.2.0
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	e920b06610fb3b6ad1d79dc910962dc3
URL:		http://pecl.php.net/package/huffman/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huffman compression belongs into a family of algorithms with a
variable codeword length. That means that individual symbols
(characters in a text file for instance) are replaced by bit sequences
that have a distinct length. So symbols that occur a lot in a file are
given a short sequence while other that are used seldom get a longer
bit sequence.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Kompresja Huffmana należy do grupy algorytmów o zmiennej długości
klucza. To oznacza, że pojedyncze symbole (np. znaki w pliku
tekstowym) są zastępowane sekwencjami bitów o różnej długości. W ten
sposób symbole, które często pojawiają się w pliku, są zastępowane
krótszą sekwencją, podczas gdy inne, rzadziej używane, otrzymują
dłuższą sekwencję bitową.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
