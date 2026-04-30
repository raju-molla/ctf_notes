#!/usr/bin/env python3
import sys
import cv2
from pyzbar.pyzbar import decode

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} image.jpg")
    sys.exit(1)

image_path = sys.argv[1]

img = cv2.imread(image_path)

if img is None:
    print("Error: Could not open image.")
    sys.exit(1)

results = decode(img)

if not results:
    print("No QR code found.")
    sys.exit(0)

for qr in results:
    print("Type:", qr.type)
    print("Data:", qr.data.decode("utf-8", errors="replace"))