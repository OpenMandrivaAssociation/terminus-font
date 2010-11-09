%define fontdir %{_datadir}/fonts/terminus
%define consolefontdir %{_prefix}/lib/kbd/consolefonts

Summary:        Fixed width font especially for long hacking sessions
Name:           terminus-font
Version:        4.30
Release:        %mkrel 2
License:        GPLv2+
Group:          System/Fonts/X11 bitmap
URL:            http://terminus-font.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl
BuildRequires:	mkfontdir
BuildRequires:	bdftopcf
Buildarch:      noarch

%description
The Terminus font is a complete set of fixed-size fonts designed
especially for the usage in terms and the console.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--psfdir=%{consolefontdir} \
	--x11dir=%{fontdir}

%install
rm -rf %{buildroot}
%makeinstall_std \
	install-psf \
	fontdir

%__sed -e 's/.pcf.gz//' %{buildroot}%{fontdir}/fonts.dir|%__grep terminus > %{buildroot}%{fontdir}/fonts.alias

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{fontdir} %{buildroot}%{_sysconfdir}/X11/fontpath.d/terminus:unscaled:pri=50

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_sysconfdir}/X11/fontpath.d/terminus:unscaled:pri=50
%{consolefontdir}/*.psf.gz
%{fontdir}
