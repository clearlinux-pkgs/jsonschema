#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonschema
Version  : 2.6.0
Release  : 25
URL      : http://pypi.debian.net/jsonschema/jsonschema-2.6.0.tar.gz
Source0  : http://pypi.debian.net/jsonschema/jsonschema-2.6.0.tar.gz
Summary  : An implementation of JSON Schema validation for Python
Group    : Development/Tools
License  : MIT
Requires: jsonschema-bin
Requires: jsonschema-legacypython
Requires: jsonschema-python3
Requires: jsonschema-python
Requires: functools32
Requires: webcolors
BuildRequires : funcsigs
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : vcversioner

%description
.. image:: https://img.shields.io/pypi/v/jsonschema.svg
:target: https://pypi.python.org/pypi/jsonschema
.. image:: https://travis-ci.org/Julian/jsonschema.svg?branch=master
:target: https://travis-ci.org/Julian/jsonschema
.. image:: https://img.shields.io/pypi/l/jsonschema.svg
:target: https://pypi.python.org/pypi/jsonschema

%package bin
Summary: bin components for the jsonschema package.
Group: Binaries

%description bin
bin components for the jsonschema package.


%package legacypython
Summary: legacypython components for the jsonschema package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the jsonschema package.


%package python
Summary: python components for the jsonschema package.
Group: Default
Requires: jsonschema-legacypython
Requires: jsonschema-python3

%description python
python components for the jsonschema package.


%package python3
Summary: python3 components for the jsonschema package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jsonschema package.


%prep
%setup -q -n jsonschema-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155584
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1507155584
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonschema

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
