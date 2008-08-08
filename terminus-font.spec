%define fontdir %_datadir/fonts/terminus
%define consolefontdir %_prefix/lib/kbd/consolefonts

Summary:        Fixed width font especially for long hacking sessions
Name:           terminus-font
Version:        4.26
Release:        %mkrel 2
License:        GPLv2+
Group:          System/Fonts/X11 bitmap
URL:            http://www.is-vn.bg/hamster/jimmy-en.html
Source0:        http://www.is-vn.bg/hamster/%name-%version.tar.gz
BuildRoot:      %_tmppath/%name-buildroot
BuildRequires:  perl mkfontdir bdftopcf
Buildarch:      noarch

%description
The Terminus font is a complete set of fixed-size fonts designed
especially for the usage in terms and the console.

%prep
%setup -q

%build
%__make pcf psf
%__gzip *pcf *psf

%install
%__rm -rf           %buildroot
%__install       -d %buildroot%consolefontdir
%__install *.psf.gz %buildroot%consolefontdir
%__install       -d %buildroot%fontdir
%__install *.pcf.gz %buildroot%fontdir
cd                  %buildroot%fontdir
%_bindir/mkfontdir
%__sed -e 's/.pcf.gz//' fonts.dir|%__grep terminus > fonts.alias

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/terminus:unscaled:pri=50

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc README
%fontdir/*
%dir %fontdir
%consolefontdir/*
%dir %consolefontdir
%_sysconfdir/X11/fontpath.d/terminus:unscaled:pri=50
