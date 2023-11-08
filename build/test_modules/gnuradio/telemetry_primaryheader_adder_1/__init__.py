#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio TELEMETRY_PRIMARYHEADER_ADDER_1 module. Place your Python package
description here (python/__init__.py).
'''
import os

# import pybind11 generated symbols into the telemetry_primaryheader_adder_1 namespace
try:
    # this might fail if the module is python-only
    from .telemetry_primaryheader_adder_1_python import *
    from .tele import * 
except ModuleNotFoundError:
    pass

# import any pure python here
from .tph import tph
#
