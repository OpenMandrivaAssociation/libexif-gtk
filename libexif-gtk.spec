%define major	5
%define libname	%mklibname exif-gtk %{major}
%define develname %mklibname exif-gtk -d

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif-gtk
Version:	0.3.5
Release:	%mkrel 11
License:	LGPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source: http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-gtk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:	libexif-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	libglib2.0-devel

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
Conflicts:	%{_lib}exif-gtk4

%description  -n %{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This library does not contain any documentation, but it seems to make
the connection between libexif, the core library for EXIF, and
GTK-based graphical frontends.

%package -n %{develname}
Summary: Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	libexif-gtk-devel
Obsoletes:	%mklibname exif-gtk 5 -d

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{name}" library.


%prep
%setup -q

# Disable GTK_DISABLE_DEPRECATED macro
sed -i s/-DGTK_DISABLE_DEPRECATED// */Makefile.*

%build
# "autogen" is needed because we have a CVS snapshot.
#./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname}
/sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_libdir}/*.so.*

%files  -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*


