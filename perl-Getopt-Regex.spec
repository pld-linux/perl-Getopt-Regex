%define	pdir	Getopt
%define	pnam	Regex
%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Regex perl module
Summary(pl):	Modu³ perla Getopt-Regex
Name:		perl-Getopt-Regex
Version:	0.02
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-Regex - handle command line options flexibly using regular
expressions.

%description -l pl
Modu³ perla Getopt-Regex.

%prep
%setup -q -n Getopt-Regex-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Getopt/Regex.pm
%{_mandir}/man3/*
