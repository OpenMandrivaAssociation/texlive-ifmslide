# revision 20727
# category Package
# catalog-ctan /macros/latex/contrib/ifmslide
# catalog-date 2010-12-14 00:15:57 +0100
# catalog-license lppl1.2
# catalog-version 0.47
Name:		texlive-ifmslide
Version:	0.47
Release:	2
Summary:	Presentation slides for screen and printouts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifmslide
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is used to produce printed slides with latex and
online presentations with pdflatex. It is provided by the
'Institute of Mechanics' (ifm) Univ. of Technology Darmstadt,
Germany. It is based on ideas of pdfslide, but completely
rewritten for compatibility with texpower and seminar. The
manual describes all functions and provides a sample.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifmslide/aqua_ravines.eps
%{_texmfdistdir}/tex/latex/ifmslide/aqua_ravines.jpg
%{_texmfdistdir}/tex/latex/ifmslide/button1c.eps
%{_texmfdistdir}/tex/latex/ifmslide/button1c.pdf
%{_texmfdistdir}/tex/latex/ifmslide/button1e.eps
%{_texmfdistdir}/tex/latex/ifmslide/button1e.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonec.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonec.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonee.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonee.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttongc.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttongc.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonge.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonge.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogoc.eps
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogoc.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogog.eps
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogog.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmslide.cfg
%{_texmfdistdir}/tex/latex/ifmslide/ifmslide.sty
%{_texmfdistdir}/tex/latex/ifmslide/liquid_helium.eps
%{_texmfdistdir}/tex/latex/ifmslide/liquid_helium.jpg
%doc %{_texmfdistdir}/doc/latex/ifmslide/README
%doc %{_texmfdistdir}/doc/latex/ifmslide/genbutton
%doc %{_texmfdistdir}/doc/latex/ifmslide/ifmman.pdf
%doc %{_texmfdistdir}/doc/latex/ifmslide/ifmman.tex
#- source
%doc %{_texmfdistdir}/source/latex/ifmslide/genbutton

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
