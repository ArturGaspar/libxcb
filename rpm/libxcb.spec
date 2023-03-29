Name:       libxcb
Version:    1.17.0
Release:    1%{?dist}
Summary:    C interface to the X Window System protocol
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xau) >= 0.99.2
BuildRequires:  pkgconfig(xcb-proto) >= 1.17.0
BuildRequires:  pkgconfig(xorg-macros) >= 1.18
BuildRequires:  python3-base

%description
libxcb provides an interface to the X Window System protocol, which
replaces the traditional Xlib interface.

%package composite
Summary:    XCB Composite Extension

%description composite
%{summary}.

%package damage
Summary:    XCB Damage Extension

%description damage
%{summary}.

%package dbe
Summary:    XCB DBE Extension

%description dbe
%{summary}.

%package dpms
Summary:    XCB DPMS Extension

%description dpms
%{summary}.

%package dri2
Summary:    XCB DRI2 Extension

%description dri2
%{summary}.

%package dri3
Summary:    XCB DRI3 Extension

%description dri3
%{summary}.

%package glx
Summary:    XCB GLX Extension

%description glx
%{summary}.

%package present
Summary:    XCB Present Extension

%description present
%{summary}.

%package randr
Summary:    XCB RandR Extension

%description randr
%{summary}.

%package record
Summary:    XCB Record Extension

%description record
%{summary}.

%package render
Summary:    XCB Render Extension

%description render
%{summary}.

%package res
Summary:    XCB X-Resource Extension

%description res
%{summary}.

%package screensaver
Summary:    XCB Screensaver Extension

%description screensaver
%{summary}.

%package shape
Summary:    XCB Shape Extension

%description shape
%{summary}.

%package shm
Summary:    XCB Shm Extension

%description shm
%{summary}.

%package sync
Summary:    XCB Sync Extension

%description sync
%{summary}.

%package xf86dri
Summary:    XCB XFree86-DRI Extension

%description xf86dri
%{summary}.

%package xfixes
Summary:    XCB XFixes Extension

%description xfixes
%{summary}.

%package xinerama
Summary:    XCB Xinerama Extension

%description xinerama
%{summary}.

%package xinput
Summary:    XCB XInput Extension (EXPERIMENTAL)

%description xinput
%{summary}.

%package xkb
Summary:    XCB Keyboard Extension (EXPERIMENTAL)

%description xkb
%{summary}.

%package xtest
Summary:    XCB XTEST Extension

%description xtest
%{summary}.

%package xv
Summary:    XCB Xv Extension

%description xv
%{summary}.

%package xvmc
Summary:    XCB XvMC Extension

%description xvmc
%{summary}.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-composite = %{version}-%{release}
Requires:   %{name}-damage = %{version}-%{release}
Requires:   %{name}-dbe = %{version}-%{release}
Requires:   %{name}-dpms = %{version}-%{release}
Requires:   %{name}-dri2 = %{version}-%{release}
Requires:   %{name}-dri3 = %{version}-%{release}
Requires:   %{name}-glx = %{version}-%{release}
Requires:   %{name}-present = %{version}-%{release}
Requires:   %{name}-randr = %{version}-%{release}
Requires:   %{name}-record = %{version}-%{release}
Requires:   %{name}-render = %{version}-%{release}
Requires:   %{name}-res = %{version}-%{release}
Requires:   %{name}-screensaver = %{version}-%{release}
Requires:   %{name}-shape = %{version}-%{release}
Requires:   %{name}-shm = %{version}-%{release}
Requires:   %{name}-sync = %{version}-%{release}
Requires:   %{name}-xf86dri = %{version}-%{release}
Requires:   %{name}-xfixes = %{version}-%{release}
Requires:   %{name}-xinerama = %{version}-%{release}
Requires:   %{name}-xinput = %{version}-%{release}
Requires:   %{name}-xkb = %{version}-%{release}
Requires:   %{name}-xtest = %{version}-%{release}
Requires:   %{name}-xv = %{version}-%{release}
Requires:   %{name}-xvmc = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post composite -p /sbin/ldconfig
%postun composite -p /sbin/ldconfig

%post damage -p /sbin/ldconfig
%postun damage -p /sbin/ldconfig

%post dbe -p /sbin/ldconfig
%postun dbe -p /sbin/ldconfig

%post dpms -p /sbin/ldconfig
%postun dpms -p /sbin/ldconfig

%post dri2 -p /sbin/ldconfig
%postun dri2 -p /sbin/ldconfig

%post dri3 -p /sbin/ldconfig
%postun dri3 -p /sbin/ldconfig

%post glx -p /sbin/ldconfig
%postun glx -p /sbin/ldconfig

%post randr -p /sbin/ldconfig
%postun randr -p /sbin/ldconfig

%post record -p /sbin/ldconfig
%postun record -p /sbin/ldconfig

%post render -p /sbin/ldconfig
%postun render -p /sbin/ldconfig

%post res -p /sbin/ldconfig
%postun res -p /sbin/ldconfig

%post screensaver -p /sbin/ldconfig
%postun screensaver -p /sbin/ldconfig

%post shape -p /sbin/ldconfig
%postun shape -p /sbin/ldconfig

%post shm -p /sbin/ldconfig
%postun shm -p /sbin/ldconfig

%post sync -p /sbin/ldconfig
%postun sync -p /sbin/ldconfig

%post present -p /sbin/ldconfig
%postun present -p /sbin/ldconfig

%post xf86dri -p /sbin/ldconfig
%postun xf86dri -p /sbin/ldconfig

%post xfixes -p /sbin/ldconfig
%postun xfixes -p /sbin/ldconfig

%post xkb -p /sbin/ldconfig
%postun xkb -p /sbin/ldconfig

%post xinerama -p /sbin/ldconfig
%postun xinerama -p /sbin/ldconfig

%post xinput -p /sbin/ldconfig
%postun xinput -p /sbin/ldconfig

%post xtest -p /sbin/ldconfig
%postun xtest -p /sbin/ldconfig

%post xv -p /sbin/ldconfig
%postun xv -p /sbin/ldconfig

%post xvmc -p /sbin/ldconfig
%postun xvmc -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files composite
%license COPYING
%{_libdir}/%{name}-composite.so.*

%files damage
%license COPYING
%{_libdir}/%{name}-damage.so.*

%files dbe
%license COPYING
%{_libdir}/%{name}-dbe.so.*

%files dpms
%license COPYING
%{_libdir}/%{name}-dpms.so.*

%files dri2
%license COPYING
%{_libdir}/%{name}-dri2.so.*

%files dri3
%license COPYING
%{_libdir}/%{name}-dri3.so.*

%files glx
%license COPYING
%{_libdir}/%{name}-glx.so.*

%files randr
%license COPYING
%{_libdir}/%{name}-randr.so.*

%files record
%license COPYING
%{_libdir}/%{name}-record.so.*

%files render
%license COPYING
%{_libdir}/%{name}-render.so.*

%files res
%license COPYING
%{_libdir}/%{name}-res.so.*

%files screensaver
%license COPYING
%{_libdir}/%{name}-screensaver.so.*

%files shape
%license COPYING
%{_libdir}/%{name}-shape.so.*

%files shm
%license COPYING
%{_libdir}/%{name}-shm.so.*

%files sync
%license COPYING
%{_libdir}/%{name}-sync.so.*

%files present
%license COPYING
%{_libdir}/%{name}-present.so.*

%files xf86dri
%license COPYING
%{_libdir}/%{name}-xf86dri.so.*

%files xfixes
%license COPYING
%{_libdir}/%{name}-xfixes.so.*

%files xkb
%license COPYING
%{_libdir}/%{name}-xkb.so.*

%files xinerama
%license COPYING
%{_libdir}/%{name}-xinerama.so.*

%files xinput
%license COPYING
%{_libdir}/%{name}-xinput.so.*

%files xtest
%license COPYING
%{_libdir}/%{name}-xtest.so.*

%files xv
%license COPYING
%{_libdir}/%{name}-xv.so.*

%files xvmc
%license COPYING
%{_libdir}/%{name}-xvmc.so.*

%files devel
%license COPYING
%{_includedir}/xcb
%{_libdir}/%{name}.so
%{_libdir}/%{name}-*.so
%{_libdir}/pkgconfig/xcb.pc
%{_libdir}/pkgconfig/xcb-*.pc

%files doc
%license COPYING
%{_docdir}/%{name}
%{_mandir}/man3/xcb-examples.3*
%{_mandir}/man3/xcb-requests.3*
%{_mandir}/man3/xcb_*.3*
