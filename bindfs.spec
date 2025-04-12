Summary:	Mount a directory elsewhere with changed permissions
Summary(pl.UTF-8):	Montowanie katalogu w innym miejscu z innymi uprawnieniami
Name:		bindfs
Version:	1.18.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://bindfs.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9ed1aea621de3828fe5e193df3bfd942
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

%description -l pl.UTF-8
bindfs to system plików FUSE do odwzorowania lustrzanego katalogu w
innym katalogu, podobnie do mount --bind. Uprawnienia źródłowego
katalogu mogą być jednak modyfikowane na różne sposoby.

Niektóre zastosowania bindfs:
- uczynienie katalogu będącym tylko do odczytu
- uczynienie wszystkich programów niewykonywalnymi
- współdzielenie katalogu z listą użytkowników (lub grup)
- zmodyfikowanie bitów uprawnień przy użyciu reguł o składni jak chmod
- zmiana uprawnień, z jakimi są tworzone pliki

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
%doc ChangeLog README.md TODO
%attr(755,root,root) %{_bindir}/bindfs
%{_mandir}/man1/bindfs.1*
