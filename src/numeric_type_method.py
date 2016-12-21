#!/usr/bin/env python

import sys

def IsVersion2_x():
    return sys.version_info.major == 2;

def IsVersion3_x():
    return sys.version_info.major == 3;

# Integer Type Method:

v0 = 2
v1 = -2

# int.bit_length()
# Return the number of bit necessary to represent an integer in binary,
# Excluding the sign and leading zeros.
print(v0.bit_length())
print(v1.bit_length())

# int.to_bytes(length, byteorder = "little" | "big", signed = True | False)
# Return an array of bytes representing an integer.
if IsVersion3_x():
    print(v0.to_bytes(4, "big", signed = False))
    print(v0.to_bytes(4, "little", signed = False))
    print(v1.to_bytes(4, "big", signed = True))
    print(v1.to_bytes(4, "little", signed = True))

# int.from_bytes(bytes, byteorder = "little" | "big", signed = True | False)
# Return an integer represented by an array of bytes.
if IsVersion3_x():
    v2 = int.from_bytes(b'\x0f\x00', "little", signed = False)
    print('v2 = {0}'.format(v2))

# Float Type Method:
v0 = -2.0
v1 = 3.2

# float.as_integer_ratio()
# Return a pair of integers whose ratio is exactly equal to the original
# float and with a positive denominator raises OverflowError on infinities
# and ValueError on NaNs.
def AsIntegerRatio(v):
    dividend, divisor = v.as_integer_ratio()
    print('{0} integer ratio: {1} / {2}'.format(v, dividend, divisor))

AsIntegerRatio(v0)
AsIntegerRatio(v1)

# float.is_integer()
# Return True if the float instance is finite with integral value
# and False otherwise.
def IsInteger(v):
    if (v.is_integer()):
        print('{} is an finite with integral value'.format(v))
    else:
        print('{} is not an finite with integral value'.format(v))

IsInteger(v0)
IsInteger(v1)

print('{0} hex: {1}'.format(v0, v0.hex()))
print('{0} hex: {1}'.format(v1, v1.hex()))
print('-0x1.d3p+1 = {}'.format(float.fromhex('0x1.d3p+1')))

