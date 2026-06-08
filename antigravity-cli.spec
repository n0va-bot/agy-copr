%global debug_package %{nil}

Name:           antigravity-cli
Version:        1.0.6
Release:        1%{?dist}
Summary:        Google Antigravity CLI

License:        Proprietary
URL:            https://antigravity-cli-auto-updater-974169037036.us-central1.run.app
Source0:        https://storage.googleapis.com/antigravity-public/antigravity-cli/1.0.6-6458082025406464/linux-x64/cli_linux_x64.tar.gz
Source1:        https://storage.googleapis.com/antigravity-public/antigravity-cli/1.0.6-6458082025406464/linux-arm/cli_linux_arm64.tar.gz
Source2:        https://raw.githubusercontent.com/google-antigravity/antigravity-cli/main/CHANGELOG.md

ExclusiveArch:  x86_64 aarch64

%description
Antigravity CLI flat native build.

%prep
%ifarch x86_64
%setup -q -c -T -a 0 -n antigravity-cli
%endif
%ifarch aarch64
%setup -q -c -T -a 1 -n antigravity-cli
%endif
cp %{SOURCE2} .

%build
# Pre-compiled binary, nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 antigravity %{buildroot}%{_bindir}/agy

%files
%doc CHANGELOG.md
%{_bindir}/agy
