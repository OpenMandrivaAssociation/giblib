%define major   1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name

Name:		giblib
Version:	1.2.4
Release:	9
Summary:	Simple library and a wrapper for imlib2
License:	GPL
Group:		System/Libraries
URL:		http://linuxbrit.co.uk/giblib
Source:		http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	freetype-devel

%description
giblib is a utility library used by many of the applications from
linuxbrit.co.uk. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2. The wrapper does two things.
It gives you access to fontstyles, which can be loaded from files,
saved to files or defined dynamically through the API. It also,
and more importantly, wraps imlib2's context API.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{develname}
Summary:	Development header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_prefix}/doc
chmod 644 %{buildroot}%{_libdir}/lib%{name}.la

%files -n %libname
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_bindir}/%{name}-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-8mdv2011.0
+ Revision: 610853
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1.2.4-7mdv2010.1
+ Revision: 507766
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-6mdv2009.0
+ Revision: 246107
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.4-4mdv2008.1
+ Revision: 132435
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import giblib


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.4-3mdv2007.0
- Rebuild

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.4-2mdk
- fix multiarch 
- %%mkrel
- spec cleanup
- fix summary
- fix libtool file perms
- less strict requires

* Thu Oct 28 2004 Lenny Cartir <lenny@mandrakesoft.com> 1.2.4-1mdk
- 1.2.4

* Wed May 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.2.3-3mdk
- rebuild 
- rpmbuildupdate aware

* Fri Apr 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2.3-2mdk
- fixed buildrequires (Stefan van der Eijk <stefan@eijk.nu>)

* Tue Feb 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2.3-1mdk
- 1.2.3

* Sun Feb 16 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2.2-2mdk
- fix provides

* Sun Feb 09 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2.2-1mdk
- first mdk release, spec stolen from Matthias Saou <matthias.saou@est.une.marmotte.net>
