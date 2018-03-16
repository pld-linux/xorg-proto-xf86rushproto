# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XF86Rush protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86Rush i pomocnicze
Name:		xorg-proto-xf86rushproto
Version:	1.1.2
Release:	3.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xf86rushproto-%{version}.tar.bz2
# Source0-md5:	b6a96ffdae084e27487a58314008b000
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86Rush protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu XF86Rush i pomocnicze.

%package devel
Summary:	XF86Rush protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86Rush i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-videoproto-devel

%description devel
XF86Rush protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu XF86Rush i pomocnicze.

%prep
%setup -q -n xf86rushproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/xf86rush*.h
%{_pkgconfigdir}/xf86rushproto.pc
