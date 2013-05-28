Summary:	Heroes 3: WoG recreated
Name:		vcmi
Version:	0.90
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.vcmi.eu/%{name}_%{version}.tar.gz
# Source0-md5:	ab6772d9b8010925e6c00847b7c63c0d
Source1:	http://download.vcmi.eu/core.zip
# Source1-md5:	5cf75d588cc53b93aceb809a6068ae37
Source2:	ax_boost_iostreams.m4
Patch0:		boost-build.patch
URL:		http://www.vcmi.eu/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1.11
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
cp %{SOURCE2} aclocal/m4

%build
%{__aclocal} -I aclocal/m4
%{__autoconf}
%{__automake}
export CXXFLAGS="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{64x64,48x48,32x32}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install client/icons/vcmiclient.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/vcmiclient.xpm
install client/icons/vcmiclient.64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/vcmiclient.png
install client/icons/vcmiclient.48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/vcmiclient.png
install client/icons/vcmiclient.32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/vcmiclient.png

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/AI/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}{/Scripting,}/*.{la,so}

%{__unzip} %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/%{name}/lib%{name}*.so.?.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/lib%{name}*.so.?
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/AI
%attr(755,root,root) %{_libdir}/%{name}/AI/lib*.so
%dir %{_libdir}/%{name}/Scripting
%attr(755,root,root) %{_libdir}/%{name}/Scripting/lib*.so.?.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/Scripting/lib*.so.?
%{_datadir}/%{name}
%{_desktopdir}/%{name}client.desktop
%{_pixmapsdir}/%{name}client.xpm
%{_iconsdir}/hicolor/*x*/apps/%{name}client.png
