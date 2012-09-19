Summary:	Heroes 3: WoG recreated
Name:		vcmi
Version:	0.89
Release:	4
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.dropbox.com/u/22372764/vcmi/packages/%{name}_%{version}.tar.gz
# Source0-md5:	3f67cabb2b395f933b0e14c412e0f0f9
Source1:	http://download.vcmi.eu/%{name}-data_%{version}.tar.gz
# Source1-md5:	e6018250e5363c440c5dcbf2492eda24
Patch0:		boost-1.50.patch
URL:		http://www.vcmi.eu/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
#BuildRequires:	autoconf >= 2.68
#BuildRequires:	automake >= 1.11
BuildRequires:	boost-devel
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
%setup
%patch0 -p1

%build
export CXXFLAGSc="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{Data,Maps,Mp3,Sprites,config}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/AI/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}{/Scripting,}/*.{la,so}

%{__tar} zxf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%{_iconsdir}/%{name}client.png
