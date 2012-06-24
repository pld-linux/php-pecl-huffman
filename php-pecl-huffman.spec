%define		_modname	huffman
%define		_status		beta

Summary:	%{_modname} - lossless compression algorithm
Summary(pl):	%{_modname} - bezstratny algorytm kompresji
Name:		php-pecl-%{_modname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	2b20c8bdf2209f7758f65576bdf923c5
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

#%description -l pl
#
#To rozszerzenie ma w PECL status: %{_status}.

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
