Summary:	A package for maintenance of constant databases
Summary(pl):	Sta³a baza danych
Name:		tinycdb
Version:	0.76
Release:	1
License:	Public Domain
Group:		Applications/Databases
Source0:	ftp://ftp.corpit.ru/pub/tinycdb/%{name}_%{version}.tar.gz
# Source0-md5:	77db6fa098b674819ba1e06689bc87e8
URL:		http://www.corpit.ru/mjt/tinycdb.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyCDB is a very fast and simple package for creating and reading
constant data bases, a data structure introduced by Dan J. Bernstein
in his cdb package. It may be used to speed up searches in a sequence
of (key,value) pairs with very big number of records. Example usage is
indexing a big list of users - where a search will require linear
reading of a large /etc/passwd file, and for many other tasks. It's
usage/API is similar to ones found in BerkeleyDB, gdbm and traditional
*nix dbm/ndbm libraries, and is compatible in great extent to cdb-0.75
package by Dan Bernstein.

CDB is a constant database, that is, it cannot be updated at a
runtime, only rebuilt. Rebuilding is atomic operation and is very
fast - much faster than of many other similar packages. Once created,
CDB may be queried, and a query takes very little time to complete.

This package contains shared library and cdb utility.

%description -l pl
tinycdb jest bardzo szybkim i prostym pakietem do tworzenia i czytania
sta³ych baz danych o strukturze wprowadzonej przez Dana J. Bernsteina
w jego pakiecie cdb. Mo¿e byæ u¿ywana do przyspieszenia wyszukiwania
kolejnych par (klucz,warto¶æ) przy bardzo du¿ej liczbie rekordów.
Przyk³adowe zastosowanie to indeksowanie du¿ej listy u¿ytkowników -
gdzie wyszukiwanie wymaga³oby liniowego odczytu du¿ego pliku
/etc/passwd. Sposób u¿ycia i API s± podobne do znanych z BerkeleyDB,
gdbm czy tradycyjnych uniksowych bibliotek dbm/ndbm i s± kompatybilne
w du¿ym stopniu z pakietem cdb-0.75 Dana Bernsteina.

CDB to sta³a baza danych, co oznacza, ¿e nie mo¿na jej uaktualniaæ, a
jedynie przebudowaæ od pocz±tku. Przebudowanie jest atomow± operacj± i
jest bardzo szybkie - du¿o szybsze ni¿ w przypadku wielu innych
podobnych pakietów. Po utworzeniu bazy CDB mo¿na wykonywaæ zapytania,
których wykonanie jest bardzo szybkie.

Ten pakiet zawiera bibliotekê wspó³dzielon± i narzêdzie cdb.

%package devel
Summary:	Header file for tinycdb
Summary(de):	Header-Datei für tinycdb
Summary(pl):	Plik nag³ówkowy tinycdb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file for tinycdb. It is required if
you plan to do development using the tinycdb database.

%description devel -l pl
W pakiecie tym znajduje siê plik nag³ówkowy dla systemu bazy danych
tinycdb. Jest potrzebny do programowania z u¿yciem tej bazy.

%package static
Summary:	Static tinycdb library
Summary(pl):	Statyczna biblioteka tinycdb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tinycdb library.

%description static -l pl
Statyczna biblioteka tinycdb.

%package -n nss_tinycdb
Summary:	NSS module which uses tinycdb database
Summary(pl):	Modu³ NSS u¿ywaj±cy bazy danych tinycdb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n nss_tinycdb
NSS module which uses tinycdb database to keep passwd, group and
shadow entries.

%description -n nss_tinycdb -l pl
Modu³ NSS u¿ywaj±cy bazy danych tinycdb do przechowywania wpisów
passwd, group i shadow.

%prep
%setup -q

%build
%{__make} -j1 shared staticlib nss \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	NSS_USELIB="\$(SOLIB)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-sharedlib install-nss \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	mandir=%{_mandir} \
	syslibdir=/%{_lib} \
	INSTALLPROG=cdb-shared

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/cdb
%attr(755,root,root) %{_libdir}/libcdb.so.*
%{_mandir}/man1/cdb.1*
%{_mandir}/man5/cdb.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdb.so
%{_mandir}/man3/cdb.3*
%{_includedir}/cdb.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcdb.a

%files -n nss_tinycdb
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_cdb.so.2
/etc/cdb-Makefile
