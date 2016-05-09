Name: jmx_exporter
Version: %{getenv:RPMPACK_VER}
Release: 1%{?dist}
Summary: JMX exporter for Prometheus
License: Apache License 2.0
URL: http://prometheus.io
Source0: %{getenv:JARFILE}
Source1: example_7800.yml
Source2: jmx_exporter.init
%define progdir /opt/%{name}

%description

%prep

%install
install -p -d %{buildroot}%{progdir}/{bin,conf/sd,conf/targets,lib}
install -p -d %{buildroot}/data/logs/%{name}
install -p -d %{buildroot}/var/run/%{name}
install -p -d %{buildroot}%{_initrddir}
install -p -D -m 644 %{S:0} %{buildroot}%{progdir}/lib/%{name}.jar
install -p -D -m 644 %{S:1} %{buildroot}/%{progdir}/conf/
install -p -D -m 755 %{S:2} %{buildroot}/%{progdir}/bin/%{name}
ln -sf %{progdir}/bin/%{name} %{buildroot}/%{_initrddir}/%{name}

%files
%defattr(-,root,root,-)
%doc
%{progdir}
%{_initrddir}/%{name}
%dir %attr(-, %{name}, %{name}) /data/logs/%{name}
%dir %attr(-, %{name}, %{name}) /var/run/%{name}

%pre
/usr/bin/getent group %{name} || /usr/sbin/groupadd -r %{name}
/usr/bin/getent passwd %{name} || /usr/sbin/useradd -g %{name} -r -M -s /bin/bash %{name}

%preun
%{_initrddir}/%{name} stop

