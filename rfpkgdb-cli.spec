Name:           rfpkgdb-cli
Version:        2.15.0
Release:        0.6rc2%{?dist}
Summary:        A CLI for pkgdb

License:        GPLv2+
URL:            https://github.com/rpmfusion-infra/rfpkgdb-cli
Source0:        %{url}/archive/v%{version}rc2/%{name}-%{version}rc2.tar.gz
Patch0:         py3.patch

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-fedora
BuildRequires:  python3-bugzilla
BuildRequires:  koji


Requires(post): python3-fedora
Requires(post): python3-requests
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
%autosetup -p1 -n %{name}-%{version}rc2


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

