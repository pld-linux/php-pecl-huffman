%define		_modname	huffman
%define		_status		stable
Summary:	%{_modname} - lossless compression algorithm
Summary(pl.UTF-8):	%{_modname} - bezstratny algorytm kompresji
Name:		php-pecl-%{_modname}
Version:	0.2.0
Release:	6
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	e920b06610fb3b6ad1d79dc910962dc3
URL:		http://pecl.php.net/package/huffman/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huffman compression belongs into a family of algorithms with a
variable codeword length. That means that individual symbols
(characters in a text file for instance) are replaced by bit sequences
that have a distinct length. So symbols that occur a lot in a file are
given a short sequence while other that are used seldom get a longer
bit sequence.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Kompresja Huffmana należy do grupy algorytmów o zmiennej długości
klucza. To oznacza, że pojedyncze symbole (np. znaki w pliku
tekstowym) są zastępowane sekwencjami bitów o różnej długości. W ten
sposób symbole, które często pojawiają się w pliku, są zastępowane
krótszą sekwencją, podczas gdy inne, rzadziej używane, otrzymują
dłuższą sekwencję bitową.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
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
%doc %{_modname}-%{version}/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
