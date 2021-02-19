#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4A34925D05172859 (mahtin@mahtin.com)
#
Name     : cloudflare
Version  : 2.3.1
Release  : 14
URL      : https://files.pythonhosted.org/packages/9b/8c/973e3726c2aa73821bb4272717c6f9f6fc74e69d41ba871bdf97fc671782/cloudflare-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9b/8c/973e3726c2aa73821bb4272717c6f9f6fc74e69d41ba871bdf97fc671782/cloudflare-2.3.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/9b/8c/973e3726c2aa73821bb4272717c6f9f6fc74e69d41ba871bdf97fc671782/cloudflare-2.3.1.tar.gz.asc
Summary  : Python wrapper for the Cloudflare v4 API
Group    : Development/Tools
License  : MIT
Requires: cloudflare-bin = %{version}-%{release}
Requires: cloudflare-license = %{version}-%{release}
Requires: cloudflare-python = %{version}-%{release}
Requires: cloudflare-python3 = %{version}-%{release}
Requires: PyYAML
Requires: jsonlines
Requires: requests
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : jsonlines
BuildRequires : python-future
BuildRequires : requests

%description
=================
        
        Installation
        ------------
        
        Two methods are provided to install this software. Use PyPi (see

%package bin
Summary: bin components for the cloudflare package.
Group: Binaries
Requires: cloudflare-license = %{version}-%{release}

%description bin
bin components for the cloudflare package.


%package license
Summary: license components for the cloudflare package.
Group: Default

%description license
license components for the cloudflare package.


%package python
Summary: python components for the cloudflare package.
Group: Default
Requires: cloudflare-python3 = %{version}-%{release}

%description python
python components for the cloudflare package.


%package python3
Summary: python3 components for the cloudflare package.
Group: Default
Requires: python3-core
Provides: pypi(cloudflare)
Requires: pypi(beautifulsoup4)
Requires: pypi(jsonlines)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the cloudflare package.


%prep
%setup -q -n cloudflare-2.3.1
cd %{_builddir}/cloudflare-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133241
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cloudflare
cp %{_builddir}/cloudflare-2.3.1/LICENSE %{buildroot}/usr/share/package-licenses/cloudflare/1857fba4ea5c0240235ad8374c2a15727733798e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")
rm -rf %{buildroot}/${sitedir}/examples
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cli4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cloudflare/1857fba4ea5c0240235ad8374c2a15727733798e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
