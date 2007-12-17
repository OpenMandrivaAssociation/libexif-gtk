##### GENERAL STUFF #####

%define major	5
%define libname	%mklibname exif-gtk %{major}

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif-gtk
Version:	0.3.5
Release:	%mkrel 5
License:	LGPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/

##### SOURCE FILES #####

Source: http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-gtk-%{version}.tar.bz2

##### ADDITIONAL DEFINITIONS #####

BuildRequires:	libexif-devel libgtk+2.0-devel libglib2.0-devel

##### SUB-PACKAGES #####

%description

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This library does not contain any documentation, but it seems to make
the connection between libexif, the core library for EXIF, and
GTK-based graphical frontends.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Provides:	libexif-gtk
Group:		Graphics
Conflicts:	%{_lib}exif-gtk4

%description  -n %{libname}

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This library does not contain any documentation, but it seems to make
the connection between libexif, the core library for EXIF, and
GTK-based graphical frontends.

%package -n %{libname}-devel
Summary: Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}
Provides:	libexif-gtk-devel
Group:		Development/C

%description -n %{libname}-devel
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
%setup -q

# Disable GTK_DISABLE_DEPRECATED macro
sed -i s/-DGTK_DISABLE_DEPRECATED// */Makefile.*

##### BUILD #####

%build
# "autogen" is needed because we have a CVS snapshot.
#./autogen.sh
%configure2_5x
%make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Install the README files of the source tarball in the doc directory
#cp *.txt $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

%find_lang %{name}

##### PRE/POST INSTALL SCRIPTS #####

%post -n %{libname}
/sbin/ldconfig

%postun -n %{libname}
/sbin/ldconfig

##### CLEAN UP #####

%clean
rm -rf $RPM_BUILD_ROOT

##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libexif-gtk
%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_libdir}/*.so.*

##### %{libname}-devel
%files  -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


