# NOTE: PLD uses elfutils currently
Summary:	ELF object file access library
Summary(de.UTF-8):	Objektdateizugriffs-Library ELF
Summary(pt_BR.UTF-8):	Biblioteca para acesso a arquivos objeto ELF
Summary(es.UTF-8):	Biblioteca para acceso a archivos objeto ELF
Summary(fr.UTF-8):	Bibliothèque de gestion de fichiers ELF
Summary(pl.UTF-8):	Biblioteka dostępu do plików ELF
Summary(pt_BR.UTF-8):	Biblioteca para acesso a arquivos objeto ELF
Summary(ru.UTF-8):	Библиотека доступа к объектным файлам в формате ELF
Summary(tr.UTF-8):	ELF ara kod erişim kitaplığı
Summary(uk.UTF-8):	Бібліотека доступу до об'єктних файлів формату ELF
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

%description -l de.UTF-8
Diese Library gibt Ihnen Zugang zum Inneren des ELF-Objekt-
Dateiformats. Sie können damit in den verschiedenen Teilen einer
ELF-Datei umherstochern, die Symbole überprüfen und ähnliches.

%description -l es.UTF-8
Esta biblioteca ofrece acceso a datos internos del formato de archivo
objeto ELF. Permite visualizar varias secciones diferentes de un
archivo ELF, observar los símbolos, etc.

%description -l fr.UTF-8
La bibliothèque libelf permet de manipuler des fichiers ELF (format de
programmes exécutables communs à plusieurs Unix dont Linux) et leurs
différentes sections.

%description -l pl.UTF-8
Biblioteka elf umożliwia dostęp do struktury wewnętrznej plików w
formacie ELF. Udostępnia ona funkcje do przeglądania poszczególnych
części ELF-a, a także sprawdzanie symboli itp.

%description -l pt_BR.UTF-8
Esta biblioteca fornece acesso a dados internos do formato de arquivo
objeto ELF. Ele permite visualizar várias seções diferentes de um
arquivo ELF, observar os símbolos, etc.

%description -l uk.UTF-8
Ця бібліотека надає доступ до внутрішньої структури об'єктних файлів
формату ELF. Вона дозволяє вивчати різні секції ELF-файлу, перевіряти
символи і т.п.

%description -l ru.UTF-8
Эта библиотека предоставляет доступ к внутренностям объектных файлов в
формате ELF. Она позволяет изучать различные секции ELF-файла,
проверять символы и т.д.

%description -l tr.UTF-8
Bu kitaplık, ELF ara kod dosyası içeriğine erişimi sağlar. ELF
dosyalarının çeşitli yerleri ile oynama, sembolleri kontrol etme gibi
olanaklar sunar.

%description -l uk.UTF-8
Ця бібліотека надає доступ до внутрішньої структури об'єктних файлів
формату ELF. Вона дозволяє вивчати різні секції ELF-файлу, перевіряти
символи і т.п.

%package devel
Summary:	Development files for libelf
Summary(pl.UTF-8):	Pliki dla programistów libelf
Summary(ru.UTF-8):	Файлы для разработки с использованием библиотеки libelf
Summary(uk.UTF-8):	Файли для розробки з використанням бібліотеки libelf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libelf0-devel

%description devel
Development files for libelf.

%description devel -l pl.UTF-8
Pliki dla programistów tworzących programy używające libelf.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ с
использованием библиотеки libelf.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм з
використанням бібліотеки libelf.

%package static
Summary:	Static libelf library
Summary(pl.UTF-8):	Statyczna biblioteka libelf
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием libelf
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням libelf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libelf library.

%description static -l pl.UTF-8
Statyczna biblioteka libelf.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ.

%description static -l uk.UTF-8
Цей пакет містить статичні бібіліотеки для розробки програм.

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
