# 🧠 Simple Word Based Tokenizer

A minimalistic Python script that reads a text file, builds a vocabulary from it, and tokenizes user input text into integer sequences. It also supports decoding those sequences back into human-readable text.

---

## 📌 Features

- 📖 Reads and preprocesses text from a user-specified file (e.g., `the-verdict.txt`)
- ✂️ Tokenizes text using regular expressions (words + punctuation)
- 🔡 Creates a vocabulary from unique tokens in the file
- 🔁 Encodes text to integer IDs and decodes back to readable text
- ❓ Handles unknown tokens using `<|unk|>`
- 📍 Uses special tokens like `<|endoftext|>` to separate segments

---

## 🛠️ How It Works

1. **Preprocessing**: Text is split using punctuation and spaces via regex.
2. **Vocabulary Generation**: A sorted set of all unique tokens is mapped to integers.
3. **Encoding**: User inputs are tokenized and converted to integer IDs.
4. **Decoding**: ID sequences are translated back into readable text with proper punctuation formatting.

---

## 🚀 Usage

### 📂 Step 1: Prepare Your Text File
Place your input file (e.g., `the-verdict.txt`) in the same directory or provide the full path.

### ▶️ Step 2: Run the Script

```bash
python tokenizer.py
