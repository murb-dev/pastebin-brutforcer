import string , random , requests

letters = string.ascii_letters
URL = "https://pastebin.com"

while True:
     fullString = ""
     string = random.choices(letters , k=8)
     for letter in string:
             fullString = fullString + letter
     newURL = f"{URL}/{fullString}"
     try:
        code = requests.get(newURL).status_code
     except ConnectionError as e:
        requests.post("https://ntfy.sh/Notif-minetrap" , data="program crashed! check logs")
        print(e)
        exit()
     if code == 200:
            requests.post("https://ntfy.sh/Notif-minetrap" , data=f"found a link {newURL}")
     print(f"{newURL} : {code}")