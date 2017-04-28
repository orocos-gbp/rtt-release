#
# ROS Release cmake configuration for Orocos RTT
#

# include defaults
include(orocos-rtt.default.cmake)

# enable CORBA
set(ENABLE_CORBA ON)
set(CORBA_IMPLEMENTATION OMNIORB)
