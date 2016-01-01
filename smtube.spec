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
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-linguist >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/smtube

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc Readme.txt Release_notes.txt Changelog
%attr(755,root,root) %{_bindir}/smtube
%{_desktopdir}/smtube.desktop
%{_iconsdir}/hicolor/*/apps/smtube.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(bg) %{_datadir}/%{name}/translations/smtube_bg.qm
%lang(cs) %{_datadir}/%{name}/translations/smtube_cs.qm
%lang(da) %{_datadir}/%{name}/translations/smtube_da.qm
%lang(de) %{_datadir}/%{name}/translations/smtube_de.qm
%lang(en) %{_datadir}/%{name}/translations/smtube_en.qm
%lang(en_GB) %{_datadir}/%{name}/translations/smtube_en_GB.qm
%lang(es) %{_datadir}/%{name}/translations/smtube_es.qm
%lang(eu) %{_datadir}/%{name}/translations/smtube_eu.qm
%lang(fr) %{_datadir}/%{name}/translations/smtube_fr.qm
%lang(gl) %{_datadir}/%{name}/translations/smtube_gl.qm
%lang(he_IL) %{_datadir}/%{name}/translations/smtube_he_IL.qm
%lang(hr) %{_datadir}/%{name}/translations/smtube_hr.qm
%lang(hu) %{_datadir}/%{name}/translations/smtube_hu.qm
%lang(it) %{_datadir}/%{name}/translations/smtube_it.qm
%lang(ja) %{_datadir}/%{name}/translations/smtube_ja.qm
%lang(ko) %{_datadir}/%{name}/translations/smtube_ko.qm
%lang(ms) %{_datadir}/%{name}/translations/smtube_ms.qm
%lang(nn_NO) %{_datadir}/%{name}/translations/smtube_nn_NO.qm
%lang(pl) %{_datadir}/%{name}/translations/smtube_pl.qm
%lang(pt) %{_datadir}/%{name}/translations/smtube_pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/smtube_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/translations/smtube_ru.qm
%lang(sq) %{_datadir}/%{name}/translations/smtube_sq.qm
%lang(sr) %{_datadir}/%{name}/translations/smtube_sr.qm
%lang(tr) %{_datadir}/%{name}/translations/smtube_tr.qm
%lang(uk) %{_datadir}/%{name}/translations/smtube_uk.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/smtube_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/smtube_zh_TW.qm
