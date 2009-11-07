%define kde_version     4.3.3

Summary: 	kio-gopher
Name: 		kio-gopher
Version: 	0.1.3
Release: 	%mkrel 2
Source:		kio_gopher-%{version}-kde%{kde_version}.tar.bz2
License: 	GPLv2+
Group: 		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://kgopher.berlios.de/
BuildRequires:  kdelibs4-devel

%description
This adds support for the gopher protocol to konqueror.
It is still in development.
It has been tested to work with KDE 3.1 and up.
It has not been tested on other KDE versions.

Currently it supports most (if not all) of the gopher protocol.

Support for gopher+ protocol is planned.

Protocol Documentation:
 Gopher:
  http://www.faqs.org/rfcs/rfc1436.html
 Gopher+:
  http://iubio.bio.indiana.edu/soft/util/gopher/Gopher+-spec.text
 Gopher URL:
  http://www.cotse.com/CIE/RFC/1738/16.htm

%files
%defattr(-,root,root)
%doc README  FAQ
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*
%{_kde_datadir}/locale/*/*/kio_gopher.mo

#--------------------------------------------------------------------

%prep
%setup -qn kio_gopher-%{version}-kde%{kde_version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


