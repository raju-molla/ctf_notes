# 🛡️ My CTF Notes

This is my personal CTF learning notes.
Click sections to expand 👇

---

<details>
<summary>🔐 Hashing & Decoder</summary>

## 📌 Hashing

### 🔹 What is Hashing

* One-way function (cannot reverse directly)
* Common types:

  * MD5
  * SHA1
  * SHA256

---

### 🔹 Usage

```bash
md5sum file.txt
sha1sum file.txt
sha256sum file.txt
```

---

### 🔹 Important

* Hashes cannot be decoded
* Only possible by:

  * Brute force
  * Wordlist attack

---

## 📌 decoder.py

### 🔹 What it does

* Auto-decodes:

  * Base64
  * Hex
  * ROT13
  * URL
  * Binary / Decimal

---

### 🔹 Run

```bash
python3 decoder.py "SGVsbG8="
```

OR:

```bash
python3 decoder.py "$(cat file.txt)"
```

---

### 🔹 Output

```bash
[Base64]
Hello
```

---

### 🔹 Use case

* Find hidden encoded strings in CTF

</details>

---

<details>
<summary>🖼️ Image Extraction & Steganography</summary>

## 📌 Metadata (EXIF)

### 🔹 Tool: exiftool

### 🔹 Install

```bash
sudo apt install exiftool
```

---

### 🔹 Usage

```bash
exiftool image.jpg
```

---

### 🔹 What to look for

* Comments
* Hidden text
* Strange values

---

## 📌 Steghide

### 🔹 Check hidden data

```bash
steghide info image.jpg
```

---

### 🔹 Extract

```bash
steghide extract -sf image.jpg
```

---

## 📌 Stegseek

### 🔹 Crack password

```bash
stegseek image.jpg /usr/share/wordlists/rockyou.txt
```

---

## 📌 zsteg

### 🔹 Install

```bash
gem install zsteg
```

---

### 🔹 Usage

```bash
zsteg image.png
```

---

## 📌 Basic Commands

```bash
file image.jpg
strings image.jpg | less
exiftool image.jpg
binwalk -e image.jpg
steghide info image.jpg
stegseek image.jpg rockyou.txt
zsteg image.png
```

---

## ⚠️ Tips

* Start with `strings`
* Check metadata first
* JPG ≠ always steghide
* Use multiple tools

---

## 🎯 Goal

* Extract hidden flags from images
* Understand steganography techniques

</details>

<details>
<summary>📷 QR Code Decoder</summary>

## 📌 Decode QR from Image

### 🔹 Tool: zbarimg

### 🔹 Install

```bash
sudo apt install zbar-tools
```

---

### 🔹 Usage

```bash
zbarimg image.jpg
```

---

### 🔹 Output Example

```bash
QR-Code:THM{example_flag}
```

👉 Fastest way to decode QR in CTF

---

## 🐍 Python QR Decoder

### 🔹 Requirements

```bash
sudo apt install libzbar0 python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install opencv-python pyzbar pillow
```

---
### 🔹 Run

```bash
python3 qr_decoder.py image.jpg
```

---

### 🔹 Output

```bash
Type: QRCODE
Data: THM{example_flag}
```

---

## 🧠 Tips

* Try `zbarimg` first (faster)
* If QR not detected:

  * crop image
  * increase contrast
  * rotate image
* Use `binwalk -e image.jpg` if QR is hidden inside

</details>
