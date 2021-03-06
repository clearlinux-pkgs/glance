#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : glance
Version  : 17.0.0
Release  : 74
URL      : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz
Source0  : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz
Source1  : glance-api.service
Source2  : glance-registry.service
Source3  : glance-scrubber.service
Source4  : glance.tmpfiles
Source5  : http://tarballs.openstack.org/glance/glance-17.0.0.tar.gz.asc
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
BuildRequires : Paste
BuildRequires : Paste-python
BuildRequires : PasteDeploy
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : WSME
BuildRequires : WSME-python
BuildRequires : WebOb
BuildRequires : alembic
BuildRequires : alembic-python
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : cursive
BuildRequires : cursive-python
BuildRequires : debtcollector
BuildRequires : debtcollector-python
BuildRequires : defusedxml
BuildRequires : eventlet
BuildRequires : futurist
BuildRequires : glance_store-python
BuildRequires : httplib2
BuildRequires : iso8601
BuildRequires : iso8601-python
BuildRequires : jsonschema
BuildRequires : jsonschema-python
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : monotonic
BuildRequires : monotonic-python
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.db-python
BuildRequires : oslo.i18n
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log
BuildRequires : oslo.log-python
BuildRequires : oslo.messaging
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware
BuildRequires : oslo.middleware-python
BuildRequires : oslo.policy
BuildRequires : oslo.policy-python
BuildRequires : oslo.utils
BuildRequires : osprofiler
BuildRequires : osprofiler-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pytest
BuildRequires : python-swiftclient-python
BuildRequires : retrying
BuildRequires : retrying-python
BuildRequires : six
BuildRequires : sqlalchemy-migrate
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : taskflow
BuildRequires : taskflow-python
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : xattr-python
Patch1: 0001-Unfreeze-jsonschema.patch

%description
Team and repository tags
        ========================

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
Provides: pypi(glance)
Requires: pypi(alembic)
Requires: pypi(castellan)
Requires: pypi(cryptography)
Requires: pypi(cursive)
Requires: pypi(debtcollector)
Requires: pypi(defusedxml)
Requires: pypi(eventlet)
Requires: pypi(futurist)
Requires: pypi(glance_store)
Requires: pypi(httplib2)
Requires: pypi(iso8601)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(keystonemiddleware)
Requires: pypi(os_win)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.db)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.middleware)
Requires: pypi(oslo.policy)
Requires: pypi(oslo.reports)
Requires: pypi(oslo.upgradecheck)
Requires: pypi(oslo.utils)
Requires: pypi(osprofiler)
Requires: pypi(paste)
Requires: pypi(pastedeploy)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(pyopenssl)
Requires: pypi(retrying)
Requires: pypi(routes)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(sqlalchemy_migrate)
Requires: pypi(sqlparse)
Requires: pypi(stevedore)
Requires: pypi(taskflow)
Requires: pypi(webob)
Requires: pypi(wsme)

%description python3
python3 components for the glance package.


%package services
Summary: services components for the glance package.
Group: Systemd services

%description services
services components for the glance package.


%prep
%setup -q -n glance-17.0.0
cd %{_builddir}/glance-17.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584642917
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glance
cp %{_builddir}/glance-17.0.0/LICENSE %{buildroot}/usr/share/package-licenses/glance/294b43b2cec9919063be1a3b49e8722648424779
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
mv %{buildroot}/usr/etc/glance/*  %{buildroot}/usr/share/defaults/glance/
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
/usr/share/defaults/glance/metadefs/image-signature-verification.json
/usr/share/defaults/glance/metadefs/operating-system.json
/usr/share/defaults/glance/metadefs/software-databases.json
/usr/share/defaults/glance/metadefs/software-runtimes.json
/usr/share/defaults/glance/metadefs/software-webservers.json
/usr/share/defaults/glance/metadefs/storage-volume-type.json
/usr/share/defaults/glance/ovf-metadata.json
/usr/share/defaults/glance/policy.json
/usr/share/defaults/glance/property-protections-policies.conf
/usr/share/defaults/glance/property-protections-roles.conf
/usr/share/defaults/glance/rootwrap.conf
/usr/share/defaults/glance/schema-image.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glance/294b43b2cec9919063be1a3b49e8722648424779

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
