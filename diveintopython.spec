Summary:	A Python book
Summary(pl):	Ksi±¿ka o Pythonie
Name:		diveintopython
Version:	5.4
Release:	1
License:	FDL
Group:		Documentation
Source0:	http://www.diveintopython.org/download/%{name}-html-%{version}.zip
# Source0-md5:	09247597b21c6253b810f081053e56b5
URL:		http://www.diveintopython.org/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__python_provides	%{nil}
%define		__python_requires	%{nil}

%description
Dive Into Python is a Python book for experienced programmers.

%description -l pl
Dive Into Python (Zag³êbiaj±c siê w Pythona) jest ksi±¿k± o Pythonie
dla do¶wiadczonych programistów.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -a py/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html
%{_examplesdir}/%{name}-%{version}
