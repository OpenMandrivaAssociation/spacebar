#define snapshot 20200710
#define commit ae62f708713657e9eb8e614a6b1b95613d34ae11

Name:		spacebar
Version:	0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Instant messenger for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/spacebar/-/archive/master/spacebar-master.tar.bz2
%else
Source0:	https://invent.kde.org/plasma-mobile/spacebar/-/archive/v%{version}/spacebar-v%{version}.tar.bz2
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Notifications)

%description
Instant messenger for Plasma Mobile

%prep
%if 0%{?snapshot}
%autosetup -p1 -n spacebar-master
%else
%autosetup -p1 -n spacebar-v%{version}
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/spacebar
%{_datadir}/applications/org.kde.spacebar.desktop
%{_datadir}/metainfo/org.kde.spacebar.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.spacebar.svg
%{_libdir}/libexec/spacebar-daemon
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.SpaceObserver.service
%{_datadir}/knotifications5/spacebar.notifyrc
%{_datadir}/telepathy/clients/SpaceObserver.client
