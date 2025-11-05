Name:		spacebar
Version:	6.5.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Instant messenger for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/spacebar/-/archive/master/spacebar-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(FutureSQL6)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libcrypto) >= 3.0.0
BuildRequires:	phonenumber-devel

%description
Instant messenger for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/spacebar
%{_bindir}/spacebar-fakeserver
%{_datadir}/applications/org.kde.spacebar.desktop
%{_datadir}/metainfo/org.kde.spacebar.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.spacebar.svg
%{_libdir}/libexec/spacebar-daemon
%{_datadir}/knotifications6/spacebar.notifyrc
%{_sysconfdir}/xdg/autostart/org.kde.spacebar.daemon.desktop
