# revision 32864
# category Package
# catalog-ctan /macros/latex/contrib/pkgloader
# catalog-date 2014-02-03 01:30:56 +0100
# catalog-license lppl1.3
# catalog-version 0.1.0
Name:		texlive-pkgloader
Version:	0.1.0
Release:	1
Summary:	Managing the options and loading order of other packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pkgloader
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package seeks to address the frustration caused by package
conflicts. It is in an early stage of its development, and
should probably not be used as a matter of course; however the
author welcomes feedback via the home page link given in this
catalogue entry. Nevertheless, the author urges users to try
the package and to report issues (or whatever) via the
package's repository.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-dry.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-early.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-error.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-false.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-late.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-recommended.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-test-rules.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-true.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader.sty
%doc %{_texmfdistdir}/doc/latex/pkgloader/README
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader-packagedoc.cls
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader.pdf
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader.tex
%doc %{_texmfdistdir}/doc/latex/pkgloader/test1.sty
%doc %{_texmfdistdir}/doc/latex/pkgloader/test2.sty
%doc %{_texmfdistdir}/doc/latex/pkgloader/test3.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
