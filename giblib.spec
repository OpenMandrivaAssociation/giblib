%define name    giblib
%define version 1.2.4
%define release %mkrel 3
%define major   1
%define libname %mklibname %{name} %{major}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Simple library and a wrapper for imlib2
License:        GPL
Group:          System/Libraries
URL:            http://linuxbrit.co.uk/giblib
Source:         http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.bz2
BuildRequires:  imlib2-devel
BuildRequires:  freetype-devel

%description
giblib is a utility library used by many of the applications from
linuxbrit.co.uk. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2. The wrapper does two things.
It gives you access to fontstyles, which can be loaded from files,
saved to files or defined dynamically through the API. It also,
and more importantly, wraps imlib2's context API.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{libname}-devel
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_prefix}/doc
chmod 644 %{buildroot}%{_libdir}/lib%{name}.la
%multiarch_binaries %{buildroot}%{_bindir}/%{name}-config

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/%{name}-config
%{_bindir}/%{name}-config
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}

