import requests

url = "https://srcpjcc.clubautomation.com/calendar/classes-by-date"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://srcpjcc.clubautomation.com",
    "Referer": "https://srcpjcc.clubautomation.com/calendar/classes?tab=by-date",
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "Cookie": "PASTE_FULL_COOKIE_STRING_HERE",  # From your devtools
}

data = {
    "tab": "by-date",
    "isFrame": "0"
}

response = requests.post(url, headers=headers, data=data)

# If the response is JSON (try printing it)
try:
    print(response.json())
except Exception:
    print(response.text)  # fallback to raw text
