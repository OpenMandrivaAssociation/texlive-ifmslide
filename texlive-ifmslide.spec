%global tl_name ifmslide
%global tl_revision 20727

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.47
Release:	%{tl_revision}.1
Summary:	Presentation slides for screen and printouts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifmslide
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is used to produce printed slides with LaTeX and online
presentations with pdfLaTeX. It is provided by the 'Institute of
Mechanics' (ifm) Univ. of Technology Darmstadt, Germany. It is based on
ideas of pdfslide, but completely rewritten for compatibility with
texpower and seminar. The manual describes all functions and provides a
sample.

