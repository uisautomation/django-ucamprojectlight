Name: django-ucamprojectlight
Version: 1.1
Release: 1
Summary: University of Cambridge "Project Light" Web templates for Django
Source: %{name}-%{version}.tar.gz
Group: Unknown
License: None
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-setuptools

Requires: python-Django >= 1.6

%Description
This package provides Django templates to implement the University of
Cambridge's "Project Light" Web style.

%Prep
%setup

%Build
python setup.py build

%Install
python setup.py install -O1 --prefix=%{_prefix} --root="${RPM_BUILD_ROOT}" --record=INSTALLED_FILES

%Clean
rm -rf "${RPM_BUILD_ROOT}"

%Files -f INSTALLED_FILES
%defattr(-,root,root)
