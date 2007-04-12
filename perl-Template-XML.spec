%define module  Template-XML
%define name	perl-%{module}
%define	modprefix Template

%define version 2.16

%define	rel	1
%define release %mkrel %{rel}

%define _provides_exceptions perl(XML::

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	XML plugin for the Template Toolkit
License:	Artistic/GPL
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
URL:		http://www.template-toolkit.org
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Template) >= 2.15
BuildRequires:	perl(XML::DOM) >= 1.27
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Parser) >= 2.19
BuildRequires:	perl(XML::RSS) >= 0.9
BuildRequires:	perl(XML::Simple) >= 2
BuildRequires:	perl(XML::XPath) >= 1
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Template-XML distribution provides a number of Template Toolkit
plugin modules for working with XML.

The basic XML plugins were distributed as part of the Template Toolkit
until version 2.15 released in May 2006. At this time they were
extracted into this separate Template-XML distribution and an alpha
version of this Template::Plugin::XML front-end module was added.


%prep
%setup -q -n %{module}-%{version}

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

