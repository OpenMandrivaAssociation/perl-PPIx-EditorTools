%define upstream_name    PPIx-EditorTools
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Introduces a temporary variable using PPI
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(PPI)
BuildRequires:	perl(PPI::Find)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::NoWarnings) >= 0.084
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Base class and utility methods for manipulating Perl via PPI. Pulled out
from the 'Padre::Task::PPI' code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jul 08 2011 Shlomi Fish <shlomif@mandriva.org> 0.150.0-2mdv2011
+ Revision: 689367
- Add missing dependcies
- Upgraded to 0.15

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2
+ Revision: 658868
- rebuild for updated spec-helper

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.10

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 448260
- update to 0.09

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 410679
- update to 0.08

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 398909
- update to 0.07

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 396342
- update to 0.06
- forgot to commit the new tarball
- update to 0.05

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 393893
- import perl-PPIx-EditorTools


* Thu Jul 09 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
