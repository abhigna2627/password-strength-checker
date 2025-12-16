# Password Strength Checker 🔐

A simple Python-based cybersecurity tool that checks the strength of a password using common security rules.

This project is built to understand how weak passwords contribute to attacks like brute-force and credential stuffing, and how basic validation can reduce risk.

## Features
- Checks minimum length
- Detects uppercase, lowercase, numbers, and special characters
- Flags commonly used weak passwords
- Classifies passwords as WEAK, MODERATE, or STRONG

## Why this matters
Weak passwords are one of the most common causes of account compromise.  
This tool demonstrates how basic security principles can be translated into real code.

## How it works
The script assigns a score based on password characteristics and compares it against known weak patterns.

## How to run
1. Make sure Python is installed
2. Clone this repository
3. Run the script:

```bash
python password_checker.py
