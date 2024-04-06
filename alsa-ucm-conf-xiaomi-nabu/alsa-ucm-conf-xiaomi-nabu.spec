Name: alsa-ucm-conf-xiaomi-nabu
Version: 1.0
Release: %autorelease
Summary: ALSA ucm2 settings for Xiaomi Mi Pad 5 (nabu)
URL: https://github.com/map220v/ubuntu-xiaomi-nabu
Source1: %{name}-%{version}.tar.gz
License: Unknown
BuildArch: noarch

Requires: alsa-ucm 

%description
ALSA Use Case Manager configuration settings for Xiaomi Mi Pad 5 (nabu)

%prep
tar -xzf %{SOURCE1}

%install
install -dm 755 %{buildroot}%{_datadir}/alsa/ucm2/
cp -r src/usr/share/alsa/ucm2/* %{buildroot}%{_datadir}/alsa/ucm2/

%files
%{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf
%{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf