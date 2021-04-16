# Force out of source build
%undefine __cmake_in_source_build

%global commit0 65ac5258cdcd1c1bfdf2d8f29c9518e16bcca445
	

Name:           libadwaita
Version:        1.0.2
Release:        1%{?dist}
License:        LGPLv2+ 
Summary:        The aim of the Adwaita library is to help with developing UI for mobile

Url:            https://gitlab.gnome.org/GNOME/libadwaita
Source0:        https://gitlab.gnome.org/GNOME/libadwaita/-/archive/%{commit0}/libadwaita-%{commit0}.tar.gz


BuildRequires:  cmake

BuildRequires:  meson 
BuildRequires:  vala
BuildRequires:  ninja-build
BuildRequires:	sassc
BuildRequires:	gtk4-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(wayland-protocols)

%description
The aim of the Adwaita library is to help with developing UI for mobile devices
using GTK/GNOME.

%package devel
Summary:        Development files for libadwaita
Requires:       libadwaita = %{version}-%{release}

%description devel
The libadwaita package contains libraries and header files for
developing applications that use libadwaita.

%prep
%autosetup -n %{name}-%{commit0} 

%build
%meson

%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/adwaita-1-demo
%{_libdir}/girepository-1.0/Adw-1.typelib
%{_libdir}/libadwaita-1.so.0
%{_datadir}/gir-1.0/Adw-1.gir
%{_datadir}/vala/vapi/

%files devel
%{_includedir}/libadwaita-1/
%{_libdir}/libadwaita-1.so
%{_libdir}/pkgconfig/libadwaita-1.pc

%changelog
* Wed Apr 14 2021 David Va <davidva AT tuta DOT io> 2.0.0-7.gitf660e9 - 1.0.2-1
- Initial build
