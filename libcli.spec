Summary:	Cisco-like telnet command-line library
Summary(pl):	Biblioteka Cisco-podobnej linii polece� telnetu
Name:		libcli
Version:	1.8.5
Release:	1
License:	LGPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/libcli/%{name}-%{version}.tar.gz
# Source0-md5:	0fdd30df5a8c1388a4549751ba61247a
URL:		http://www.sf.net/projects/libcli/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcli provides a shared library for including a Cisco-like
command-line interface into other software. It's a telnet interface
which supports command-line editing, history, authentication and
callbacks for a user-definable function tree.

%description -l pl
Pakiet libcli dostarcza wsp�dzielon� bibliotek� do w��czania
Cisco-podobnego interfejsu linii polece� do innego oprogramowania.
Jest to interfejs telnetu, kt�ry obs�uguje edycj� linii polece�,
histori�, uwierzytelnienie i callbacki do definiowalnego przez
u�ytkownika drzewa funkcji.

%package devel
Summary:	libcli header files
Summary(pl):	Pliki nag��wkowe libcli
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcli library.

%description devel -l pl
Pliki nag��wkowe biblioteki libcli.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS='%{rpmldflags} -shared -nostartfiles -Wl,-soname,libcli.so.$(MAJOR)'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libcli.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
install libcli.h $RPM_BUILD_ROOT%{_includedir}
# can be expanded in current directory
ln -sf libcli.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libcli.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README Doc/usersguide.html
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc Doc/developers.html
%{_libdir}/*.so
%{_includedir}/*.h
