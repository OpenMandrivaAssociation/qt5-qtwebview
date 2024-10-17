%define beta %{nil}
%define libpkg %mklibname qt5webview 5
%define devpkg %mklibname qt5webview -d

Summary:	Qt WebView - a module for displaying web content in a QML application
Name:		qt5-qtwebview
Version:	5.15.15
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtwebview-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtwebview-everywhere-opensource-src-%{version}
#Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}-clean.tar.xz
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# From KDE
# [currently no patches]
License:	GPLv2 LGPLv3
Group:		System/Libraries
Url:		https://qt.io/
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5WebChannel)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Sensors)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	qt5-qtquick-private-devel
BuildRequires:	qt5-qtquickwidgets-private-devel
BuildRequires:	qt5-qtqmlmodels-private-devel
BuildRequires:	qmake5
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt WebView provides a way to display web content in a QML application without
necessarily including a full web browser stack by using native APIs where it
makes sense.

%package -n %{libpkg}
Summary:	Qt WebView - a module for displaying web content in a QML application
Group:		System/Libraries

%description -n %{libpkg}
Qt WebView provides a way to display web content in a QML application without
necessarily including a full web browser stack by using native APIs where it
makes sense.

%files -n %{libpkg}
%{_libdir}/libQt5WebView.so.5*
%{_libdir}/qt5/qml/QtWebView
%{_libdir}/qt5/plugins/webview

%package -n %{devpkg}
Summary:	Development files for QtWebEngine
Group:		Development/KDE and Qt
Requires:	%{libpkg} = %{EVRD}

%description -n %{devpkg}
Development files for Qt WebEngine.

%files -n %{devpkg}
%{_includedir}/qt5/QtWebView
%{_libdir}/cmake/Qt5WebView
%{_libdir}/*.prl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt5/mkspecs/modules/*.pri

%package examples
Summary:	Examples for QtWebEngine
Group:		Development/KDE and Qt
Suggests:	%{devpkg} = %{EVRD}

%description examples
Examples for QtWebEngine.

%files examples
%{_libdir}/qt5/examples

%prep
%autosetup -n %(echo %{qttarballdir}|sed -e 's,-opensource,,') -p1
%{_libdir}/qt5/bin/syncqt.pl -version %{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
