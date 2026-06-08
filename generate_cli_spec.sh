#!/bin/bash
set -e

BASE_URL="https://antigravity-cli-auto-updater-974169037036.us-central1.run.app"

# Fetch manifests
AMD64_MANIFEST=$(curl -s "$BASE_URL/manifests/linux_amd64.json")
ARM64_MANIFEST=$(curl -s "$BASE_URL/manifests/linux_arm64.json")

# Extract info using jq
VERSION=$(echo "$AMD64_MANIFEST" | jq -r '.version')
URL_AMD64=$(echo "$AMD64_MANIFEST" | jq -r '.url')
URL_ARM64=$(echo "$ARM64_MANIFEST" | jq -r '.url')

# Generate spec file
cat <<EOF > antigravity-cli.spec
%global debug_package %{nil}

Name:           antigravity-cli
Version:        $VERSION
Release:        1%{?dist}
Summary:        Google Antigravity CLI

License:        Proprietary
URL:            $BASE_URL
Source0:        $URL_AMD64
Source1:        $URL_ARM64
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
EOF

echo "Generated antigravity-cli.spec for version $VERSION"
