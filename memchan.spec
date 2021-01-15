#
# RPM spec for Memchan
#

%{!?directory:%define directory /usr}
%define tarname Memchan

Name:           memchan
Version:        2.3
Summary:        Memory Channels in Tcl
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Url:            https://sourceforge.net/projects/memchan/
BuildRequires:  autoconf
BuildRequires:  tcl-devel >= 8.1
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcllib
Source:         %{tarname}%{version}.tar.gz
Patch0:         makefile.patch
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-build

%description
A new channel type for Tcl 8's channel system.  Memory channels
conform to the same interface as files and sockets, but the data
is stored in memory rather than in files.  They are good for
long dynamic strings and passing large quantities of data.

%package devel
Summary:        Development package for Memchan
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
A new channel type for Tcl 8's channel system.  Memory channels
conform to the same interface as files and sockets, but the data
is stored in memory rather than in files.  They are good for
long dynamic strings and passing large quantities of data.
 
This package contains the development files.

%prep
%setup -q -n %{tarname}%{version}
%patch0

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make

%install
mkdir -p %{buildroot}/%tclscriptdir/%name%version
make DESTDIR=%{buildroot} pkglibdir=%tclscriptdir/%name%version install

%files
%defattr(-,root,root)
%doc license.terms README
%tclscriptdir/%name%version
%_libdir/libMemchan2.3.so
%{_mandir}/mann/*.n*

%files devel
%defattr(-,root,root)
%_libdir/libMemchanstub2.3.a
%{_includedir}/*.h

%changelog

