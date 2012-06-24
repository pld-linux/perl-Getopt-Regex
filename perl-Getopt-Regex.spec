%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Regex
Summary:	Getopt::Regex perl module
Summary(pl):	Modu� perla Getopt::Regex
Name:		perl-Getopt-Regex
Version:	0.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Regex - handle command line options flexibly using regular
expressions.

%description -l pl
Modu� perla Getopt::Regex - obs�uguj�cy opcje z linii polece� w spos�b
elastyczny, z u�yciem wyra�e� regularnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Getopt/Regex.pm
%{_mandir}/man3/*
