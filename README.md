# 🛡️ My CTF Toolkit & Notes

This document contains my personal notes and tools for solving CTF challenges.
Click each section to expand 👇

---

<details>
<summary>🧰 decoder.py (Auto Decoder Script)</summary>

### 🔹 What it does

* Automatically tries:

  * Base64, Base32
  * Hex
  * ROT13
  * URL decode
  * Binary / Decimal ASCII

---

### 🔹 Requirements

```bash
python3 --version
```

---

### 🔹 How to run

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

👉 Helps quickly find hidden decoded values

</details>

---

<details>
<summary>🖼️ exiftool (Metadata Analysis)</summary>

### 🔹 What it does

* Extracts hidden metadata from images
* Useful for finding:

  * Comments
  * Hidden flags
  * Author info

---

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

### 🔹 Output Example

```bash
Comment: THM{flag_here}
```

</details>

---

<details>
<summary>🔐 Steghide</summary>

### 🔹 Tool: Steghide

### 🔹 What it does

* Hides or extracts data inside images (JPG, BMP)

---

### 🔹 Check for hidden data

```bash
steghide info image.jpg
```

---

### 🔹 Extract

```bash
steghide extract -sf image.jpg
```

👉 Requires password

---

### 🔹 Output

```bash
wrote extracted data to "secret.txt"
```

</details>

---

<details>
<summary>🧪 zsteg (LSB Steganography)</summary>

### 🔹 Tool: zsteg

### 🔹 What it does

* Finds hidden data in pixel bits (LSB)

---

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

### 🔹 Output Example

```bash
b1,r,lsb: "hidden_message"
```

</details>

---

<details>
<summary>🚀 Stegseek (Password Cracker)</summary>

### 🔹 Tool: Stegseek

### 🔹 What it does

* Brute-force steghide passwords using wordlists

---

### 🔹 Usage

```bash
stegseek image.jpg /usr/share/wordlists/rockyou.txt
```

---

### 🔹 Output

```bash
Found passphrase: password123
Extracting data...
```

</details>

---

<details>
<summary>🧠 My CTF Workflow</summary>

### 🔹 Steps

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

### 🔹 Tips

* Always check `strings` first
* JPG ≠ steghide always
* Use multiple tools
* Think logically, not blindly

</details>

---

## 🎯 Goal

* Build strong CTF skills
* Solve challenges faster
* Keep all knowledge in one place

---
