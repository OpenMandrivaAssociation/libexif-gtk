%define major 5
%define libname %mklibname exif-gtk %{major}
%define develname %mklibname exif-gtk -d

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif-gtk
Version:	0.3.5
Release:	15
License:	LGPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-gtk-%{version}.tar.bz2
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)

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

%package -n %{develname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	libexif-gtk-devel

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
%makeinstall_std

%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%doc COPYING ChangeLog
%{_libdir}/*.so.*

%files  -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*




%changelog
* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.3.5-13mdv2011.0
+ Revision: 660618
- update br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-12mdv2011.0
+ Revision: 601045
- rebuild

* Thu Apr 22 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.3.5-11mdv2010.1
+ Revision: 537946
- bump release for build
- dropped major from devel pkg name
  disabled static build
  minor spec cleanups
- cleaned specfile after visit from capt obvious

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-10mdv2010.1
+ Revision: 520768
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.5-9mdv2010.0
+ Revision: 425539
- rebuild

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-8mdv2009.1
+ Revision: 301007
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-7mdv2009.0
+ Revision: 222543
- rebuild
- fix spacing at top of description

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - normalize call to ldconfig in %%post/%%postun

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-6mdv2008.1
+ Revision: 150558
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.3.5-5mdv2008.0
+ Revision: 76823
- Disable GTK_DISABLE_DEPRECATED macro, otherwise it won't compile anymore.


* Mon Jan 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.3.5-4mdv2007.0
+ Revision: 109122
- Fixed devel group. Closes: #28138
- Import libexif-gtk

* Mon Sep 11 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3.5-4mdv2007.0
- Add conflict to ease upgrade from Mdv 2006

* Wed May 17 2006 Till Kamppeter <till@mandriva.com> 0.3.5-3mdk
- Introduced %%mkrel.

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.3.5-2mdk
- Rebuild

* Sat Nov 27 2004 Till Kamppeter <till@mandrakesoft.com> 0.3.5-1mdk
- Updated to version 0.3.5.

