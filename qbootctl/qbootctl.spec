%define service_name qbootctl-mark-bootable.service
Name: qbootctl
Version: 0.2.2
Release: %autorelease
Summary: Qualcomm bootctl HAL for Linux
License: BSD-3-Clause
URL: https://github.com/linux-msm/qbootctl
Source: %{url}/archive/refs/tags/%{version}.tar.gz
Source1: %{service_name}

BuildRequires: make
BuildRequires: libzstd-devel
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
Requires: libzstd
Requires: systemd

%description
This HAL was pulled from AOSP source code and bastardised to build and run on 
a musl/glibc system. This may or may not render any hardware you run it 
on unusable, you have been warned.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE1} %{buildroot}%{_unitdir}

%post
%systemd_post %{service_name}
	
%preun
%systemd_preun %{service_name}
	
%postun
%systemd_postun %{service_name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{service_name}

%changelog
%autochangelog