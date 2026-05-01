#!/usr/bin/env python3
import sys
import base64
import codecs
import urllib.parse
import html
import gzip
import zlib
import bz2
import lzma
import binascii
import string

try:
    import base58
except ImportError:
    base58 = None


def printable(data):
    if isinstance(data, bytes):
        try:
            data = data.decode("utf-8")
        except UnicodeDecodeError:
            return None

    data = data.strip()
    if not data:
        return None

    score = sum(c in string.printable for c in data) / len(data)
    if score < 0.85:
        return None

    return data


def show(name, func, value):
    try:
        result = func(value)
        result = printable(result)

        if result and result != value:
            print(f"\n[{name}]")
            print(result)
    except Exception:
        pass


def decode_binary_ascii(value):
    parts = value.replace("\n", " ").split()
    return bytes([int(x, 2) for x in parts])


def decode_decimal_ascii(value):
    parts = value.replace(",", " ").split()
    return bytes([int(x) for x in parts])


def decode_octal_ascii(value):
    parts = value.replace(",", " ").split()
    return bytes([int(x, 8) for x in parts])


def decode_hex_escaped(value):
    return codecs.decode(value, "unicode_escape")


def decode_zlib_hex(value):
    return zlib.decompress(bytes.fromhex(value))


def decode_gzip_hex(value):
    return gzip.decompress(bytes.fromhex(value))


def decode_bz2_hex(value):
    return bz2.decompress(bytes.fromhex(value))


def decode_lzma_hex(value):
    return lzma.decompress(bytes.fromhex(value))


def caesar(value, shift):
    result = ""

    for c in value:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c

    return result


def decode_big_integer(value):
    n = int(value)
    return n.to_bytes((n.bit_length() + 7) // 8, "big")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} '<encoded_value>'")
        sys.exit(1)

    value = " ".join(sys.argv[1:]).strip()

    print(f"[Input]")
    print(value)

    show("URL Decode", urllib.parse.unquote, value)
    show("HTML Entity Decode", html.unescape, value)
    show("Unicode Escape Decode", decode_hex_escaped, value)

    show("Hex", lambda x: bytes.fromhex(x), value)
    show("Base16", lambda x: base64.b16decode(x.upper()), value)
    show("Base32", lambda x: base64.b32decode(x.upper() + "=" * (-len(x) % 8)), value)
    show("Base64", lambda x: base64.b64decode(x + "=" * (-len(x) % 4)), value)
    show("Base64 URL Safe", lambda x: base64.urlsafe_b64decode(x + "=" * (-len(x) % 4)), value)
    show("Base85", base64.b85decode, value)
    show("Ascii85", base64.a85decode, value)

    if base58:
        show("Base58", base58.b58decode, value)
    else:
        print("\n[Base58 skipped]")
        print("Install: pip install base58")

    show("ROT13", lambda x: codecs.decode(x, "rot_13"), value)

    for i in range(1, 26):
        show(f"Caesar Shift {i}", lambda x, s=i: caesar(x, s), value)

    show("Binary ASCII", decode_binary_ascii, value)
    show("Decimal ASCII", decode_decimal_ascii, value)
    show("Octal ASCII", decode_octal_ascii, value)

    show("Zlib Hex", decode_zlib_hex, value)
    show("Gzip Hex", decode_gzip_hex, value)
    show("BZ2 Hex", decode_bz2_hex, value)
    show("LZMA Hex", decode_lzma_hex, value)
    show("Big Integer to Bytes", decode_big_integer, value)

if __name__ == "__main__":
    main()