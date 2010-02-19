Summary:	A command line HP (Compaq) SmartArray status checker
Name:		arrayprobe
Version:	2.0
Release:	%mkrel 4
License:	GPL
Group:		System/Kernel and hardware
URL:		http://www.strocamp.net/opensource/
Source0:	http://www.strocamp.net/opensource/compaq/downloads/%{name}-%{version}.tar.bz2
Patch0:		arrayprobe_2.0-2.diff
BuildRequires:	kernel-source
BuildRequires:	libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Arrayprobe is a linux commandline utility that reports the status of a HP
(compaq) arraycontroller. This version only supports the newer controllers that
use the cciss driver. It works in two modes. The default mode reports the
status in a single line and can be used as a nagios check. The second mode is
activated by the -r option and prints a complete status report of the
controller and any events in the event queue.

%prep

%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x \
    --with-kernel=`ls -d /usr/src/linux`

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/cron.daily
install -d %{buildroot}%{_mandir}/man1

%makeinstall_std

install -m0644 debian/%{name}.cron.daily %{buildroot}%{_sysconfdir}/cron.daily/%{name}
install -m0644 debian/%{name}.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(0644,root,root) %{_sysconfdir}/cron.daily/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*
