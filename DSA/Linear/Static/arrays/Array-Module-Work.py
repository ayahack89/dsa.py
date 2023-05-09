# Module Work
from array import *

val = array("i", [1, 4, 5, -1, 7])
print(val)
print(f"REVERSE:- {val}")
"""Squre this function using inner for loop"""
val.reverse()
val = array("i", [9, 8, 5, 4, 7])
print(val)
nval = array(val.typecode, (a * a for a in val))
for e in nval:
    print(e)

print(type(val))
