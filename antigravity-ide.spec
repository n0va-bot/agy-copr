%global debug_package %{nil}
%global _debugsource_packages 0
%global __strip /bin/true
%global _build_id_links none

%global package_version 2.0.4
%global upstream_build 6381998290370560

Name:           antigravity-ide
Version:        %{package_version}
Release:        1%{?dist}
Summary:        Google Antigravity IDE - An agentic development platform

License:        LicenseRef-Google-Antigravity
URL:            https://antigravity.google/
Source0:        https://dl.google.com/release2/j0qc3/antigravity/stable/%{version}-%{upstream_build}/linux-x64/Antigravity%%20IDE.tar.gz
Source1:        https://dl.google.com/release2/j0qc3/antigravity/stable/%{version}-%{upstream_build}/linux-arm/Antigravity%%20IDE.tar.gz
Source10:       antigravity-ide.sh
Source11:       antigravity-ide.desktop
Source12:       antigravity-ide-url-handler.desktop
Source13:       antigravity-ide.appdata.xml
Source14:       antigravity-ide-workspace.xml
Source20:       antigravity-ide.png

ExclusiveArch:  x86_64 aarch64

Requires:       alsa-lib
Requires:       at-spi2-core
Requires:       bash
Requires:       cairo
Requires:       curl
Requires:       dbus
Requires:       expat
Requires:       glib2
Requires:       glibc
Requires:       gtk3
Requires:       libcups
Requires:       libgcc
Requires:       libsecret
Requires:       libsoup3
Requires:       libstdc++
Requires:       libx11
Requires:       libxcb
Requires:       libxcomposite
Requires:       libxdamage
Requires:       libxext
Requires:       libxfixes
Requires:       libxkbcommon
Requires:       libxkbfile
Requires:       libxrandr
Requires:       mesa
Requires:       nspr
Requires:       nss
Requires:       openssl
Requires:       pango
Requires:       systemd-libs
Requires:       util-linux-libs
Requires:       webkit2gtk-4.1

Conflicts:      antigravity < 2.0

%description
Google Antigravity IDE - An agentic development platform from Google, 
evolving the IDE into the agent-first era.

This package installs the upstream prebuilt Linux release under
/opt/antigravity-ide and provides a command-line wrapper and desktop entries.

%prep
%ifarch x86_64
%setup -q -c -T -n antigravity-ide -b 0
%endif
%ifarch aarch64
%setup -q -c -T -n antigravity-ide -b 1
%endif

%build
# Upstream ships prebuilt binaries.

%install
install -dm0755 %{buildroot}/opt
cp -a Antigravity* %{buildroot}/opt/antigravity-ide

install -dm0755 %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE10} %{buildroot}%{_bindir}/antigravity-ide

install -Dpm0644 %{SOURCE11} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm0644 %{SOURCE12} %{buildroot}%{_datadir}/applications/%{name}-url-handler.desktop
install -Dpm0644 %{SOURCE13} %{buildroot}%{_metainfodir}/%{name}.appdata.xml
install -Dpm0644 %{SOURCE14} %{buildroot}%{_datadir}/mime/packages/%{name}-workspace.xml
install -Dpm0644 %{SOURCE20} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
/opt/antigravity-ide/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-url-handler.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}-workspace.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jun 08 2026 n0va <n0va@example.com> - 2.0.4-1
- Update to version 2.0.4
