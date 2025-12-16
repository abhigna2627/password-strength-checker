from flask import Flask, render_template, request
import re

app = Flask(__name__)

common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]

def check_password_strength(password):
    if password.lower() in common_passwords:
        return "VERY WEAK ❌","weak"

    score = 0
    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "WEAK ❌","weak"
    elif score <= 4:
        return "MODERATE ⚠️","moderate"
    else:
        return "STRONG ✅","strong"
    
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    level=""
    
    if request.method == "POST":
        password = request.form["password"]
        result, level = check_password_strength(password)
    return render_template("index.html", result=result, level=level)

if __name__ == "__main__":
    app.run(debug=True)
