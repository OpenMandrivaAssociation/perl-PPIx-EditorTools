%define upstream_name    PPIx-EditorTools
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Introduces a temporary variable using PPI
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(PPI)
BuildRequires: perl(PPI::Find)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Test::NoWarnings) >= 0.084
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Base class and utility methods for manipulating Perl via PPI. Pulled out
from the 'Padre::Task::PPI' code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
