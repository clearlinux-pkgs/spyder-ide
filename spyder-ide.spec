#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spyder-ide
Version  : 4.1.2
Release  : 6
URL      : https://github.com/spyder-ide/spyder/archive/v4.1.2/spyder-4.1.2.tar.gz
Source0  : https://github.com/spyder-ide/spyder/archive/v4.1.2/spyder-4.1.2.tar.gz
Summary  : The Scientific Python Development Environment
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-3.0 MIT
Requires: spyder-ide-bin = %{version}-%{release}
Requires: spyder-ide-data = %{version}-%{release}
Requires: spyder-ide-license = %{version}-%{release}
Requires: spyder-ide-python = %{version}-%{release}
Requires: spyder-ide-python3 = %{version}-%{release}
Requires: PyQt5
Requires: Pygments
Requires: applaunchservices
Requires: atomicwrites
Requires: chardet
Requires: cloudpickle
Requires: diff-match-patch
Requires: intervaltree
Requires: ipython
Requires: jedi
Requires: keyring
Requires: nbconvert
Requires: numpydoc
Requires: paramiko
Requires: parso
Requires: pexpect
Requires: pickleshare
Requires: psutil
Requires: pylint
BuildRequires : PyQt5
BuildRequires : Pygments
BuildRequires : applaunchservices
BuildRequires : atomicwrites
BuildRequires : buildreq-distutils3
BuildRequires : chardet
BuildRequires : cloudpickle
BuildRequires : diff-match-patch
BuildRequires : intervaltree
BuildRequires : ipython
BuildRequires : jedi
BuildRequires : keyring
BuildRequires : nbconvert
BuildRequires : numpydoc
BuildRequires : paramiko
BuildRequires : parso
BuildRequires : pexpect
BuildRequires : pickleshare
BuildRequires : psutil
BuildRequires : pylint

%description
![Spyder — The Scientific Python Development Environment](https://raw.githubusercontent.com/spyder-ide/spyder/master/img_src/spyder_readme_banner.png)

%package bin
Summary: bin components for the spyder-ide package.
Group: Binaries
Requires: spyder-ide-data = %{version}-%{release}
Requires: spyder-ide-license = %{version}-%{release}

%description bin
bin components for the spyder-ide package.


%package data
Summary: data components for the spyder-ide package.
Group: Data

%description data
data components for the spyder-ide package.


%package license
Summary: license components for the spyder-ide package.
Group: Default

%description license
license components for the spyder-ide package.


%package python
Summary: python components for the spyder-ide package.
Group: Default
Requires: spyder-ide-python3 = %{version}-%{release}

%description python
python components for the spyder-ide package.


%package python3
Summary: python3 components for the spyder-ide package.
Group: Default
Requires: python3-core
Provides: pypi(spyder)
Requires: pypi(atomicwrites)
Requires: pypi(chardet)
Requires: pypi(cloudpickle)
Requires: pypi(diff_match_patch)
Requires: pypi(intervaltree)
Requires: pypi(ipython)
Requires: pypi(jedi)
Requires: pypi(keyring)
Requires: pypi(nbconvert)
Requires: pypi(numpydoc)
Requires: pypi(parso)
Requires: pypi(pexpect)
Requires: pypi(pickleshare)
Requires: pypi(psutil)
Requires: pypi(pygments)
Requires: pypi(pylint)
Requires: pypi(pyqt5)
Requires: pypi(pyqtwebengine)
Requires: pypi(python_language_server)
Requires: pypi(pyxdg)
Requires: pypi(pyzmq)
Requires: pypi(qdarkstyle)
Requires: pypi(qtawesome)
Requires: pypi(qtconsole)
Requires: pypi(qtpy)
Requires: pypi(sphinx)
Requires: pypi(spyder_kernels)
Requires: pypi(watchdog)

%description python3
python3 components for the spyder-ide package.


%prep
%setup -q -n spyder-4.1.2
cd %{_builddir}/spyder-4.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588307147
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
mkdir -p %{buildroot}/usr/share/package-licenses/spyder-ide
cp %{_builddir}/spyder-4.1.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/22c12f6b37fae71737eba4178d938fa6a4014003
cp %{_builddir}/spyder-4.1.2/external-deps/spyder-kernels/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/4d8c327cf6d4ba1ac22d4feb6df04672893016ef
cp %{_builddir}/spyder-4.1.2/img_src/oxygen_icon_set/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/8f8bc9efa4291244a381947813e32326ef3c301d
cp %{_builddir}/spyder-4.1.2/spyder/plugins/help/utils/js/mathjax/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/c646d2cd1433560a4b43cb98e7273b59aac4563c
cp %{_builddir}/spyder-4.1.2/spyder/utils/external/binaryornot/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/3a9052b4cf583cf56f81ceec5e688aa475b97032
cp %{_builddir}/spyder-4.1.2/spyder/widgets/github/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-ide/7fe07a375ab07059ff21c6b8a36ccb37811bd67c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/spyder3
/usr/bin/spyder_win_post_install.py

%files data
%defattr(-,root,root,-)
/usr/share/applications/spyder3.desktop
/usr/share/icons/spyder3.png
/usr/share/metainfo/spyder3.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spyder-ide/22c12f6b37fae71737eba4178d938fa6a4014003
/usr/share/package-licenses/spyder-ide/3a9052b4cf583cf56f81ceec5e688aa475b97032
/usr/share/package-licenses/spyder-ide/4d8c327cf6d4ba1ac22d4feb6df04672893016ef
/usr/share/package-licenses/spyder-ide/7fe07a375ab07059ff21c6b8a36ccb37811bd67c
/usr/share/package-licenses/spyder-ide/8f8bc9efa4291244a381947813e32326ef3c301d
/usr/share/package-licenses/spyder-ide/c646d2cd1433560a4b43cb98e7273b59aac4563c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
