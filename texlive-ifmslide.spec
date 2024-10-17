Name:		texlive-ifmslide
Version:	20727
Release:	2
Summary:	Presentation slides for screen and printouts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifmslide
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmslide.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/ifmslide
%doc %{_texmfdistdir}/doc/latex/ifmslide

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
