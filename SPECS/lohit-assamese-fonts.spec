%global fontname lohit-assamese
%global fontconf 65-0-%{fontname}.conf
%global metainfo io.pagure.lohit.assamese.font.metainfo

Name:           %{fontname}-fonts
Version:        2.91.5
Release:        3%{?dist}
Summary:        Free Assamese font

Group:          User Interface/X
License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
Requires:       fontpackages-filesystem

%description
This package provides a free Assamese TrueType/OpenType font.


%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-assamese.conf


%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-assamese.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.5-1
- Upstream new release 2.91.5
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.4-2
- Migrated upstream from fedorahosted to pagure.

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.4-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423900 - FTBFS in rawhide

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Pravin Satpute <psatpute@redhat.com> - 2.91.3-1
- Upstream release 2.91.3
- Updates to Unicode 8.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Pravin Satpute <psatpute@redhat.com> - 2.91.2-1
- Upstream release 2.91.2
- Resolved issue https://github.com/pravins/lohit/issues/58.

* Wed Dec 03 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.1-1
- Upstream release 2.91.1
- Resolves #1170142 - [as_IN] Assamese 2.91, Conjuncts rendering issue for some glyphs

* Fri Oct 17 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-2
- Added metainfo for gnome-software

* Mon Oct 13 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Upstream release 2.91.0
- Rewritten all GSUB rules.
- Open type feature available in .fea file for easy reusability.
- Developer friendly glyphname with following AGL guidelines.
- Font Information updated in sfd.
- Support bng2 and beng open type tags.
- "copy reference" feature implemented
- Automated testing support.
- Added test and README file.
- Done with lookup writings.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2 and spec file cleanup
- enabled autohinting in fontconfig file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug #803294

* Thu Mar 01 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release 2.5.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-9
- fixes bug 705348
- patch for correcting fsf address

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-8
- fixes bug 692359

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixes bug 673411

* Wed May 12 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- fixes bug 586308

* Thu Apr 15 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- fixes bug 578029

* Thu Dec 24 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixes bug 548686 and 549319

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Wed Sep 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
