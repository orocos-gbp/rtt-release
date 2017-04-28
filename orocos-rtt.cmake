#
# ROS Release cmake configuration for Orocos RTT
#

# include defaults
include(orocos-rtt.default.cmake)

# enable CORBA
set(ENABLE_CORBA ON CACHE BOOL "")
set(CORBA_IMPLEMENTATION OMNIORB CACHE STRING "")
