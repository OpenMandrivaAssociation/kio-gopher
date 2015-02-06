%define kde_version     4.4.0

Summary: 	kio-gopher
Name: 		kio-gopher
Version: 	0.1.3
Release: 	6
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




%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-5mdv2011.0
+ Revision: 612611
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.1.3-4mdv2010.1
+ Revision: 508861
- Using kde 4.4 tarball

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.3-3mdv2010.1
+ Revision: 465241
- Rebuild against new Qt

* Sat Nov 07 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.1.3-2mdv2010.1
+ Revision: 462412
- First import
- import kio-gopher


* Sun Nov 07 2009 Daniel Lucio <dlucio@okay.com.mx> 0.1.3-1mdv2010.0
- Fist intent
