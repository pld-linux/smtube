# TODO
# - smtube: use system qtsingleapplication

%define		qtver	5.0
%define		smver	14.8.0
Summary:	SMTube - YouTube browser for SMPlayer
Name:		smtube
Version:	21.10.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/smtube/%{name}-%{version}.tar.bz2
# Source0-md5:	93383ae9220614d7e9fc5fbbbb8f060b
URL:		https://www.smtube.org/
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	desktop-file-utils
Recommends:	yt-dlp
Obsoletes:	smplayer-smtube < 15.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMTube is an application that allows to browse, search and play
YouTube videos. Videos are played back with a media player (by default
SMPlayer) instead of a flash player, this allows better performance,
particularly with HD content.

%prep
%setup -q

# skip docs install
%{__sed} -i -e '/DOC_PATH/d' src/smtube.pro

# skip manpage compress
%{__sed} -i -e '/gzip/d' Makefile

# skip build rule on install
%{__sed} -i -e 's,install: src/smplayer,install:,' Makefile

%build
%{__make} \
	PREFIX=%{_prefix} \
	QMAKE=qmake-qt5 \
	LRELEASE=lrelease-qt5

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/smtube

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Readme.txt README.md Release_notes.md
%attr(755,root,root) %{_bindir}/smtube
%{_desktopdir}/smtube.desktop
%{_iconsdir}/hicolor/*/apps/smtube.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
