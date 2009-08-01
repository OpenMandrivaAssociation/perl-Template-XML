%define upstream_name    Template-XML
%define upstream_version 2.17

%define _provides_exceptions perl(XML::

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	XML plugin for the Template Toolkit
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Template-XML distribution provides a number of Template Toolkit
plugin modules for working with XML.

The basic XML plugins were distributed as part of the Template Toolkit
until version 2.15 released in May 2006. At this time they were
extracted into this separate Template-XML distribution and an alpha
version of this Template::Plugin::XML front-end module was added.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Template
%{_mandir}/*/*
