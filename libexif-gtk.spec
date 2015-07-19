%define major	5
%define libname	%mklibname exif-gtk %{major}
%define devname	%mklibname exif-gtk -d

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif-gtk
Version:	0.3.5
Release:	23
License:	LGPLv2
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libexif)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This library does not contain any documentation, but it seems to make
the connection between libexif, the core library for EXIF, and
GTK-based graphical frontends.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Group:		Graphics
Provides:	libexif-gtk

%description  -n %{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This library does not contain any documentation, but it seems to make
the connection between libexif, the core library for EXIF, and
GTK-based graphical frontends.

%package -n %{devname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains all files which one needs to compile programs using
the "%{name}" library.

%prep
%setup -q

# Disable GTK_DISABLE_DEPRECATED macro
sed -i s/-DGTK_DISABLE_DEPRECATED// */Makefile.*

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%{_libdir}/libexif-gtk.so.%{major}*

%files  -n %{devname}
%doc COPYING ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

