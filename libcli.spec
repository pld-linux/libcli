Summary:	Cisco-like telnet command-line library
Summary(pl):	Cisco-podobna biblioteka telnet
Name:		libcli
Version:	1.1.0
Release:	0.1
Group:		Applications/Networking
License:	LGPL
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	43aa6d438fd75bc80f512d5756bb5d2c
URL:		http://www.sf.net/projects/libcli
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcli provides a shared library for including a Cisco-like
command-line interface into other software. It's a telnet interface
which supports command-line editing, history, authentication and
callbacks for a user-definable function tree.

%description -l pl
libcli dostarcza wspó³dzielon± bibliotekê

%prep
%setup -q

%build

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install
ln -sf %{_libdir}/libcli.so.1.1.0 $RPM_BUILD_ROOT%{_libdir}/libcli.so


%post
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Doc/usersguide.html Doc/developers.html
%{_libdir}/*.so*
%{_includedir}/*.h
