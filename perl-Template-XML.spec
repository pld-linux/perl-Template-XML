#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Template
%define		pnam	XML
Summary:	Template::XML - XML plugins for the Template Toolkit
Summary(pl.UTF-8):	Template::XML - wtyczki XML dla Template Toolkit
Name:		perl-Template-XML
Version:	2.17
Release:	1
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21a381e6d7da26c78b25e6a1f3e98fff
URL:		http://search.cpan.org/dist/Template-XML/
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Template-Toolkit >= 2.15
BuildRequires:	perl-Text-Autoformat >= 1.03
BuildRequires:	perl-XML-DOM >= 1.27
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-XML-RSS >= 0.9
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-XPath >= 1.00
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Template-Toolkit >= 2.15
Obsoletes:	perl-Template-Toolkit-Plugin-XML-Style
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Template-XML distribution provides a number of Template Toolkit
plugin modules for working with XML.

This package contains eg. the Template::Plugin::XML module being a
front-end to the various other XML plugin modules and the
Template::Plugin::XML::File module through which you can access XML
files.

%description -l pl.UTF-8
Dystrybucja Template-XML udostępnia kilka modułów będących wtyczkami
dla Template Toolkit do pracy z XML-em.

Pakiet ten zawiera m.in. moduł Template::Plugin::XML, będący
frontendem dla różnych innych modułów-wtyczek XML-owych oraz moduł
Template::Plugin::XML::File umożliwiający dostęp do plików w XML-u.

%package -n perl-Template-Plugin-XML-DOM
Summary:	XML::DOM plugin for Template Toolkit
Summary(pl.UTF-8):	Wtyczka XML::DOM dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-DOM

%description -n perl-Template-Plugin-XML-DOM
XML::DOM plugin for Template Toolkit - interface to the XML::DOM
module.

%description -n perl-Template-Plugin-XML-DOM -l pl.UTF-8
Wtyczka XML::DOM dla pakietu Template Toolkit - interfejs do modułu
XML::DOM.

%package -n perl-Template-Plugin-XML-RSS
Summary:	XML::RSS plugin for Template Toolkit - parsing RSS files
Summary(pl.UTF-8):	Wtyczka XML::RSS dla pakietu Template Toolkit - analiza plików RSS
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-RSS

%description -n perl-Template-Plugin-XML-RSS
XML::RSS plugin for Template Toolkit - interface to the XML::RSS
module. It creates an XML::RSS object, which is then used to parse
specified RSS file. An RSS (Rich Site Summary) file is typically used
to store short news 'headlines' describing different links within a
site.

%description -n perl-Template-Plugin-XML-RSS -l pl.UTF-8
Wtyczka XML::RSS dla pakietu Template Toolkit - interfejs do modułu
XML::RSS. Tworzy on obiekt XML::RSS, który można użyć do analizy
podanego pliku RSS. Pliki RSS (Rich Site Summary - obfite streszczenie
witryny) zwykle są używane do zapisywania krótkich nowinek opisujących
odnośniki na witrynie.

%package -n perl-Template-Plugin-XML-Simple
Summary:	XML::Simple plugin for Template Toolkit
Summary(pl.UTF-8):	Wtyczka XML::Simple dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-Simple

%description -n perl-Template-Plugin-XML-Simple
XML::Simple plugin for Template Toolkit - interface to the XML::Simple
module.

%description -n perl-Template-Plugin-XML-Simple -l pl.UTF-8
Wtyczka XML::Simple dla pakietu Template Toolkit - interfejs do modułu
XML::Simple.

%package -n perl-Template-Plugin-XML-XPath
Summary:	XML::XPath plugin for Template Toolkit
Summary(pl.UTF-8):	Wtyczka XML::XPath dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-XPath

%description -n perl-Template-Plugin-XML-XPath
XML::XPath plugin for Template Toolkit - interface to the XML::XPath
module. All methods implemented by the XML::XPath modules are
available. In addition, the XML::XPath::Node::Element module
implements present($view) and content($view) methods method for
seamless integration with Template Toolkit VIEWs. The
XML::XPath::Node::Text module is also adorned with a present($view)
method which presents itself via the view using the 'text' template.

%description -n perl-Template-Plugin-XML-XPath -l pl.UTF-8
Wtyczka XML::XPath dla pakietu Template Toolkit - będąca interfejsem
do modułu XML::XPath. Dostępne są wszystkie metody zaimplementowane w
modułach XML::XPath, a ponadto moduł XML::XPath::Node::Element zawiera
implementacje metod present($view) i content($view) do spójnej
integracji z widokami Toolkitu. Moduł XML::XPath::Node::Text jest
dodatkowo ulepszony o metodę present($view) prezentującą się przez
widok przy użyciu szablonu 'text'.

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
%dir %{perl_vendorlib}/Template/Plugin/XML
%{perl_vendorlib}/Template/Plugin/XML.pm
%dir %{perl_vendorlib}/Template/Plugin/XML
%{perl_vendorlib}/Template/Plugin/XML/[FLV]*.pm
%{perl_vendorlib}/Template/Plugin/XML/Style.pm
%{_mandir}/man3/Template::XML*
%{_mandir}/man3/Template::Plugin::XML.*
%{_mandir}/man3/Template::Plugin::XML::[FLV]*
%{_mandir}/man3/Template::Plugin::XML::Style*

%files -n perl-Template-Plugin-XML-DOM
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/DOM.pm
%{_mandir}/man3/Template::Plugin::XML::DOM*

%files -n perl-Template-Plugin-XML-RSS
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/RSS.pm
%{_mandir}/man3/Template::Plugin::XML::RSS*

%files -n perl-Template-Plugin-XML-Simple
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/Simple.pm
%{_mandir}/man3/Template::Plugin::XML::Simple*

%files -n perl-Template-Plugin-XML-XPath
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/XPath.pm
%{_mandir}/man3/Template::Plugin::XML::XPath*
