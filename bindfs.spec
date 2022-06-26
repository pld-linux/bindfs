Summary:	Mount a directory elsewhere with changed permissions
Name:		bindfs
Version:	1.16.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://bindfs.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c07f12a76c6b0eb15bbd74ae22c215a4
URL:		https://bindfs.org/
BuildRequires:	libfuse3-devel >= 3.4.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libfuse3 >= 3.4.0
Requires:	libfuse3-tools >= 3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bindfs is a FUSE filesystem for mirroring a directory to another
directory, similarly to mount --bind. The permissions of the mirrored
directory can be altered in various ways.

Some things bindfs can be used for:
- Making a directory read-only.
- Making all executables non-executable.
- Sharing a directory with a list of users (or groups).
- Modifying permission bits using rules with chmod-like syntax.
- Changing the permissions with which files are created.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/bindfs
%{_mandir}/man1/bindfs.1*
