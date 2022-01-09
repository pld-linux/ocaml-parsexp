#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	S-expression parsing library
Summary(pl.UTF-8):	Biblioteka analizująca S-wyrażenia
Name:		ocaml-parsexp
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/parsexp/tags
Source0:	https://github.com/janestreet/parsexp/archive/v%{version}/parsexp-%{version}.tar.gz
# Source0-md5:	e6659d53f4d94de8979e05d17222b753
URL:		https://github.com/janestreet/parsexp
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-sexplib0-devel >= 0.14
BuildRequires:	ocaml-sexplib0-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
This library provides generic parsers for parsing S-expressions from
strings or other medium.

This package contains files needed to run bytecode executables using
parsexp library.

%description -l pl.UTF-8
Ta biblioteka zapewnia ogólne parsery do analizy S-wyrażeń z łańcuchów
lub innego nośnika.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki parsexp.

%package devel
Summary:	S-expression parsing library - development part
Summary(pl.UTF-8):	Biblioteka analizująca S-wyrażenia - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-sexplib0-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
parsexp library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki parsexp.

%prep
%setup -q -n parsexp-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/parsexp/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/parsexp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.org
%dir %{_libdir}/ocaml/parsexp
%{_libdir}/ocaml/parsexp/META
%{_libdir}/ocaml/parsexp/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/parsexp/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/parsexp/*.cmi
%{_libdir}/ocaml/parsexp/*.cmt
%{_libdir}/ocaml/parsexp/*.cmti
%{_libdir}/ocaml/parsexp/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/parsexp/parsexp.a
%{_libdir}/ocaml/parsexp/*.cmx
%{_libdir}/ocaml/parsexp/*.cmxa
%endif
%{_libdir}/ocaml/parsexp/dune-package
%{_libdir}/ocaml/parsexp/opam
