Summary:	A package for maintenance of constant databases
Summary(pl):    Sta³a baza danych
Name:		tinycdb
Version:	0.73
Release:	1
License:	Public Domain
Group:		Applications/Databases
URL:		http://www.corpit.ru/mjt/tinycdb.html
Source0:	ftp://ftp.corpit.ru/pub/tinycdb/%{name}-%version.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tinycdb is a small, fast and reliable utility set and subroutine
library for creating and reading constant databases. The database
structure is tuned for fast reading:

 - Successful lookups take normally just two disk accesses.
 - Unsuccessful lookups take only one disk access.
 - Small disk space and memory size requirements; a database uses 2048
   bytes for the header and 24 bytes per record.
 - Maximum database size is 4GB; individual record size is not
   otherwise limited.
 - Portable file format.
 - Fast creation of new databases.
 - No locking, updates are atomical.

This package contains the utility.

%description -l pl
tinycdb jest szybkim, wiarygodnym, ma³ym pakietem do tworzenia i
czytania sta³ych baz danych. Struktura bazy zosta³a zoptymalizowana do
szybkiego odczytu:

- Udane odwo³ania normalnie potrzebuj± tylko dwóch odwo³añ do dysku.
- Nieudane odwo³ania potrzebuj± tylko jednego odwo³ania do dysku.
- Ma³e wymagania co do miejsca do dysku i pamiêci; baza danych u¿ywa
  2048 bajtów na nag³ówek i 24 bajtów na rekord.
- Maksymalny rozmiar bazy to 4GB; rozmiar pojedynczego rekordu nie ma
  innych ograniczeñ.
- Przeno¶ny format pliku.
- Szybkie tworzenie nowych baz.
- Nie ma blokowania, zmiany s± atomowe.

Ten pakiet zawiera narzêdzie.

%package devel
Summary:        development libraries and header files for tinycdb
Summary(de):    Entwicklungs-Libraries und Header-Dateien für tinycdb
Summary(fr):    Bibliothèques de développement et en-têtes pour tinycdb
Summary(pl):    Biblioteki i pliki nag³ówkowe dla tinycdb
Summary(tr):    tinycdb için baþlýk dosyalarý ve geliþtirme kitaplýklarý
Group:          Development/Libraries

%description devel
These are the development libraries and header files for tinycdb.
These are required if you plan to do development using the tinycdb
database.

%description devel -l de
Dies sind die Entwicklungs-Libraries und Header-Dateien für tinycdbr.
Sie sind darauf angewiesen, wenn Sie vorhaben, die tinycdb für
Entwicklungsarbeiten zu benutzen.

%description devel -l fr
Ce sont les librairies de développement et les fichiers d'en-tête pour
tinycdb. Ceci est nécessaire si vous désirez développer en utilisant
la base de données tinycdb.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe i biblioteki dla systemu
bazy danych tinycdb.

%description devel -l tr
GNU veri tabaný sistemi tinycdb ile program geliþtirmek için gereken
baþlýk dosyalarý ve kitaplýklar.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man{1,3,5}}

install cdb	$RPM_BUILD_ROOT%{_bindir}
install cdb.h	$RPM_BUILD_ROOT%{_includedir}
install lib*.a	$RPM_BUILD_ROOT%{_libdir}
install cdb.1	$RPM_BUILD_ROOT%{_mandir}/man1
install cdb.3	$RPM_BUILD_ROOT%{_mandir}/man3
install cdb.5	$RPM_BUILD_ROOT%{_mandir}/man5
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_mandir}/man3/*
%{_includedir}/*
