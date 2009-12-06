%define module configfile
%define srcname ConfigFile

Name: haskell-%{module}
Version: 1.0.4
Release: %mkrel 2
Summary: Configuration file reading & writing
Group: Development/Other
License: LGPL
Url: http://software.complete.org/configfile
Source: http://software.complete.org/%{module}/static/download_area/%{version}/%{srcname}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros
BuildRequires: haskell(parsec)
BuildRequires: haskell(base)
BuildRequires: haskell(haskell98)
BuildRequires: haskell(mtl)
BuildRequires: haskell(MissingH) >= 0.18.0

%description
ConfigFile is a configuration file parser and writer library for Haskell.

The ConfigFile module works with configuration files in a standard format
that is easy for the user to edit, easy for the programmer to work with, yet
remains powerful and flexible. It is inspired by, and compatible with, Python's
ConfigParser module. It uses files that resemble Windows .INI-style files, but
with numerous improvements.

ConfigFile provides simple calls to both read and write config files. It's
possible to make a config file parsable by this module, the Unix shell, and
make.

%prep
%setup -q -n %{srcname}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%doc dist/doc/html
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot


