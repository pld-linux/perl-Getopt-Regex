%include	/usr/lib/rpm/macros.perl
%define		pdir	Getopt
%define		pnam	Regex
Summary:	Getopt::Regex - handle command line options flexibly using regular expressions
Summary(pl.UTF-8):	Getopt::Regex - elastyczna obsługa opcji z linii poleceń przy pomocy wyrażeń regularnych
Name:		perl-Getopt-Regex
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	44054a9d96b88da3b9774ec95dac70c9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Regex Perl module provides a flexible yet simple method for
handling command line options.  It does not stamp over the callers
namespace or, currently, inforce any particular standard for the
options - the user can do this if they want.  By using anonymous
closures sophisticated option specifications can be constructed.

%description -l pl.UTF-8
Moduł Perla Getopt::Regex udostępnia elastyczną i prostą metodę
obsługi opcji z linii poleceń. On nie znakuje przestrzeni nazw
wywołującego, ani, jak dotąd, nie wymusza żadnego konkretnego
standardu odnośnie opcji - użytkownicy mogą to zrobić sami, jeśli
chcą. Korzystając z anonimowych zamknięć, można tworzyć wyszukane
specyfikacje dla opcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/Regex.pm
%{_mandir}/man3/*
