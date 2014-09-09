%define fontdir %{_datadir}/fonts/terminus
%define consolefontdir %{_prefix}/lib/kbd/consolefonts

Summary:        Fixed width font especially for long hacking sessions
Name:           terminus-font
Version:        4.39
Release:        1
License:        GPLv2+
Group:          System/Fonts/X11 bitmap
URL:            http://terminus-font.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/terminus-font/terminus-font-4.39/%{name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:	mkfontdir
BuildRequires:	bdftopcf
BuildRequires:	fontconfig
Buildarch:      noarch

%description
The Terminus font is a complete set of fixed-size fonts designed
especially for the usage in terms and the console.

%prep
%setup -q

%build
sh ./configure \
	--prefix=%{_prefix} \
	--psfdir=%{consolefontdir} \
	--x11dir=%{fontdir}

%install
%makeinstall_std \
	install-psf \
	fontdir

%__sed -e 's/.pcf.gz//' %{buildroot}%{fontdir}/fonts.dir|%__grep terminus > %{buildroot}%{fontdir}/fonts.alias

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{fontdir} %{buildroot}%{_sysconfdir}/X11/fontpath.d/terminus:unscaled:pri=50

%clean

%files
%doc README
%{_sysconfdir}/X11/fontpath.d/terminus:unscaled:pri=50
%{consolefontdir}/*.psf.gz
%{fontdir}
