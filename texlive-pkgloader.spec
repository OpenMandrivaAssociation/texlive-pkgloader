# revision 34019
# category Package
# catalog-ctan /macros/latex/contrib/pkgloader
# catalog-date 2014-05-11 22:11:06 +0200
# catalog-license lppl1.3
# catalog-version 0.2.0
Name:		texlive-pkgloader
Version:	0.2.0
Release:	3
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
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-cls-pkg.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-dry.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-early.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-error.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-false.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-late.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-recommended.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-true.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader.sty
%doc %{_texmfdistdir}/doc/latex/pkgloader/README
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader-packagedoc.cls
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader.pdf
%doc %{_texmfdistdir}/doc/latex/pkgloader/pkgloader.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
