#!/usr/bin/env python3

def find_key(cipher_prefix, plain_prefix):
    key = ""

    for c, p in zip(cipher_prefix, plain_prefix):
        if c.isalpha() and p.isalpha():
            c_val = ord(c.upper()) - ord("A")
            p_val = ord(p.upper()) - ord("A")
            k = (c_val - p_val) % 26
            key += chr(k + ord("A"))

    return key


def vigenere_decrypt(ciphertext, key):
    result = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord("A")
            k = ord(key[key_index % len(key)]) - ord("A")
            p = (c - k) % 26
            result += chr(p + ord("A"))
            key_index += 1
        else:
            result += char

    return result


ciphertext = input("Enter full ciphertext: ")
known_plain = input("Enter known plaintext prefix: ")

cipher_prefix = ""
for char in ciphertext:
    if char.isalpha():
        cipher_prefix += char
    if len(cipher_prefix) == len(known_plain):
        break

key = find_key(cipher_prefix, known_plain)
plaintext = vigenere_decrypt(ciphertext, key)

print("\nFound key:")
print(key)

print("\nDecrypted text:")
print(plaintext)