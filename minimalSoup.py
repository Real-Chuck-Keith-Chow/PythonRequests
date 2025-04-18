import requests
from bs4 import BeautifulSoup

url = "https://srcpjcc.clubautomation.com/calendar/classes-by-date"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://srcpjcc.clubautomation.com",
    "Referer": "https://srcpjcc.clubautomation.com/calendar/classes?tab=by-date",
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "Cookie": "PASTE-YOUR-COOKIE-HERE"
}

data = {
    "tab": "by-date",
    "isFrame": "0"
}

response = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(response.text, "html.parser")



# Example: find all schedule blocks
for event in soup.find_all("div", class_="calendar-class"):
    print(event.text.strip())
