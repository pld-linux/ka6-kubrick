#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kubrick
Summary:	kubrick
Summary(pl.UTF-8):	kubrick
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	560228c08ff74b18954ea68afc46f85c
URL:		http://www.kde.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6OpenGL-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kubrick is a game based on the Rubik's Cube™ puzzle. The cube sizes
range from 2x2x2 up to 6x6x6, or you can play with irregular "bricks"
such as 5x3x2 or "mats" such as 6x4x1 or 2x2x1. The game has a
selection of puzzles at several levels of difficulty, as well as demos
of pretty patterns and solution moves, or you can make up your own
puzzles.

%description -l pl.UTF-8
Kubrick jest oparty na kostce Rubika z rozmiarami kostki w zakresie od
2x2x2 do 6x6x6, a także nieregularnymi kształtami, takimi jak: 5x3x2,
6x4x1 czy 2x2x1. Gra zawiera wybór zagadek do rozwiązania różnego
poziomu trudności, a także dema, ciekawe wzory, a także rozwiązania.
Możesz także tworzyć własne układy.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kubrick
%{_desktopdir}/org.kde.kubrick.desktop
%{_iconsdir}/hicolor/*x*/apps/kubrick.png
%{_datadir}/kubrick
%{_datadir}/metainfo/org.kde.kubrick.appdata.xml
%{_datadir}/qlogging-categories6/kubrick.categories
%{_datadir}/qlogging-categories6/kubrick.renamecategories
