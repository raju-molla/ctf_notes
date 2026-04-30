#!/usr/bin/env python3
import sys

def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} <hex1> <hex2>")
    sys.exit(1)

# Input hex strings
s1 = bytes.fromhex(sys.argv[1])
s2 = bytes.fromhex(sys.argv[2])

# XOR
result = xor_bytes(s1, s2)

# Output
try:
    print(result.decode())
except:
    print(result)