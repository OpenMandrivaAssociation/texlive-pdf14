Name:		texlive-pdf14
Version:	0.1
Release:	1
Summary:	Restore PDF 1.4 to a TeX live 2010 format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdf14
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf14.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Starting with TeX Live 2010, the various formats that directly
generate PDF will default to generating PDF 1.5. This is
generally a good thing, but it can lead to compatibility issues
with some older PDF viewers. This package changes the version
of PDF generated with formats (based on pdfTeX or LuaTeX in PDF
mode), back to 1.4 for documents that need to achieve maximal
compatibility with old viewers.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdf14/pdf14.sty
%doc %{_texmfdistdir}/doc/latex/pdf14/README
%doc %{_texmfdistdir}/doc/latex/pdf14/pdf14.pdf
%doc %{_texmfdistdir}/doc/latex/pdf14/test-pdf14.tex
#- source
%doc %{_texmfdistdir}/source/latex/pdf14/Makefile
%doc %{_texmfdistdir}/source/latex/pdf14/pdf14.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
