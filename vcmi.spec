Summary:	Heroes 3: WoG recreated
Name:		vcmi
Version:	0.98
Release:	6
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://github.com/vcmi/vcmi/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6a69e52a3380358220eba67332b097c6
Source1:	http://download.vcmi.eu/core.zip
# Source1-md5:	5cf75d588cc53b93aceb809a6068ae37
Patch0:		boost-1.58.patch
Patch1:		ffmpeg3.patch
Patch2:		cxx.patch
URL:		http://www.vcmi.eu/
BuildRequires:	Qt5Network-devel
BuildRequires:	qt5-build
BuildRequires:	Qt5Widgets-devel
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_ttf-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.5
BuildRequires:	ffmpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	libstdc++-devel
Suggests:	smpeg-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fpermissive

# symbols defined in binaries and main library
%define	skip_post_check_so	vcmi/Scripting/libvcmiERM.so.0.0.0

%description
H3 engine rewrie (not another mod) with new possibilities.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{64x64,48x48,32x32}/apps

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install client/icons/vcmiclient.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/vcmiclient.xpm
install client/icons/vcmiclient.64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/vcmiclient.png
install client/icons/vcmiclient.48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/vcmiclient.png
install client/icons/vcmiclient.32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/vcmiclient.png

echo A | %{__unzip} %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/%{name}/lib%{name}*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/AI
%attr(755,root,root) %{_libdir}/%{name}/AI/lib*.so
%{_datadir}/%{name}
%{_desktopdir}/%{name}client.desktop
%{_desktopdir}/vcmilauncher.desktop
%{_pixmapsdir}/%{name}client.xpm
%{_iconsdir}/hicolor/*x*/apps/%{name}client.png
