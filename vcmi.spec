Summary:	Heroes 3: WoG recreated
Name:		vcmi
Version:	0.89
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.dropbox.com/u/22372764/vcmi/packages/%{name}_%{version}.tar.gz
# Source0-md5:	3f67cabb2b395f933b0e14c412e0f0f9
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# object defined in binaries and main library
%define	skip_post_check_so	vcmi/Scripting/libvcmiERM.so.0.0.0

%description
H3 engine rewrie (not another mod) with new possibilities.

%prep
%setup

%build
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
export CXXFLAGSc="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/AI/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}{/Scripting,}/*.{la,so}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/{%{name}/lib%{name}.so*,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/lib%{name}*.so.?.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}*.so.?
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/AI
%attr(755,root,root) %{_libdir}/%{name}/AI/lib*.so
%dir %{_libdir}/%{name}/Scripting
%attr(755,root,root) %{_libdir}/%{name}/Scripting/lib*.so.?.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/Scripting/lib*.so.?
%{_desktopdir}/%{name}client.desktop
%{_iconsdir}/%{name}client.png
