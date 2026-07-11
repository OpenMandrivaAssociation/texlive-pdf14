%global tl_name pdf14
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Restore PDF 1.4 to a TeX Live 2010 format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdf14
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Starting with TeX Live 2010, the various formats, that directly generate
PDF, default to generating PDF 1.5. This is generally a good thing, but
it can lead to compatibility issues with some older PDF viewers. This
package changes the version of PDF generated with formats (based on
pdfTeX or LuaTeX in PDF mode), back to 1.4 for documents that need to
achieve maximal compatibility with old viewers.

