Name:           freshplayerplugin
Version:        0.3.5
Release:        1%{?dist}
Summary:        PPAPI-host NPAPI-plugin adapter

License:        MIT
URL:            https://github.com/i-rinat/freshplayerplugin
Source0:        https://github.com/i-rinat/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  ragel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  chrpath
BuildRequires:  libavdevice
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(icu-i18n)

%description
For various reasons Firefox developers are not interested now in implementing
PPAPI in Firefox. However that does not mean it cannot be done.

The main goal of this project is to get PPAPI (Pepper) Flash player working in
Firefox. This can be done in two ways. First one is to implement full PPAPI
interface in Firefox itself. Other one is to implement a wrapper, some kind of
adapter which will look like browser to PPAPI plugin and look like NPAPI plugin
for browser.

%prep
%setup -q
#Correct search path
sed -i -e "s;/opt/google/chrome/PepperFlash/libpepflashplayer.so;%{_libdir}/chromium/PepperFlash/libpepflashplayer.so;" data/freshwrapper.conf.example


%build
mkdir build
pushd build
    %cmake ..
    %make_build
popd


%install
install -Dm 755 build/libfreshwrapper-flashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libfreshwrapper-flashplayer.so
install -Dm 644 data/freshwrapper.conf.example %{buildroot}%{_sysconfdir}/freshwrapper.conf
find %{buildroot} -name "*" -exec chrpath --delete {} \; 2>/dev/null

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README.md
%license LICENSE
%{_libdir}/mozilla/plugins/libfreshwrapper-flashplayer.so
%config %{_sysconfdir}/freshwrapper.conf


%changelog
* Wed Apr 13 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.5-1
- Update to 0.3.5

* Mon Dec 21 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.4-1
- Update to 0.3.4

* Mon Oct 05 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.3-1
- Update to 0.3.3

* Tue Aug 18 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.2-1
- Update to 0.3.2

* Mon Jul 06 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.1-1
- Update to 0.3.1

* Thu Jun 11 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.0-1
- Update to 0.3.0

* Sun Apr 26 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.4-1
- Update to 0.2.4

* Mon Feb 16 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.3-1
- Update to 0.2.3

* Fri Jan 23 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.2-2
- Add freshwrapper.conf with path to libpepflashplayer.so

* Fri Jan 16 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.2-1
- Initial release
