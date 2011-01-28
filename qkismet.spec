Summary:	Qt4 frontend to kismet
Name:		qkismet
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://qkismet.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qkismet/%{name}-%{version}.tar.bz2
# Source0-md5:	4011311a03ffae7ee34fcd3059e2137c
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qKismet is graphical Kismet client written in Qt. It aims to be a
full-featured client, which provides features allowing easy overview
of Kismet output. Currently it displays networks, clients, alerts and
status messages and allows to sort and filter them.

%prep
%setup -q

%build
cd src
qmake-qt4
sed -i 's,-pipe ,%{rpmcflags} ,g' Makefile.Release
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C src install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qkismet
