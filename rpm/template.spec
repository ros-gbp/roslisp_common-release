Name:           ros-melodic-cl-transforms
Version:        0.2.11
Release:        1%{?dist}
Summary:        ROS cl_transforms package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/cl_transforms
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cl-utils
Requires:       sbcl
BuildRequires:  ros-melodic-catkin

%description
Homogeneous transform library for Common Lisp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu May 16 2019 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.2.11-1
- Autogenerated by Bloom

* Tue Oct 16 2018 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.2.10-0
- Autogenerated by Bloom

