#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glance
Version  : 12.0.0
Release  : 52
URL      : http://tarballs.openstack.org/glance/glance-12.0.0.tar.gz
Source0  : http://tarballs.openstack.org/glance/glance-12.0.0.tar.gz
Source1  : glance-api.service
Source2  : glance-registry.service
Source3  : glance-scrubber.service
Source4  : glance.tmpfiles
Summary  : OpenStack Image Service
Group    : Development/Tools
License  : Apache-2.0
Requires: glance-bin
Requires: glance-python
Requires: glance-config
Requires: glance-data
BuildRequires : SQLAlchemy-python
BuildRequires : WSME-python
BuildRequires : castellan-python
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : debtcollector-python
BuildRequires : futurist-python
BuildRequires : glance_store-python
BuildRequires : iso8601-python
BuildRequires : keystonemiddleware
BuildRequires : monotonic-python
BuildRequires : oslo.db-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.policy-python
BuildRequires : osprofiler-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycrypto-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : pytz-python
BuildRequires : semantic_version-python
BuildRequires : setuptools
BuildRequires : sqlalchemy-migrate-python
BuildRequires : taskflow-python
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-Enable-systemd-notification.patch
Patch2: 0002-Default-configuration-values.patch
Patch3: 0003-move-json-metadefs-to-stateless-dir.patch

%description
This is a database migration repository.
More information at
http://code.google.com/p/sqlalchemy-migrate/

%package bin
Summary: bin components for the glance package.
Group: Binaries
Requires: glance-data
Requires: glance-config

%description bin
bin components for the glance package.


%package config
Summary: config components for the glance package.
Group: Default

%description config
config components for the glance package.


%package data
Summary: data components for the glance package.
Group: Data

%description data
data components for the glance package.


%package python
Summary: python components for the glance package.
Group: Default
Requires: SQLAlchemy-python
Requires: WSME-python
Requires: castellan-python
Requires: cryptography
Requires: debtcollector-python
Requires: futurist-python
Requires: iso8601-python
Requires: keystonemiddleware
Requires: monotonic-python
Requires: oslo.db-python
Requires: oslo.messaging-python
Requires: oslo.middleware-python
Requires: oslo.policy-python
Requires: osprofiler-python
Requires: pycrypto-python
Requires: sqlalchemy-migrate-python
Requires: taskflow-python

%description python
python components for the glance package.


%prep
%setup -q -n glance-12.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/glance-api.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/glance-registry.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/glance-scrubber.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/glance.conf
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.conf %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.ini %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.json %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.sample %{buildroot}/usr/share/defaults/glance/
for i in %{buildroot}/usr/share/defaults/glance/*.sample; do mv $i ${i%.*}; done;
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance-api
/usr/bin/glance-cache-cleaner
/usr/bin/glance-cache-manage
/usr/bin/glance-cache-prefetcher
/usr/bin/glance-cache-pruner
/usr/bin/glance-control
/usr/bin/glance-glare
/usr/bin/glance-manage
/usr/bin/glance-registry
/usr/bin/glance-replicator
/usr/bin/glance-scrubber

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/glance-api.service
/usr/lib/systemd/system/glance-registry.service
/usr/lib/systemd/system/glance-scrubber.service
/usr/lib/tmpfiles.d/glance.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/glance/glance-api-paste.ini
/usr/share/defaults/glance/glance-api.conf
/usr/share/defaults/glance/glance-cache.conf
/usr/share/defaults/glance/glance-glare-paste.ini
/usr/share/defaults/glance/glance-glare.conf
/usr/share/defaults/glance/glance-manage.conf
/usr/share/defaults/glance/glance-registry-paste.ini
/usr/share/defaults/glance/glance-registry.conf
/usr/share/defaults/glance/glance-scrubber.conf
/usr/share/defaults/glance/glance-swift.conf
/usr/share/defaults/glance/metadefs/README
/usr/share/defaults/glance/metadefs/cim-processor-allocation-setting-data.json
/usr/share/defaults/glance/metadefs/cim-resource-allocation-setting-data.json
/usr/share/defaults/glance/metadefs/cim-storage-allocation-setting-data.json
/usr/share/defaults/glance/metadefs/cim-virtual-system-setting-data.json
/usr/share/defaults/glance/metadefs/compute-aggr-disk-filter.json
/usr/share/defaults/glance/metadefs/compute-aggr-iops-filter.json
/usr/share/defaults/glance/metadefs/compute-aggr-num-instances.json
/usr/share/defaults/glance/metadefs/compute-cpu-pinning.json
/usr/share/defaults/glance/metadefs/compute-guest-memory-backing.json
/usr/share/defaults/glance/metadefs/compute-guest-shutdown.json
/usr/share/defaults/glance/metadefs/compute-host-capabilities.json
/usr/share/defaults/glance/metadefs/compute-hypervisor.json
/usr/share/defaults/glance/metadefs/compute-instance-data.json
/usr/share/defaults/glance/metadefs/compute-libvirt-image.json
/usr/share/defaults/glance/metadefs/compute-libvirt.json
/usr/share/defaults/glance/metadefs/compute-quota.json
/usr/share/defaults/glance/metadefs/compute-randomgen.json
/usr/share/defaults/glance/metadefs/compute-trust.json
/usr/share/defaults/glance/metadefs/compute-vcputopology.json
/usr/share/defaults/glance/metadefs/compute-vmware-flavor.json
/usr/share/defaults/glance/metadefs/compute-vmware-quota-flavor.json
/usr/share/defaults/glance/metadefs/compute-vmware.json
/usr/share/defaults/glance/metadefs/compute-watchdog.json
/usr/share/defaults/glance/metadefs/compute-xenapi.json
/usr/share/defaults/glance/metadefs/glance-common-image-props.json
/usr/share/defaults/glance/metadefs/operating-system.json
/usr/share/defaults/glance/metadefs/software-databases.json
/usr/share/defaults/glance/metadefs/software-runtimes.json
/usr/share/defaults/glance/metadefs/software-webservers.json
/usr/share/defaults/glance/metadefs/storage-volume-type.json
/usr/share/defaults/glance/ovf-metadata.json
/usr/share/defaults/glance/policy.json
/usr/share/defaults/glance/property-protections-policies.conf
/usr/share/defaults/glance/property-protections-roles.conf
/usr/share/defaults/glance/schema-image.json

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
