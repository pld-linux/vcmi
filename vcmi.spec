Summary:	"Heroes 3: WoG recreated
Summary(pl.UTF-8):	Gra "Heroes 3: WoG" stworzona od nowa
Name:		vcmi
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://github.com/vcmi/vcmi/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6a657666e335bfde5f007b9542a08cfa
Source1:	http://download.vcmi.eu/core.zip
# Source1-md5:	5cf75d588cc53b93aceb809a6068ae37
Patch0:		erm.patch
URL:		http://www.vcmi.eu/
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SDL2_image-devel >= 2
BuildRequires:	SDL2_mixer-devel >= 2
BuildRequires:	SDL2_ttf-devel >= 2
BuildRequires:	boost-devel >= 1.50
BuildRequires:	cmake >= 2.8.12
# avformat, swscale
BuildRequires:	ffmpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	minizip-devel
BuildRequires:	qt5-build >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Suggests:	smpeg-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fpermissive

# symbols defined in binaries and main library
%define		skip_post_check_so	vcmi/Scripting/libvcmiERM.so.0.0.0

%description
H3 engine rewrite (not another mod) with new possibilities.

%description -l pl.UTF-8
Napisany od nowa silnik H3 (nie kolejna modyfikacja) z nowymi
możliwościami.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DENABLE_ERM=ON \
	-DENABLE_EDITOR=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{64x64,48x48,32x32}/apps

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__unzip} -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog.md README.md
%attr(755,root,root) %{_bindir}/vcmibuilder
%attr(755,root,root) %{_bindir}/vcmiclient
%attr(755,root,root) %{_bindir}/vcmieditor
%attr(755,root,root) %{_bindir}/vcmilauncher
%attr(755,root,root) %{_bindir}/vcmiserver
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libvcmi.so
%dir %{_libdir}/%{name}/AI
%attr(755,root,root) %{_libdir}/%{name}/AI/lib*.so
%dir %{_libdir}/%{name}/scripting
%attr(755,root,root) %{_libdir}/%{name}/scripting/libvcmiERM.so
%attr(755,root,root) %{_libdir}/%{name}/scripting/libvcmiLua.so
%{_datadir}/%{name}
%{_desktopdir}/vcmiclient.desktop
%{_desktopdir}/vcmieditor.desktop
%{_desktopdir}/vcmilauncher.desktop
%{_iconsdir}/hicolor/*x*/apps/vcmiclient.png
%{_iconsdir}/hicolor/*x*/apps/vcmieditor.png
%{_iconsdir}/hicolor/scalable/apps/vcmiclient.svg
%{_datadir}/metainfo/eu.vcmi.VCMI.metainfo.xml
