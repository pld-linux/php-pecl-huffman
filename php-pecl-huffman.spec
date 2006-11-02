%define		_modname	huffman
%define		_status		stable
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - lossless compression algorithm
Summary(pl):	%{_modname} - bezstratny algorytm kompresji
Name:		php-pecl-%{_modname}
Version:	0.2.0
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	e920b06610fb3b6ad1d79dc910962dc3
URL:		http://pecl.php.net/package/huffman/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
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

%description -l pl
Kompresja Huffmana nale¿y do grupy algorytmów o zmiennej d³ugo¶ci
klucza. To oznacza, ¿e pojedyncze symbole (np. znaki w pliku
tekstowym) s± zastêpowane sekwencjami bitów o ró¿nej d³ugo¶ci. W ten
sposób symbole, które czêsto pojawiaj± siê w pliku, s± zastêpowane
krótsz± sekwencj±, podczas gdy inne, rzadziej u¿ywane, otrzymuj±
d³u¿sz± sekwencjê bitow±.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
