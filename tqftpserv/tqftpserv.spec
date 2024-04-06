Name: tqftpserv
Version: 37669ab1e2993f089c8e0bc9eddd353f625f5cda
Release: %autorelease
Summary: Trivial File Transfer Protocol server over AF_QIPCRTR
License: BSD-3-Clause
URL: https://github.com/linux-msm/tqftpserv
Source: %{url}/archive/%{version}.zip

BuildRequires: make
BuildRequires: gcc
BuildRequires: qrtr-devel
BuildRequires: systemd-devel
BuildRequires:  systemd-rpm-macros

%description
TFTP server working over the QRTR protocol, enabling basic 
communication with remote processors (Wi-Fi, modem, sensors...) 
found in recent Qualcomm SoC's.

%prep
%autosetup -p1

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

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