%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-mouse-teleop
Version:        1.5.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mouse_teleop package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-tkinter
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-rclpy
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-ament-xmllint
%endif

%description
A mouse teleop tool for holonomic mobile robots.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Sep 02 2024 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.5.1-1
- Autogenerated by Bloom

* Wed Nov 01 2023 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.5.0-1
- Autogenerated by Bloom

* Wed Nov 01 2023 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.3.0-3
- Autogenerated by Bloom

* Tue Mar 28 2023 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.3.0-2
- Autogenerated by Bloom

* Wed Nov 23 2022 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.3.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.2.1-3
- Autogenerated by Bloom

* Tue Feb 08 2022 Enrique Fernandez <enrique.fernandez.perdomo@gmail.com> - 1.2.1-2
- Autogenerated by Bloom

