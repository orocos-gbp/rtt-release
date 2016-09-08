Name:           ros-jade-rtt
Version:        2.8.3
Release:        1%{?dist}
Summary:        ROS rtt package

Group:          Development/Libraries
License:        GPL v2 with linking exception
URL:            http://www.orocos.org/rtt
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       omniORB
Requires:       omniORB-devel
Requires:       omniORB-servers
Requires:       perl-XML-XPath
Requires:       pkgconfig
Requires:       ros-jade-catkin
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  perl-XML-XPath
BuildRequires:  pkgconfig
BuildRequires:  ros-jade-catkin

%description
Orocos/RTT component framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Sep 08 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.3-1
- Autogenerated by Bloom

* Thu Aug 11 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.3-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.1-0
- Autogenerated by Bloom

