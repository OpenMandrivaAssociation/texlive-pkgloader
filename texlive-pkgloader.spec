%global tl_name pkgloader
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Manage the options and loading order of other packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pkgloader
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pkgloader.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package seeks to address the frustration caused by package
conflicts. It is in an early stage of its development, and should
probably not be used as a matter of course; however the author welcomes
feedback via the home page link given in this catalogue entry.
Nevertheless, the author urges users to try the package and to report
issues (or whatever) via the package's repository. To use pkgloader you
need, apart from packages installed by default, the lt3graph package.

