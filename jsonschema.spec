#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonschema
Version  : 2.4.0
Release  : 13
URL      : https://pypi.python.org/packages/source/j/jsonschema/jsonschema-2.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/j/jsonschema/jsonschema-2.4.0.tar.gz
Summary  : An implementation of JSON Schema validation for Python
Group    : Development/Tools
License  : MIT
Requires: jsonschema-bin
Requires: jsonschema-python
BuildRequires : funcsigs
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
==========
jsonschema
==========
``jsonschema`` is an implementation of `JSON Schema <http://json-schema.org>`_
for Python (supporting 2.6+ including Python 3).

%package bin
Summary: bin components for the jsonschema package.
Group: Binaries

%description bin
bin components for the jsonschema package.


%package python
Summary: python components for the jsonschema package.
Group: Default

%description python
python components for the jsonschema package.


%prep
%setup -q -n jsonschema-2.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonschema

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
