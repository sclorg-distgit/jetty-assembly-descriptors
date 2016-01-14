%global pkg_name jetty-assembly-descriptors
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        9.8%{?dist}
Summary:        Jetty assembly descriptors used for building

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{pkg_name}-%{version}.tar.bz2
BuildArch:      noarch

Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}jetty-toolchain
BuildRequires:  %{?scl_prefix}maven-surefire-provider-junit
BuildRequires:  %{?scl_prefix}maven-resources-plugin

%description
Jetty assembly descriptors used for building

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} %{SOURCE2} .

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE-2.0.txt epl-v10.html

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-9.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-9.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-9
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Michal Srb <msrb@redhat.com> - 1.0-8
- Migrate away from mvn-rpmbuild (Resolves: #997521)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-5
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov  4 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-2
- Added missing BR on maven-surefire-provider-junit

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Initial version of the package

