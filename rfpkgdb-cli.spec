Name:           rfpkgdb-cli
Version:        2.15.2
Release:        2%{?dist}
Summary:        A CLI for pkgdb

License:        GPLv2+
URL:            https://github.com/rpmfusion-infra/rfpkgdb-cli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Requires-an-argument.patch

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#BuildRequires:  python3-rpmfusion
#BuildRequires:  python3-bugzilla
#BuildRequires:  koji


Requires:       python3-fedora
Requires:       python3-requests
Requires:       python3-bugzilla
Requires:       python3-koji
Requires:       python3-beautifulsoup4
Requires:       python3-setuptools
Requires:       python3-rpmfusion-cert

%description
rfpkgdb-cli is a command line interface for the
packagedb of the Rpmfusion project.

It allows you to manage the ACL for your packages as well
as requesting new ACL for new packages.
It also allows you to orphan and/or retire your package(s).

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%files
%doc README.rst LICENSE
%{python3_sitelib}/rfpkgdb2client/
%{python3_sitelib}/rfpkgdb_cli*.egg-info
%{_bindir}/rfpkgdb-cli
%{_bindir}/rfpkgdb-admin


%changelog
* Thu Mar 20 2025 Sérgio Basto <sergio@serjux.com> - 2.15.2-2
- Requires an argument to rfpkgdb-cli

* Thu Mar 20 2025 Sérgio Basto <sergio@serjux.com> - 2.15.2-1
- Update rfpkgdb-cli to 2.15.2
- python3-rpmfusion replaces python3-fedora

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 2.15.1-2
- Rebuilt for Python 3.13

* Thu May 02 2024 Sérgio Basto <sergio@serjux.com> - 2.15.1-1
- Update rfpkgdb-cli to 2.15.1

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.0-0.15rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.0-0.14rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 2.15.0-0.13rc2
- Rebuilt for Python 3.12

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.0-0.12rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.15.0-0.11rc2
- Rebuilt for Python 3.11

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.15.0-0.10rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.15.0-0.9rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 2.15.0-0.8rc2
- Rebuild for python-3.10

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.15.0-0.7rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.15.0-0.6rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 2.15.0-0.5rc2
- Rebuild for python-3.9

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.15.0-0.4rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 2.15.0-0.3rc2
- Rebuild for python-3.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.15.0-0.2rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.15.0-0.1rc2
- Initial Package

