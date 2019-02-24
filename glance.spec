#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : glance
Version  : 17.0.0
Release  : 62
URL      : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz
Source0  : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz
Source1  : glance-api.service
Source2  : glance-registry.service
Source3  : glance-scrubber.service
Source4  : glance.tmpfiles
Source99 : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz.asc
Summary  : OpenStack Image Service
Group    : Development/Tools
License  : Apache-2.0
Requires: glance-bin = %{version}-%{release}
Requires: glance-config = %{version}-%{release}
Requires: glance-data = %{version}-%{release}
Requires: glance-license = %{version}-%{release}
Requires: glance-python = %{version}-%{release}
Requires: glance-python3 = %{version}-%{release}
Requires: glance-services = %{version}-%{release}
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: WSME
Requires: WebOb
Requires: alembic
Requires: cryptography
Requires: cursive
Requires: debtcollector
Requires: defusedxml
Requires: eventlet
Requires: futurist
Requires: glance_store
Requires: httplib2
Requires: iso8601
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: monotonic
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.utils
Requires: osprofiler
Requires: pbr
Requires: pyOpenSSL
Requires: retrying
Requires: six
Requires: sqlalchemy-migrate
Requires: sqlparse
Requires: stevedore
Requires: taskflow
BuildRequires : Paste-python
BuildRequires : WSME-python
BuildRequires : alembic-python
BuildRequires : buildreq-distutils3
BuildRequires : cursive-python
BuildRequires : debtcollector-python
BuildRequires : glance_store-python
BuildRequires : httplib2
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : keystonemiddleware
BuildRequires : monotonic-python
BuildRequires : oslo.db-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.policy-python
BuildRequires : osprofiler-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : retrying-python
BuildRequires : taskflow-python
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/tc/badges/glance.svg
:target: http://governance.openstack.org/tc/reference/tags/index.html
:alt: The following tags have been asserted for the Glance project:
"project:official",
"tc:approved-release",
"stable:follows-policy",
"tc:starter-kit:compute",
"vulnerability:managed",
"team:diverse-affiliation",
"assert:supports-upgrade",
"assert:follows-standard-deprecation".
Follow the link for an explanation of these tags.
.. NOTE(rosmaita): the alt text above will have to be updated when
additional tags are asserted for Glance.  (The SVG in the
governance repo is updated automatically.)

%package bin
Summary: bin components for the glance package.
Group: Binaries
Requires: glance-data = %{version}-%{release}
Requires: glance-config = %{version}-%{release}
Requires: glance-license = %{version}-%{release}
Requires: glance-services = %{version}-%{release}

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


%package license
Summary: license components for the glance package.
Group: Default

%description license
license components for the glance package.


%package python
Summary: python components for the glance package.
Group: Default
Requires: glance-python3 = %{version}-%{release}

%description python
python components for the glance package.


%package python3
Summary: python3 components for the glance package.
Group: Default
Requires: python3-core

%description python3
python3 components for the glance package.


%package services
Summary: services components for the glance package.
Group: Systemd services

%description services
services components for the glance package.


%prep
%setup -q -n glance-17.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551032950
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glance
cp LICENSE %{buildroot}/usr/share/package-licenses/glance/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/glance-api.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/glance-registry.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/glance-scrubber.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/glance.conf
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.conf %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.ini %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.json %{buildroot}/usr/share/defaults/glance/
install -p -D -m 644 etc/*.sample %{buildroot}/usr/share/defaults/glance/
for i in %{buildroot}/usr/share/defaults/glance/*.sample; do mv $i ${i%.*}; done;
## install_append end

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
/usr/bin/glance-manage
/usr/bin/glance-registry
/usr/bin/glance-replicator
/usr/bin/glance-scrubber
/usr/bin/glance-wsgi-api

%files config
%defattr(-,root,root,-)
%config /usr/etc/glance/glance-api-paste.ini
%config /usr/etc/glance/glance-api.conf
%config /usr/etc/glance/glance-cache.conf
%config /usr/etc/glance/glance-manage.conf
%config /usr/etc/glance/glance-registry-paste.ini
%config /usr/etc/glance/glance-registry.conf
%config /usr/etc/glance/glance-scrubber.conf
%config /usr/etc/glance/metadefs/README
%config /usr/etc/glance/metadefs/cim-processor-allocation-setting-data.json
%config /usr/etc/glance/metadefs/cim-resource-allocation-setting-data.json
%config /usr/etc/glance/metadefs/cim-storage-allocation-setting-data.json
%config /usr/etc/glance/metadefs/cim-virtual-system-setting-data.json
%config /usr/etc/glance/metadefs/compute-aggr-disk-filter.json
%config /usr/etc/glance/metadefs/compute-aggr-iops-filter.json
%config /usr/etc/glance/metadefs/compute-aggr-num-instances.json
%config /usr/etc/glance/metadefs/compute-cpu-pinning.json
%config /usr/etc/glance/metadefs/compute-guest-memory-backing.json
%config /usr/etc/glance/metadefs/compute-guest-shutdown.json
%config /usr/etc/glance/metadefs/compute-host-capabilities.json
%config /usr/etc/glance/metadefs/compute-hypervisor.json
%config /usr/etc/glance/metadefs/compute-instance-data.json
%config /usr/etc/glance/metadefs/compute-libvirt-image.json
%config /usr/etc/glance/metadefs/compute-libvirt.json
%config /usr/etc/glance/metadefs/compute-quota.json
%config /usr/etc/glance/metadefs/compute-randomgen.json
%config /usr/etc/glance/metadefs/compute-trust.json
%config /usr/etc/glance/metadefs/compute-vcputopology.json
%config /usr/etc/glance/metadefs/compute-vmware-flavor.json
%config /usr/etc/glance/metadefs/compute-vmware-quota-flavor.json
%config /usr/etc/glance/metadefs/compute-vmware.json
%config /usr/etc/glance/metadefs/compute-watchdog.json
%config /usr/etc/glance/metadefs/compute-xenapi.json
%config /usr/etc/glance/metadefs/glance-common-image-props.json
%config /usr/etc/glance/metadefs/image-signature-verification.json
%config /usr/etc/glance/metadefs/operating-system.json
%config /usr/etc/glance/metadefs/software-databases.json
%config /usr/etc/glance/metadefs/software-runtimes.json
%config /usr/etc/glance/metadefs/software-webservers.json
%config /usr/etc/glance/metadefs/storage-volume-type.json
%config /usr/etc/glance/policy.json
%config /usr/etc/glance/rootwrap.conf
/usr/lib/tmpfiles.d/glance.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/glance/glance-api-paste.ini
/usr/share/defaults/glance/glance-api.conf
/usr/share/defaults/glance/glance-cache.conf
/usr/share/defaults/glance/glance-image-import.conf
/usr/share/defaults/glance/glance-manage.conf
/usr/share/defaults/glance/glance-registry-paste.ini
/usr/share/defaults/glance/glance-registry.conf
/usr/share/defaults/glance/glance-scrubber.conf
/usr/share/defaults/glance/glance-swift.conf
/usr/share/defaults/glance/ovf-metadata.json
/usr/share/defaults/glance/policy.json
/usr/share/defaults/glance/property-protections-policies.conf
/usr/share/defaults/glance/property-protections-roles.conf
/usr/share/defaults/glance/rootwrap.conf
/usr/share/defaults/glance/schema-image.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glance/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/glance-api.service
/usr/lib/systemd/system/glance-registry.service
/usr/lib/systemd/system/glance-scrubber.service
