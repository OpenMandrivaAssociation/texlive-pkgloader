Name:		texlive-pkgloader
Version:	47486
Release:	1
Summary:	Managing the options and loading order of other packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pkgloader
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
