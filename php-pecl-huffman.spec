%define		_modname	huffman
%define		_status		stable

Summary:	%{_modname} - lossless compression algorithm
Summary(pl):	%{_modname} - bezstratny algorytm kompresji
Name:		php-pecl-%{_modname}
Version:	0.2.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	e920b06610fb3b6ad1d79dc910962dc3
URL:		http://pecl.php.net/package/huffman/
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

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
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
