%define name sgas-bart
%define version 008
%define release 1

Summary: SGAS Batch system Reporting Tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Licensed under the Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Magnus Jonsson <magnus@hpc2n.umu.se>
Url: http://www.sgas.se/
Requires: python-twisted-core, python-twisted-web, pyOpenSSL, python-dateutil

%description
Tool for generating usage records from LRMS logs and registering the records to SGAS.

%prep
%setup

%build
python setup.py build
cat > sgas-bart.cron <<EOF
#!/bin/bash
# Configure BaRT in /etc/bart/bart.conf and test before uncommenting:
# 
# /usr/bin/bart-logger && /usr/bin/bart-registrant
EOF
chmod +x sgas-bart.cron

%install
python setup.py install --optimize 1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
install -D sgas-bart.cron $RPM_BUILD_ROOT/etc/cron.hourly/sgas-bart
mkdir -p $RPM_BUILD_ROOT/var/spool/bart

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%config(noreplace) /etc/bart/*
%config(noreplace) /etc/cron.hourly/sgas-bart
%dir /var/spool/bart
