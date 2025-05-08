Name: linux-sm8150
ExclusiveArch: aarch64
Version: 6.14
Release: 6
Summary: AIO package for linux kernel, modules and headers for sm8150 devices.
URL: https://gitlab.com/sm8150-mainline/linux
Source1: %{url}/-/archive/sm8150/%{version}/linux-sm8150-%{version}.tar.gz
License: GPL

Provides: kernel = %{version}-%{release}
Provides: kernel-core = %{version}-%{release}
Provides: kernel-modules = %{version}-%{release}
Provides: kernel-devel = %{version}-%{release}
Provides: kernel-headers = %{version}-%{release}

BuildRequires: kmod, bash, coreutils, tar, git-core, which
BuildRequires: bzip2, xz, findutils, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: zstd
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex, gcc-c++
BuildRequires: rust, rust-src, bindgen, rustfmt, clippy
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: dwarves
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: glibc-static
BuildRequires: rsync
BuildRequires: opencsd-devel >= 1.0.0
BuildRequires: openssl-devel

%description
Mainline kernel for sm8150 (qcom snapdragon 855/860) devices.

%prep
tar -xzf %{SOURCE1}

%build
cd %{name}-%{version}
make defconfig sm8150.config 
cat >> .config << EOF
CONFIG_FW_LOADER_COMPRESS=y
CONFIG_FW_LOADER_COMPRESS_XZ=y
CONFIG_FW_LOADER_COMPRESS_ZSTD=y
CONFIG_OF_RESOLVE=y
CONFIG_OF_OVERLAY=y
EOF
make EXTRAVERSION="-%{release}" -j`nproc`

%install
cd %{name}-%{version}
kernel_version=$(make EXTRAVERSION="-%{release}" kernelrelease)

mkdir -p %{buildroot}/boot/
cp arch/arm64/boot/Image.gz %{buildroot}/boot/vmlinuz-$kernel_version
cp System.map %{buildroot}/boot/System.map-$kernel_version
cp .config %{buildroot}/boot/config-$kernel_version

make EXTRAVERSION="-%{release}" modules_install INSTALL_MOD_PATH=%{buildroot}/usr
make EXTRAVERSION="-%{release}" headers_install INSTALL_HDR_PATH=%{buildroot}/usr
rm %{buildroot}/usr/lib/modules/%{version}*/build

%files
/boot/System.map-%{version}*
/boot/config-%{version}*
/boot/vmlinuz-%{version}*
/usr/lib/modules/%{version}*
/usr/include
