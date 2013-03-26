# NOTE: PLD uses elfutils currently
Summary:	ELF object file access library
Summary(de):	Objektdateizugriffs-Library ELF
Summary(pt_BR):	Biblioteca para acesso a arquivos objeto ELF
Summary(es):	Biblioteca para acceso a archivos objeto ELF
Summary(fr):	Bibliothčque de gestion de fichiers ELF
Summary(pl):	Biblioteka dostępu do plików ELF
Summary(pt_BR):	Biblioteca para acesso a arquivos objeto ELF
Summary(ru):	âÉÂĚÉĎÔĹËÁ ÄĎÓÔŐĐÁ Ë ĎÂßĹËÔÎŮÍ ĆÁĘĚÁÍ × ĆĎŇÍÁÔĹ ELF
Summary(tr):	ELF ara kod eriţim kitaplýđý
Summary(uk):	âŚÂĚŚĎÔĹËÁ ÄĎÓÔŐĐŐ ÄĎ ĎÂ'¤ËÔÎÉČ ĆÁĘĚŚ× ĆĎŇÍÁÔŐ ELF
Name:		libelf
Version:	0.8.13
Release:	0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.mr511.de/software/%{name}-%{version}.tar.gz
# Source0-md5:	4136d7b4c04df68b686570afa26988ac
Patch0:		%{name}-hash.patch
URL:		http://www.mr511.de/software/english.html
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
Obsoletes:	libelf0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libelf package contains a library for accessing ELF object files.
Libelf allows you to access the internals of the ELF object file
format, so you can see the different sections of an ELF file.

%description -l de
Diese Library gibt Ihnen Zugang zum Inneren des ELF-Objekt-
Dateiformats. Sie können damit in den verschiedenen Teilen einer
ELF-Datei umherstochern, die Symbole überprüfen und ähnliches.

%description -l es
Esta biblioteca ofrece acceso a datos internos del formato de archivo
objeto ELF. Permite visualizar varias secciones diferentes de un
archivo ELF, observar los símbolos, etc.

%description -l fr
La bibliothčque libelf permet de manipuler des fichiers ELF (format de
programmes exécutables communs ŕ plusieurs Unix dont Linux) et leurs
différentes sections.

%description -l pl
Biblioteka elf umożliwia dostęp do struktury wewnętrznej plików w
formacie ELF. Udostępnia ona funkcje do przeglądania poszczególnych
części ELF-a, a także sprawdzanie symboli itp.

%description -l pt_BR
Esta biblioteca fornece acesso a dados internos do formato de arquivo
objeto ELF. Ele permite visualizar várias seçőes diferentes de um
arquivo ELF, observar os símbolos, etc.

%description -l uk
ăŃ ÂŚÂĚŚĎÔĹËÁ ÎÁÄÁ¤ ÄĎÓÔŐĐ ÄĎ ×ÎŐÔŇŚŰÎŘĎ§ ÓÔŇŐËÔŐŇÉ ĎÂ'¤ËÔÎÉČ ĆÁĘĚŚ×
ĆĎŇÍÁÔŐ ELF. ÷ĎÎÁ ÄĎÚ×ĎĚŃ¤ ×É×ŢÁÔÉ ŇŚÚÎŚ ÓĹËĂŚ§ ELF-ĆÁĘĚŐ, ĐĹŇĹ×ŚŇŃÔÉ
ÓÉÍ×ĎĚÉ Ś Ô.Đ.

%description -l ru
üÔÁ ÂÉÂĚÉĎÔĹËÁ ĐŇĹÄĎÓÔÁ×ĚŃĹÔ ÄĎÓÔŐĐ Ë ×ÎŐÔŇĹÎÎĎÓÔŃÍ ĎÂßĹËÔÎŮČ ĆÁĘĚĎ× ×
ĆĎŇÍÁÔĹ ELF. ďÎÁ ĐĎÚ×ĎĚŃĹÔ ÉÚŐŢÁÔŘ ŇÁÚĚÉŢÎŮĹ ÓĹËĂÉÉ ELF-ĆÁĘĚÁ,
ĐŇĎ×ĹŇŃÔŘ ÓÉÍ×ĎĚŮ É Ô.Ä.

%description -l tr
Bu kitaplýk, ELF ara kod dosyasý içeriđine eriţimi sađlar. ELF
dosyalarýnýn çeţitli yerleri ile oynama, sembolleri kontrol etme gibi
olanaklar sunar.

%description -l uk
ăŃ ÂŚÂĚŚĎÔĹËÁ ÎÁÄÁ¤ ÄĎÓÔŐĐ ÄĎ ×ÎŐÔŇŚŰÎŘĎ§ ÓÔŇŐËÔŐŇÉ ĎÂ'¤ËÔÎÉČ ĆÁĘĚŚ×
ĆĎŇÍÁÔŐ ELF. ÷ĎÎÁ ÄĎÚ×ĎĚŃ¤ ×É×ŢÁÔÉ ŇŚÚÎŚ ÓĹËĂŚ§ ELF-ĆÁĘĚŐ, ĐĹŇĹ×ŚŇŃÔÉ
ÓÉÍ×ĎĚÉ Ś Ô.Đ.

%package devel
Summary:	Development files for libelf
Summary(pl):	Pliki dla programistów libelf
Summary(ru):	ćÁĘĚŮ ÄĚŃ ŇÁÚŇÁÂĎÔËÉ Ó ÉÓĐĎĚŘÚĎ×ÁÎÉĹÍ ÂÉÂĚÉĎÔĹËÉ libelf
Summary(uk):	ćÁĘĚÉ ÄĚŃ ŇĎÚŇĎÂËÉ Ú ×ÉËĎŇÉÓÔÁÎÎŃÍ ÂŚÂĚŚĎÔĹËÉ libelf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libelf0-devel

%description devel
Development files for libelf.

%description devel -l pl
Pliki dla programistów tworzących programy używające libelf.

%description devel -l ru
üÔĎÔ ĐÁËĹÔ ÓĎÄĹŇÖÉÔ ĆÁĘĚŮ, ÎĹĎÂČĎÄÉÍŮĹ ÄĚŃ ŇÁÚŇÁÂĎÔËÉ ĐŇĎÇŇÁÍÍ Ó
ÉÓĐĎĚŘÚĎ×ÁÎÉĹÍ ÂÉÂĚÉĎÔĹËÉ libelf.

%description devel -l uk
ăĹĘ ĐÁËĹÔ ÍŚÓÔÉÔŘ ĆÁĘĚÉ, ÎĹĎÂČŚÄÎŚ ÄĚŃ ŇĎÚŇĎÂËÉ ĐŇĎÇŇÁÍ Ú
×ÉËĎŇÉÓÔÁÎÎŃÍ ÂŚÂĚŚĎÔĹËÉ libelf.

%package static
Summary:	Static libelf library
Summary(pl):	Statyczna biblioteka libelf
Summary(ru):	óÔÁÔÉŢĹÓËÉĹ ÂÉÂĚÉĎÔĹËÉ ÄĚŃ ŇÁÚŇÁÂĎÔËÉ Ó ÉÓĐĎĚŘÚĎ×ÁÎÉĹÍ libelf
Summary(uk):	óÔÁÔÉŢÎŚ ÂŚÂĚŚĎÔĹËÉ ÄĚŃ ŇĎÚŇĎÂËÉ Ú ×ÉËĎŇÉÓÔÁÎÎŃÍ libelf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libelf library.

%description static -l pl
Statyczna biblioteka libelf.

%description static -l ru
üÔĎÔ ĐÁËĹÔ ÓĎÄĹŇÖÉÔ ÓÔÁÔÉŢĹÓËÉĹ ÂÉÂĚÉĎÔĹËÉ ÄĚŃ ŇÁÚŇÁÂĎÔËÉ ĐŇĎÇŇÁÍÍ.

%description static -l uk
ăĹĘ ĐÁËĹÔ ÍŚÓÔÉÔŘ ÓÔÁÔÉŢÎŚ ÂŚÂŚĚŚĎÔĹËÉ ÄĚŃ ŇĎÚŇĎÂËÉ ĐŇĎÇŇÁÍ.

%prep
%setup -q
%patch0 -p1

%build
install -m755 /usr/share/automake/config.{sub,guess} .
%{__aclocal}
%{__autoconf}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	instroot=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libelf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libelf.so
%{_includedir}/libelf
%{_pkgconfigdir}/libelf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libelf.a
