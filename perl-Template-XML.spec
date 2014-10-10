%define upstream_name    Template-XML
%define upstream_version 2.17

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(XML::(.*)\\)'
%else
%define _provides_exceptions perl(XML::
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	XML plugin for the Template Toolkit
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Template) >= 2.15
BuildRequires:	perl(XML::DOM) >= 1.27
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Parser) >= 2.19
BuildRequires:	perl(XML::RSS) >= 0.9
BuildRequires:	perl(XML::Simple) >= 2
BuildRequires:	perl(XML::XPath) >= 1
BuildArch:	noarch

%description
The Template-XML distribution provides a number of Template Toolkit
plugin modules for working with XML.

The basic XML plugins were distributed as part of the Template Toolkit
until version 2.15 released in May 2006. At this time they were
extracted into this separate Template-XML distribution and an alpha
version of this Template::Plugin::XML front-end module was added.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%{makeinstall_std}

%files
%doc README
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-1mdv2010.0
+ Revision: 406383
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.17-3mdv2009.0
+ Revision: 241957
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.17-1mdv2008.0
+ Revision: 23193
- 2.17


* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 2.16-1mdv2007.0
- Version 2.16

* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 2.15-2mdv2007.0
- Added BuildRequires perl(XML::LibXML)

* Fri May 26 2006 Scott Karns <scottk@mandriva.org> 2.15-1mdv2007.0
- Initial Mandriva package (was part of perl-Template < 2.15)

