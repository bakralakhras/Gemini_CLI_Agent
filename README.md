# 🤖 GenAgent CLI — AI-Powered Command Line Assistant

![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/build-passing-brightgreen)
![Gemini-Enabled](https://img.shields.io/badge/LLM-Gemini_2.0-orange)

GenAgent CLI is a natural-language-driven assistant for your terminal. Powered by Google Gemini, it understands plain English and performs intelligent operations on your code — including reading, writing, listing files, fixing bugs, running code, and even pushing to GitHub.

---

## ✨ Features

- 🧠 Understands natural language instructions
- 🧮 Evaluates and fixes buggy code (like expression logic bugs)
- 📁 Reads, writes, and lists files with directory sandboxing
- 🔍 Finds the best file for evaluating expressions
- 🔧 Executes Python scripts securely and shows output
- 🌀 Autocommits and pushes changes to GitHub when told
- 🛡️ Prevents unauthorized file access (path traversal safe)

---

## 🧠 How It Works

You type a request like:

```
Fix the bug. 3 + 7 * 2 shouldn't be 20, it should be 17.
```

GenAgent will:

1. Search your project for files likely to contain the bug
2. Read and analyze them
3. Fix the logic (e.g., operator precedence)
4. Optionally commit and push the fix to GitHub when asked

---

## 🧪 Demo Flow (Narrated Script)

1. **Reproduce the Bug**

```bash
python3 calculator/main.py "3 + 7 * 2"
```

> Returns `20` — the bug is present.

2. **Launch GenAgent**

```bash
python3 main.py
```

3. **List Files**

```bash
You: list the names of the files located in directory pkg
```

> AI reads contents of `pkg` directory.

4. **Fix the Bug**

```bash
You: Fix the bug. 3 + 7 * 2 shouldn't be 20, it should be 17.
```

> AI finds the file, fixes the logic.

5. **Explain the Fix**

```bash
You: explain what file did you change and how did you fix it
```

> AI describes its changes.

6. **Push the Fix to GitHub**

```bash
You: push changes with message "fix: fixed expression bug"
```

> AI commits and pushes via Git.

7. **Verify the Fix**

```bash
python3 calculator/main.py "3 + 7 * 2"
```

> Output is now `17` — fix confirmed.

---

## 🔧 Tooling

| Tool Name             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `get_files_info`      | Lists files and directories                                                  |
| `get_file_content`    | Reads file content safely                                                    |
| `write_file`          | Creates or updates a file                                                    |
| `run_python_file`     | Executes a Python script and captures output                                |
| `find_matching_file`  | Finds files with logic to evaluate math expressions                         |
| `git_commit_and_push` | Commits and pushes staged changes to GitHub with a user-defined message     |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Google API key (Gemini)
- GitHub repo initialized
- Git authentication via SSH or PAT

### Install and Run

```bash
git clone https://github.com/yourname/genagent-cli.git
cd genagent-cli
pip install -r requirements.txt
echo "GEMINI_API_KEY=your-api-key-here" > .env
python3 main.py
```

---

## 📌 Example Use Cases

- "Read the contents of main.py"
- "Write to file notes.txt"
- "Fix the logic in calculator.py"
- "Find the file that evaluates expressions"
- "Push my changes with message: updated eval logic"

---

## 📄 License

MIT License

---

## 🎥 Video Showcase

> 📽️ Watch the full demo:
> 

https://github.com/user-attachments/assets/74010187-49f3-4395-92ca-70b3dc1c6e3b



---

## ✍️ Author

Created by [Baker Alakhras](https://github.com/bakeralakhras)  
_“Coding with words — GenAgent makes it real.”_
