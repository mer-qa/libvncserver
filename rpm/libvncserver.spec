# Note that this is NOT a relocatable package
Name:           libvncserver
Version:        0.9.14
Release:        1
License:        GPLv2+ and MIT and BSD-2-Clause
URL:            https://github.com/mer-qa/libvncserver
Source:         %{name}-%{version}.tar.gz
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  cmake
Summary: a library to make writing a vnc server easy

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schemata.

LibVNCServer was put together and is (actively ;-) maintained by
Johannes Schindelin <Johannes.Schindelin@gmx.de>

%package devel
Summary:      Header Files for %{name} 
Requires:     %{name} = %{version}

%description devel
Header Files for %{name}.

%prep
%setup -q -n %{name}-%{version}/libvncserver

%build
%cmake .
%cmake_build

%install
%cmake_install

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%pre
%post
%preun
%postun

%files
%defattr(-,root,root)
%doc README.md AUTHORS ChangeLog NEWS.md
%{_libdir}/libvncclient.so*
%{_libdir}/libvncserver.so*

%files devel
%defattr(-,root,root)
%{_includedir}/rfb/*
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc
%{_libdir}/cmake/LibVNCServer
