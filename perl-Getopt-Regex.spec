%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Regex perl module
Summary(pl):	Modu³ perla Getopt-Regex
Name:		perl-Getopt-Regex
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-Regex-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Getopt-Regex - handle command line options flexibly using regular expressions.

%description -l pl
Modu³ perla Getopt-Regex.

%prep
%setup -q -n Getopt-Regex-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Getopt/Regex
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Getopt/Regex.pm
%{perl_sitearch}/auto/Getopt/Regex

%{_mandir}/man3/*
