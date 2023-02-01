#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Cisco-like telnet command-line library
Summary(pl.UTF-8):	Biblioteka Cisco-podobnej linii poleceń telnetu
Name:		libcli
Version:	1.10.4
Release:	2
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/dparrish/libcli/releases
Source0:	https://github.com/dparrish/libcli/archive/V%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	05507ab0a08d8cad4dc0b8ed12f775a2
URL:		https://github.com/dparrish/libcli
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcli provides a shared library for including a Cisco-like
command-line interface into other software. It's a telnet interface
which supports command-line editing, history, authentication and
callbacks for a user-definable function tree.

%description -l pl.UTF-8
Pakiet libcli dostarcza współdzieloną bibliotekę do włączania
Cisco-podobnego interfejsu linii poleceń do innego oprogramowania.
Jest to interfejs telnetu, który obsługuje edycję linii poleceń,
historię, uwierzytelnienie i callbacki do definiowalnego przez
użytkownika drzewa funkcji.

%package devel
Summary:	libcli header files
Summary(pl.UTF-8):	Pliki nagłówkowe libcli
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcli library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcli.

%package static
Summary:	Static libcli library
Summary(pl.UTF-8):	Statyczna biblioteka libcli
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcli library.

%description static -l pl.UTF-8
Statyczna biblioteka libcli.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG= \
	OPTIM="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	%{!?with_static_libs:STATIC_LIB=0}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	%{!?with_static_libs:STATIC_LIB=0}

%if "%{_lib}" != "lib"
%{__mv} $RPM_BUILD_ROOT%{_prefix}/{lib,%{_lib}}
%endif

%if %{with static_libs}
cp -p libcli.a $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libcli.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcli.so.1.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcli.so
%{_includedir}/libcli.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcli.a
%endif
