#!/usr/bin/env python3
import base64
import binascii
import codecs
import urllib.parse
import zlib
import gzip
import sys

def printable(data):
    if isinstance(data, bytes):
        try:
            data = data.decode("utf-8", errors="replace")
        except:
            data = str(data)
    return data.strip()

def try_decode(name, func, value):
    try:
        result = func(value)
        result = printable(result)
        if result and result != value:
            print(f"\n[{name}]")
            print(result)
    except Exception:
        pass

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} '<encoded_value>'")
        sys.exit(1)

    value = sys.argv[1].strip()
    raw = value.encode()

    print(f"[Input]\n{value}")

    try_decode("URL Decode", urllib.parse.unquote, value)
    try_decode("ROT13", lambda x: codecs.decode(x, "rot_13"), value)

    try_decode("Hex", lambda x: bytes.fromhex(x), value)
    try_decode("Base64", lambda x: base64.b64decode(x + "=" * (-len(x) % 4)), value)
    try_decode("Base32", lambda x: base64.b32decode(x + "=" * (-len(x) % 8)), value.upper())
    try_decode("Base85", lambda x: base64.b85decode(x), value)
    try_decode("Ascii85", lambda x: base64.a85decode(x), value)

    try_decode("Binary ASCII", lambda x: bytes([int(b, 2) for b in x.split()]), value)
    try_decode("Decimal ASCII", lambda x: bytes([int(n) for n in x.split()]), value)

    try_decode("Zlib", lambda x: zlib.decompress(bytes.fromhex(x)), value)
    try_decode("Gzip", lambda x: gzip.decompress(bytes.fromhex(x)), value)

if __name__ == "__main__":
    main()