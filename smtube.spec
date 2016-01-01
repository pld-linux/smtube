# TODO
# - smtube: use system qtsingleapplication

%define		qtver	4.3.3-3
%define		smver	14.8.0
Summary:	SMTube - YouTube browser for SMPlayer
Name:		smtube
Version:	15.11.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/smtube/%{name}-%{version}.tar.bz2
# Source0-md5:	c749cc93176d051f01e4c412d84196c5
URL:		http://www.smtube.org/
BuildRequires:	QtWebKit-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-linguist >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	desktop-file-utils
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
	QMAKE=qmake-qt4 \
	LRELEASE=lrelease-qt4

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Readme.txt Release_notes.txt Changelog
%attr(755,root,root) %{_bindir}/smtube
%{_desktopdir}/smtube.desktop
%{_iconsdir}/hicolor/*/apps/smtube.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
