Name: tqftpserv
Version: 859c6e3969ffd5e4e53b07991ab9a5b46d89042d
Release: %autorelease
Summary: Trivial File Transfer Protocol server over AF_QIPCRTR
License: BSD-3-Clause
URL: https://github.com/linux-msm/tqftpserv
Source: %{url}/archive/%{version}.zip

BuildRequires: make
BuildRequires: libzstd-devel
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: qrtr-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
Requires: libzstd
Requires: systemd

%description
TFTP server working over the QRTR protocol, enabling basic 
communication with remote processors (Wi-Fi, modem, sensors...) 
found in recent Qualcomm SoC's.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_post %{name}.service
	
%preun
%systemd_preun %{name}.service
	
%postun
%systemd_postun %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog