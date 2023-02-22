Summary:	"Heroes 3: WoG recreated
Summary(pl.UTF-8):	Gra "Heroes 3: WoG" stworzona od nowa
Name:		vcmi
Version:	0.99
Release:	7
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://github.com/vcmi/vcmi/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	686c2a0283184add785d50b447db806f
Source1:	http://download.vcmi.eu/core.zip
# Source1-md5:	5cf75d588cc53b93aceb809a6068ae37
Patch0:		boost-1.66.patch
Patch1:		%{name}-boost.patch
Patch2:		no-werror.patch
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
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DENABLE_ERM=ON
# -DENABLE_EDITOR=ON breaks build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{64x64,48x48,32x32}/apps

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# not packaged
%{__rm} -r $RPM_BUILD_ROOT{%{_libdir}/libfuzzylite-static.a,%{_includedir}/fl}

install client/icons/vcmiclient.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/vcmiclient.xpm
install client/icons/vcmiclient.64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/vcmiclient.png
install client/icons/vcmiclient.48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/vcmiclient.png
install client/icons/vcmiclient.32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/vcmiclient.png

%{__unzip} -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/vcmibuilder
%attr(755,root,root) %{_bindir}/vcmiclient
%attr(755,root,root) %{_bindir}/vcmilauncher
%attr(755,root,root) %{_bindir}/vcmiserver
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libvcmi.so
%dir %{_libdir}/%{name}/AI
%attr(755,root,root) %{_libdir}/%{name}/AI/lib*.so
%dir %{_libdir}/%{name}/scripting
%attr(755,root,root) %{_libdir}/%{name}/scripting/libvcmiERM.so
%{_datadir}/%{name}
%{_desktopdir}/vcmiclient.desktop
%{_desktopdir}/vcmilauncher.desktop
%{_pixmapsdir}/vcmiclient.xpm
%{_iconsdir}/hicolor/*x*/apps/vcmiclient.png
