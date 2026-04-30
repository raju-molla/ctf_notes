# 🧰 CTF Tools Notes (Simple Guide)

## 📌 1. decoder.py (Python Decoder Script)

### 🔹 What it does

This script tries different decoding methods automatically:

* Base64
* Base32
* Hex
* ROT13
* URL decode
* Binary / Decimal ASCII

---

### 🔹 Requirements

* Python 3 installed

Check:

```bash
python3 --version
```

---

### 🔹 How to run

```bash
python3 decoder.py "SGVsbG8="
```

OR with file:

```bash
python3 decoder.py "$(cat file.txt)"
```

---

### 🔹 Output

* Shows possible decoded values
* Example:

```
[Base64]
Hello
```

👉 Helps find hidden text quickly in CTF challenges

---

## 📌 2. exiftool (Image Metadata Tool)

### 🔹 What it does

Reads hidden metadata from images:

* Comments
* Author
* Hidden strings

---

### 🔹 Install

```bash
sudo apt install exiftool
```

---

### 🔹 How to use

```bash
exiftool image.jpg
```

---

### 🔹 Output

* Shows all metadata inside the image
* Sometimes contains flag like:

```
Comment: THM{example_flag}
```

---

## 📌 3. Steghide

### 🔹 What it does

Used to hide or extract secret files inside images (JPG, BMP)

---

### 🔹 Check if data exists

```bash
steghide info image.jpg
```

---

### 🔹 Extract data

```bash
steghide extract -sf image.jpg
```

👉 Will ask for password

---

### 🔹 Output

```
wrote extracted data to "secret.txt"
```

---

## 📌 4. zsteg

### 🔹 What it does

Finds hidden data using LSB (least significant bit)

👉 Mostly used for PNG but can try on JPG

---

### 🔹 Install

```bash
gem install zsteg
```

---

### 🔹 How to use

```bash
zsteg image.png
```

---

### 🔹 Output

* Shows hidden text or encoded data
* Example:

```
b1,r,lsb: "hidden_message"
```

---

## 📌 5. Stegseek

### 🔹 What it does

Cracks steghide password using wordlist

---

### 🔹 How to use

```bash
stegseek image.jpg /usr/share/wordlists/rockyou.txt
```

---

### 🔹 Output

```
Found passphrase: password123
Extracting data...
```

---

## 🧠 Simple CTF Workflow

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

## ⚠️ Important Tips

* Always start with `strings` and `exiftool`
* JPG file does NOT always mean steghide
* Try multiple tools, not just one

---

## ✅ Result

Using these tools, you can:

* Find hidden flags
* Extract secret files
* Decode encoded values
* Solve CTF challenges faster
