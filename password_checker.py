import re
common_passwords=["123456","password","123456789","12345","12345678","qwerty",
                  "abc123","football","monkey","letmein","111111","1234","1234567",
                  "dragon","baseball","sunshine","iloveyou","trustno1","princess","adobe123","123123"]
def check_password_strength(password):
#this rule checks password strength using basic common rules    
#it helps users avoid weak passwords, common to bruteforce attacks, and credential stuffing attacks
    if password.lower() in common_passwords:
        return "Very weak password ❌❌❌: Commonly used password"
    score=0
    if len(password) >=8:
        score+=1
    if re.search(r'[A-Z]',password):
        score+=1
    if re.search(r'[a-z]',password):
        score+=1
    if re.search(r'[0-9]',password):
        score+=1
    if re.search(r'[@#$%^&+=]',password):
        score+=1

    if score <=2:
        return "WEAK ❌"
    elif score ==3 or score ==4:
        return "MODERATE ⚠️"
    else:
        return "STRONG✅"
    
password=input("Enter your password:")
result=check_password_strength(password)
print(result)