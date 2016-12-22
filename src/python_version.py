#!/usr/bin/env python

import sys

def IsVersion2x():
    return sys.version_info.major == 2;

def IsVersion3x():
    return sys.version_info.major == 3;
