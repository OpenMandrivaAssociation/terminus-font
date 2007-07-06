%define name    terminus-font
%define version 4.20
%define release %mkrel 3
%define summary Fixed width font especially for long hacking sessions

%define fontdir %_datadir/fonts/terminus
%define consolefontdir %_libdir/kbd/consolefonts

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          System/Fonts/X11 bitmap
URL:            http://www.is-vn.bg/hamster/jimmy-en.html
                # http://www.is-vn.bg/hamster/terminus-font-4.05.tar.gz
Source0:        %name-%version.tar.bz2

BuildRoot:      %_tmppath/%name-buildroot

BuildRequires:  perl XFree86-devel mkfontdir bdftopcf
Requires:       XFree86
Requires(post):         chkfontpath
Requires(postun):         chkfontpath
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
%__rm -rf              %buildroot
%__install       -d %buildroot%consolefontdir
%__install *.psf.gz %buildroot%consolefontdir
%__install       -d %buildroot%fontdir
%__install *.pcf.gz %buildroot%fontdir
cd                  %buildroot%fontdir
%_bindir/mkfontdir
%__sed -e 's/.pcf.gz//' fonts.dir|%__grep terminus > fonts.alias


%post
umask 133
/usr/sbin/chkfontpath -q -a %{fontdir}
if pidof xfs &> /dev/null; then
   /sbin/service xfs restart
else
   echo "rpm: I won't restart xfs because it isn't running."
fi

%postun
if [ $1 -eq 0 ]; then
    umask 133
    /usr/sbin/chkfontpath -q -r %{fontdir}
fi
if pidof xfs &> /dev/null; then
   /sbin/service xfs restart
else
   echo "rpm: I won't restart xfs because it isn't running."
fi


%clean
%__rm -rf %buildroot


%files
%defattr(0644,root,root,0755)
%doc README
%fontdir/*
%dir %fontdir
%consolefontdir/*
%dir %consolefontdir
