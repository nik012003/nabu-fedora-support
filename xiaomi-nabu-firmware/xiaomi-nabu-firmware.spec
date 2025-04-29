%global _firmwarepath /usr/lib/firmware

Name: xiaomi-nabu-firmware
Version: 1.1
Release: %autorelease
Summary: Firmware package for xiaomi-nabu
URL: https://github.com/map220v/ubuntu-xiaomi-nabu
Source1: %{name}-%{version}.tar.gz
License: Unknown

Requires: qcom-firmware

%description
Firmware for various compoents in Xiaomi Mi Pad 5 including 
touchscreen, audio, SoC.

%prep
tar -xzf %{SOURCE1}

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -r src/firmware/* %{buildroot}%{_firmwarepath}

%files
%{_firmwarepath}/qcom/*
%{_firmwarepath}/novatek/*
%{_firmwarepath}/cirrus/*
