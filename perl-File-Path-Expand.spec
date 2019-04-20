#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Path-Expand
Version  : 1.02
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Path-Expand-1.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Path-Expand-1.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-path-expand-perl/libfile-path-expand-perl_1.02-3.debian.tar.xz
Summary  : Perl/CPAN Module File::Path::Expand
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Path-Expand-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-File-Path-Expand package.
Group: Development
Provides: perl-File-Path-Expand-devel = %{version}-%{release}
Requires: perl-File-Path-Expand = %{version}-%{release}

%description dev
dev components for the perl-File-Path-Expand package.


%package license
Summary: license components for the perl-File-Path-Expand package.
Group: Default

%description license
license components for the perl-File-Path-Expand package.


%prep
%setup -q -n File-Path-Expand-1.02
cd ..
%setup -q -T -D -n File-Path-Expand-1.02 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Path-Expand-1.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Path-Expand
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Path-Expand/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/File/Path/Expand.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Path::Expand.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Path-Expand/deblicense_copyright
