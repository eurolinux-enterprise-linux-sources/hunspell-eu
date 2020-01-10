Name: hunspell-eu
Summary: Basque hunspell dictionaries
%define upstreamid 20080507
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source0: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/adjuntos/eu-ES-hunspell.tar.gz
Source1: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/adjuntos/XUXEN_kode_irekia_eskuliburua-LINUX-OO.pdf
Group: Applications/Text
URL: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/xuxen.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2
BuildArch: noarch

Requires: hunspell

%description
Basque hunspell dictionaries.

%prep
%setup -q -c -n hunspell-eu
cp -p %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p eu-ES/eu-ES.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eu_ES.dic
cp -p eu-ES/eu-ES.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eu_ES.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc XUXEN_kode_irekia_eskuliburua-LINUX-OO.pdf
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20080507-8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080507-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080507-1
- initial version
