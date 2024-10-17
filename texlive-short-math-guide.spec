Name:		texlive-short-math-guide
Version:	46126
Release:	2
Summary:	Guide to using amsmath and related packages to typeset mathematical notation with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/short-math-guide
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/short-math-guide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/short-math-guide.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Short Math Guide is intended to be a concise introduction
to the use of the facilities provided by amsmath and various
other LaTeX packages for typesetting mathematical notation.
Originally created by Michael Downes of the American
Mathematical Society based only on amsmath, it has been brought
up to date with references to related packages and other useful
information.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/short-math-guide

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
