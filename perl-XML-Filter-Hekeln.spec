#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-Hekeln
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Filter::Hekeln - a SAX stream editor
Summary(pl.UTF-8):	XML::Filter::Hekeln - edytor strumieni SAX
Name:		perl-XML-Filter-Hekeln
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	398f943d2469cd99cba512c2a019df91
URL:		http://search.cpan.org/dist/XML-Filter-Hekeln/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Handler-YAWriter >= 0.1
BuildRequires:	perl-libxml >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Filter::Hekeln Perl module is a sophisticated SAX stream editor.

Hekeln is a SAX filter. This means that you can use a Hekeln object as
a Handler to act on events, and to produce SAX events as a driver for
the next handler in the chain. The name Hekeln sounds like the german
word for crocheting, whats the best to describe, what Hekeln can do on
markup language translation.

%description -l pl.UTF-8
Moduł Perla XML::Filter::Hekeln to wymyślny edytor strumieni SAX.

Hekeln jest filtrem SAX. Oznacza to, że można używać obiektu Hekeln
jako funkcji obsługi zdarzeń oraz do tworzenia zdarzeń SAX jako
sterownik dla następnej funkcji obsługi w łańcuchu. Nazwa Hekeln brzmi
jak niemieckie słowo oznaczające szydełkowanie, co najlepiej oznacza,
co Hekeln może zrobić przy tłumaczeniu języka znaczników.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
