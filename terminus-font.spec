%define fontdir %{_datadir}/fonts/terminus
%define consolefontdir %{_prefix}/lib/kbd/consolefonts

Summary:        Fixed width font especially for long hacking sessions
Name:           terminus-font
Version:        4.35
Release:        %mkrel 1
License:        GPLv2+
Group:          System/Fonts/X11 bitmap
URL:            http://terminus-font.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
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


%changelog
* Sun May 15 2011 Jani Välimaa <wally@mandriva.org> 4.35-1mdv2011.0
+ Revision: 674939
- new version 4.35

* Sat May 07 2011 Jani Välimaa <wally@mandriva.org> 4.34-1
+ Revision: 672164
- fix BRs
- new version 4.34
- drop buildroot definition

* Thu Dec 30 2010 Jani Välimaa <wally@mandriva.org> 4.32-1mdv2011.0
+ Revision: 626372
- new version 4.32
- move buildroot removal from build stage to install stage

* Mon Jul 26 2010 Jani Välimaa <wally@mandriva.org> 4.30-2mdv2011.0
+ Revision: 560891
- clean and simplify .spec

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 4.30-1mdv2011.0
+ Revision: 550321
- new version 4.30

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 4.28-2mdv2010.0
+ Revision: 445417
- rebuild

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - Fixed the current URL

* Sat Feb 21 2009 Götz Waschk <waschk@mandriva.org> 4.28-1mdv2009.1
+ Revision: 343742
- update to new version 4.28

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.26-2mdv2009.0
+ Revision: 269421
- rebuild early 2009.0 package (before pixel changes)

* Wed May 07 2008 Götz Waschk <waschk@mandriva.org> 4.26-1mdv2009.0
+ Revision: 202779
- new version
- update license tag

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 12 2007 Götz Waschk <waschk@mandriva.org> 4.20-4mdv2008.0
+ Revision: 51539
- never use libdir in a noarch package

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 4.20-3mdv2008.0
+ Revision: 49197
- fontpath.d conversion (#31756)
- general spec cleanup/minor fixes
- Import terminus-font




* Mon Aug  7 2006 Götz Waschk <waschk@mandriva.org> 4.20-3mdv2007.0
- fix buildrequires

* Fri Aug  4 2006 Götz Waschk <waschk@mandriva.org> 4.20-2mdv2007.0
- fix deps
- fix location

* Mon Feb 27 2006 Lenny Cartier <lenny@mandriva.com> 4.20-1mdk
- 4.20

* Thu Nov 24 2005 Lenny Cartier <lenny@mandriva.com> 4.16-1mdk
- 4.16

* Fri May 27 2005 Lenny Cartier <lenny@mandriva.com> 4.14-1mdk
- 4.14

* Thu Apr 07 2005 Lenny Cartier <lenny@mandrakesoftc.con> 4.12-1mdk
- 4.12

* Thu Dec 03 2004 Lenny Cartier <lenny@mandrakesoftc.con> 4.11-1mdk
- 4.11

* Thu Dec 18 2003 Han Boetes <han@linux-mandrake.com> 4.06-1mdk
- bump

* Sun Nov  2 2003 Han Boetes <han@linux-mandrake.com> 4.05-2mdk
- Added a fonts.alias entry
- More macros
- Restart xfs

* Mon Oct  6 2003 Han Boetes <han@linux-mandrake.com> 4.05-1mdk
- Whoopy a new a :)

* Thu Jul  3 2003 Han Boetes <han@linux-mandrake.com> 4.03-1mdk
- bump

* Fri May 23 2003 Han Boetes <han@linux-mandrake.com> 4.00-4mdk
- Added dir entries to make Olivier's bot happy. :)
- Some minor cleanups

* Wed May  7 2003 Han Boetes <han@linux-mandrake.com> 4.00-3mdk
- Added the consolefonts.

* Sun Apr 13 2003 Marcel Pol <mpol@gmx.net> 4.00-2mdk
- buildrequires

* Sat Apr 12 2003 Han Boetes <han@linux-mandrake.com> 4.00-1mdk
- Initial mandrake release.
