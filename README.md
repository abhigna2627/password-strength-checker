# Password Strength Checker 🔐

A simple cybersecurity-focused Python project that checks password strength using common security rules and displays the result through a web interface.

This project was built to understand how backend security logic connects to a frontend using Flask.

---

## 🚀 Features

- Detects commonly used weak passwords
- Checks password length
- Validates use of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Classifies passwords as:
  - WEAK ❌
  - MODERATE ⚠️
  - STRONG ✅
- Dynamic UI feedback:
  - Container color changes based on password strength

---

## 🧠 Why this matters (Cybersecurity context)

Weak passwords are one of the most common causes of:
- Brute-force attacks
- Credential stuffing
- Account compromise

This project demonstrates how basic password policies and validation rules can be implemented in real code and exposed safely through a web interface.

---

## 🛠 Tech Stack

- Python
- Flask (backend)
- HTML + CSS (frontend)

---

## ⚙️ How it works

1. User enters a password in the browser
2. The form sends the data using a POST request
3. Flask receives the password
4. Python evaluates its strength using security rules
5. Result and strength level are sent back to the frontend
6. UI updates dynamically based on the result

---

## ▶️ How to run locally

1. Clone the repository
2. Install Flask:
   ```bash
   pip install flask


2. Run the application:

python app.py


3. Open your browser and visit:

http://127.0.0.1:5000/