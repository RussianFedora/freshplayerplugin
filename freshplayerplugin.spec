Name:           freshplayerplugin
Version:        0.3.2
Release:        1%{?dist}
Summary:        PPAPI-host NPAPI-plugin adapter

License:        MIT
URL:            https://github.com/i-rinat/freshplayerplugin
Source0:        https://github.com/i-rinat/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  alsa-lib-devel
BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libconfig-devel
BuildRequires:  libevent-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  uriparser-devel
BuildRequires:  ragel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  chrpath
BuildRequires:  libavdevice
BuildRequires:  libv4l-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel

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
mkdir build && cd build
%cmake ..
make %{?_smp_mflags}


%install
install -Dm 755 build/libfreshwrapper-pepperflash.so %{buildroot}%{_libdir}/mozilla/plugins/libfreshwrapper-pepperflash.so
install -Dm 644 data/freshwrapper.conf.example %{buildroot}%{_sysconfdir}/freshwrapper.conf
find %{buildroot} -name "*" -exec chrpath --delete {} \; 2>/dev/null

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING LICENSE README.md
%{_libdir}/mozilla/plugins/libfreshwrapper-pepperflash.so
%config %{_sysconfdir}/freshwrapper.conf


%changelog
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
