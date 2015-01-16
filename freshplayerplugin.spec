Name:           freshplayerplugin
Version:        0.2.2
Release:        1%{?dist}
Summary:        Compatibility layer for ppapi2npapi

License:        MIT
URL:            https://github.com/i-rinat/freshplayerplugin
Source0:        https://github.com/i-rinat/%{name}/archive/v%{version}.tar.gz

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

%description
PPAPI-host NPAPI-plugin adapter.

%prep
%setup -q


%build
mkdir build && cd build
%cmake ..
make %{?_smp_mflags}


%install
install -Dm 755 build/libfreshwrapper-pepperflash.so %{buildroot}%{_libdir}/mozilla/plugins/libfreshwrapper-pepperflash.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING LICENSE.MIT README.md
%{_libdir}/mozilla/plugins/libfreshwrapper-pepperflash.so


%changelog
* Fri Jan 16 2015 vascom <vascom2@gmail.com> 0.2.2-1
- Initial release
