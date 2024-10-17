%define upstream_name    Crypt-Eksblowfish
%define upstream_version 0.009

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Blowfish-based Unix crypt() password hash
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Mix)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

Eksblowfish is a variant of the Blowfish cipher, modified to make the key
setup very expensive. ("Eks" stands for "expensive key schedule".) This
doesn't make it significantly cryptographically stronger, but is intended
to hinder brute-force attacks. It also makes it unsuitable for any
application requiring key agility. It was designed by Niels Provos and
David Mazieres for password hashing in OpenBSD. See the
Crypt::Eksblowfish::Bcrypt manpage for the hash algorithm. See the
Crypt::Eksblowfish::Blowfish manpage for the unmodified Blowfish cipher.

Eksblowfish is a parameterised (family-keyed) cipher. It takes a cost
parameter that controls how expensive the key scheduling is. It also takes
a family key, known as the "salt". Cost and salt parameters together define
a cipher family. Within each family, a key determines an encryption
function in the usual way. See the Crypt::Eksblowfish::Family manpage for a
way to encapsulate an Eksblowfish cipher family.

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.0-1
+ Revision: 659894
- update to new version 0.009

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-2mdv2011.0
+ Revision: 555711
- rebuild

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 518481
- update to 0.008

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 471119
- import perl-Crypt-Eksblowfish


* Sun Nov 29 2009 cpan2dist 0.007-1mdv
- initial mdv release, generated with cpan2dist
