%global modname h5io
%global commit a73bba4f38f0d96473b1ce6b59a018b45866c771
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.1
Release:        0.1git%{shortcommit}%{?dist}
Summary:        Read and write simple Python objects using HDF5

License:        BSD
URL:            https://github.com/h5io/h5io
Source0:        https://github.com/h5io/h5io/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format.
It is a higher-level package than h5py.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  h5py
BuildRequires:  numpy
BuildRequires:  scipy
Requires:       h5py
Requires:       numpy
Recommends:     scipy

%description -n python2-%{modname}
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format.
It is a higher-level package than h5py.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-h5py
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
Requires:       python3-h5py
Requires:       python3-numpy
Recommends:     python3-scipy

%description -n python3-%{modname}
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format.
It is a higher-level package than h5py.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{modname}*

%changelog
* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-0.1gita73bba4
- Initial package
