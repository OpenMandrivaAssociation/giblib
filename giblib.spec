%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %name

Summary:	Simple library and a wrapper for imlib2
Name:		giblib
Version:	1.2.4
Release:	12
License:	GPLv2
Group:		System/Libraries
Url:		http://linuxbrit.co.uk/giblib
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
BuildRequires:	freetype-devel
BuildRequires:	pkgconfig(imlib2)

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

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{devname}
Summary:	Development header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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

%files -n %libname
%{_libdir}/libgiblib.so.%{major}*

%files -n %{devname}
%doc README ChangeLog AUTHORS
%{_bindir}/%{name}-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}

