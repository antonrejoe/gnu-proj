# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT telemetry_primaryheader_adder_1_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT telemetry_primaryheader_adder_1_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND telemetry_primaryheader_adder_1_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(telemetry_primaryheader_adder_1
   ../../..
   gr::telemetry_primaryheader_adder_1
   "${telemetry_primaryheader_adder_1_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET telemetry_primaryheader_adder_1_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:telemetry_primaryheader_adder_1_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/telemetry_primaryheader_adder_1/
)

install(TARGETS telemetry_primaryheader_adder_1_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/telemetry_primaryheader_adder_1 COMPONENT pythonapi)
