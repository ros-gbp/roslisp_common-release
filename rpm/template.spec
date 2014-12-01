Name:           ros-indigo-cl-tf
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS cl_tf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/cl_tf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cl-transforms
Requires:       ros-indigo-roslisp
Requires:       ros-indigo-tf
Requires:       sbcl
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cl-transforms
BuildRequires:  ros-indigo-roslisp
BuildRequires:  ros-indigo-tf
BuildRequires:  sbcl

%description
Client implementation to use TF from Common Lisp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 01 2014 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.3-0
- Autogenerated by Bloom

