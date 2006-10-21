#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	XML
Summary:	Fast, powerful and easily extensible template processing system
Summary(pl):	Rozbudowany i wydajny system szablonów
Name:		perl-Template-XML
Version:	2.16
Release:	0.1
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f18d8d6d2ce4920f4d5af1a3474285b6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Text-Autoformat >= 1.03
BuildRequires:	perl-Template-Toolkit >= 2.15
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-XML-RSS >= 0.9
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-XPath >= 1.00
BuildRequires:	perl-XML-DOM >= 1.27
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Template-Toolkit >= 2.15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
#TODO

%description -l pl
#TODO

%package -n Template-Plugin-XML-DOM
Summary:	XML::DOM plugin for Template Toolkit
Summary(pl):	Wtyczka XML::DOM dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-DOM

%description -n Template-Plugin-XML-DOM
XML::DOM plugin for Template Toolkit - interface to the XML::DOM
module.

%description -n Template-Plugin-XML-DOM -l pl
Wtyczka XML::DOM dla pakietu Template Toolkit - interfejs do modu³u
XML::DOM.

%package -n Template-Plugin-XML-RSS
Summary:	XML::RSS plugin for Template Toolkit - parsing RSS files
Summary(pl):	Wtyczka XML::RSS dla pakietu Template Toolkit - analiza plików RSS
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-RSS

%description -n Template-Plugin-XML-RSS
XML::RSS plugin for Template Toolkit - interface to the XML::RSS
module. It creates an XML::RSS object, which is then used to parse
specified RSS file. An RSS (Rich Site Summary) file is typically
used to store short news 'headlines' describing different links
within a site.

%description -n Template-Plugin-XML-RSS -l pl
Wtyczka XML::RSS dla pakietu Template Toolkit - interfejs do modu³u
XML::RSS. Tworzy on obiekt XML::RSS, który mo¿na u¿yæ do analizy
podanego pliku RSS. Pliki RSS (Rich Site Summary - obfite streszczenie
witryny) zwykle s± u¿ywane do zapisywania krótkich nowinek opisuj±cych
odno¶niki na witrynie.

%package -n Template-Plugin-XML-Simple
Summary:	XML::Simple plugin for Template Toolkit
Summary(pl):	Wtyczka XML::Simple dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-Simple

%description -n Template-Plugin-XML-Simple
XML::Simple plugin for Template Toolkit - interface to the XML::Simple
module.

%description -n Template-Plugin-XML-Simple -l pl
Wtyczka XML::Simple dla pakietu Template Toolkit - interfejs do modu³u
XML::Simple.

%package -n Template-Plugin-XML-Style
Summary:	XML::Style plugin for Template Toolkit - simple stylesheet-like transformations
Summary(pl):	Wtyczka XML::Style dla pakietu Template Tookit - proste przekszta³cenia styli
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-Style

%description -n Template-Plugin-XML-Style
XML::Style plugin for Template Toolkit. It defines a filter for
performing simple stylesheet based transformations of XML text.

%description -n Template-Plugin-XML-Style -l pl
Wtyczka XML::Style dla pakietu Template Toolkit. Definiuje ona filtr
do wykonywania opartych na arkuszu styli przekszta³ceñ tekstu XML.

%package -n Template-Plugin-XML-XPath
Summary:	XML::XPath plugin for Template Toolkit
Summary(pl):	Wtyczka XML::XPath dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-XML-XPath

%description -n Template-Plugin-XML-XPath
XML::XPath plugin for Template Toolkit - interface to the XML::XPath
module. All methods implemented by the XML::XPath modules are
available. In addition, the XML::XPath::Node::Element module
implements present($view) and content($view) methods method for
seamless integration with Template Toolkit VIEWs. The
XML::XPath::Node::Text module is also adorned with a present($view)
method which presents itself via the view using the 'text' template.

%description -n Template-Plugin-XML-XPath -l pl
Wtyczka XML::XPath dla pakietu Template Toolkit - bêd±ca interfejsem
do modu³u XML::XPath. Dostêpne s± wszystkie metody zaimplementowane w
modu³ach XML::XPath, a ponadto modu³ XML::XPath::Node::Element zawiera
implementacje metod present($view) i content($view) do spójnej
integracji z widokami Toolkitu. Modu³ XML::XPath::Node::Text jest
dodatkowo ulepszony o metodê present($view) prezentuj±c± siê przez
widok przy u¿yciu szablonu 'text'.

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
%{_mandir}/man3/Template::XML*
%{_mandir}/man3/Template::Plugin::XML.*
%{_mandir}/man3/Template::Plugin::XML::[FLV]*

%files -n Template-Plugin-XML-DOM
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/DOM.pm
%{_mandir}/man3/Template::Plugin::XML::DOM*

%files -n Template-Plugin-XML-RSS
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/RSS.pm
%{_mandir}/man3/Template::Plugin::XML::RSS*

%files -n Template-Plugin-XML-Simple
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/Simple.pm
%{_mandir}/man3/Template::Plugin::XML::Simple*

%files -n Template-Plugin-XML-Style
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/Style.pm
%{_mandir}/man3/Template::Plugin::XML::Style*

%files -n Template-Plugin-XML-XPath
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/XML/XPath.pm
%{_mandir}/man3/Template::Plugin::XML::XPath*
