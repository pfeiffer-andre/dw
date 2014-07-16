%define prefix /opt
%define libsdir /usr/lib

Summary: DBDesigner4 - a visual database designer for MySQL databases
Name: DBDesigner4
Version: 0.5.4
Release: 0
Copyright: GPL
Group: Applications/Databases
BuildArch: i586
BuildRoot: /tmp/%{name}-%{version}
Source: %{name}.%{version}.tar.gz
URL: http://www.fabforce.com/dbdesigner4
Vendor: fabFORCE.net
Packager: mike@fabforce.net
Prefix: %{prefix}

%description
This package contains DBDesigner4, a visual database designer for MySQL databases
running on Linux and Windows.

%prep -n %{name}

%setup -n %{name}

%build -n %{name}
# not needed since the BUILD directory already contains a running image
exit 0

%install
# copy libs
mkdir -p $RPM_BUILD_ROOT%{libsdir}/%{name}
cp Linuxlib/* $RPM_BUILD_ROOT%{libsdir}/%{name}
rm $RPM_BUILD_ROOT%{libsdir}/%{name}/deleteSymbolicLinks.sh

# copy rest to opt
mkdir -p $RPM_BUILD_ROOT%{prefix}/%{name}
cp -r Doc $RPM_BUILD_ROOT%{prefix}/%{name}
cp -r Data $RPM_BUILD_ROOT%{prefix}/%{name}
cp -r Examples $RPM_BUILD_ROOT%{prefix}/%{name}
cp -r Gfx $RPM_BUILD_ROOT%{prefix}/%{name}
cp DBDesigner4 DBDplugin_DataImporter DBDplugin_HTMLReport DBDplugin_SimpleWebFront $RPM_BUILD_ROOT%{prefix}/%{name} 

mkdir -p $RPM_BUILD_ROOT/usr/bin
cp startdbd $RPM_BUILD_ROOT/usr/bin/

# check if symbolic links for libraries already exist
if [ -f "$RPM_BUILD_ROOT%{libsdir}/%{name}/bplrtl.so.6.9" ]; then
  echo Symbolic links exist and are not created
else
  echo Create symbolic links ...
  ln -s %{libsdir}/%{name}/bplrtl.so.6.9.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/bplrtl.so.6.9
  ln -s %{libsdir}/%{name}/dbxres.en.1.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/dbxres.en.1
  ln -s %{libsdir}/%{name}/libmidas.so.1.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/libmidas.so.1
  ln -s %{libsdir}/%{name}/libmysqlclient.so.10.0.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/libmysqlclient.so
  ln -s %{libsdir}/%{name}/libqt.so.2.3.2 $RPM_BUILD_ROOT%{libsdir}/%{name}/libqt.so.2
  ln -s %{libsdir}/%{name}/libqtintf-6.9.0-qt2.3.so $RPM_BUILD_ROOT%{libsdir}/%{name}/libqtintf-6.9-qt2.3.so
  ln -s %{libsdir}/%{name}/libsqlmy23.so.1.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/libsqlmy23.so
  ln -s %{libsdir}/%{name}/libsqlmy23.so $RPM_BUILD_ROOT%{libsdir}/%{name}/libsqlmy.so
  ln -s %{libsdir}/%{name}/libsqlora.so.1.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/libsqlora.so
  ln -s %{libsdir}/%{name}/libDbxSQLite.so.2.8.5 $RPM_BUILD_ROOT%{libsdir}/%{name}/libDbxSQLite.so
  ln -s %{libsdir}/%{name}/liblcms.so.1.0.9 $RPM_BUILD_ROOT%{libsdir}/%{name}/liblcms.so
  ln -s %{libsdir}/%{name}/libpng.so.2.1.0.12 $RPM_BUILD_ROOT%{libsdir}/%{name}/libpng.so.2
  ln -s %{libsdir}/%{name}/libstdc++.so.5.0.0 $RPM_BUILD_ROOT%{libsdir}/%{name}/libstdc++.so.5
fi

# Desktop entry
mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/applnk/Programming
sed -e 's/\(Exec=\).*/\1\/usr\/bin\/startdbd/' \
    -e 's/\(Icon=\).*/\1\/opt\/DBDesigner4\/Gfx\/Icon48.xpm/' \
    startdbd.desktop > $RPM_BUILD_ROOT/opt/kde3/share/applnk/Programming/DBDesigner4.desktop

exit 0

%clean
# Clean up the BUILD directory
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{libsdir}/%{name}
%{prefix}/%{name}
/usr/bin/startdbd
/opt/kde3/share/applnk/Programming
