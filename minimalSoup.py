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
soup = BeautifulSoup(response.text, "lxml")
block_rows = soup.find_all("div", class_ = "block row_1")
for block_row in block_rows:
    location_class_time = block_row.div.h3.a.text
    #department = block_row.div.
    if "SRC" not in location_class_time:
        location = location_class_time.split('|')[1].strip()
        print(location)
"""# Extract the TIME
    time_span = block_row.find("span", class_="time")
    time = time_span.text.strip() if time_span else "N/A"
    #just for testing purposes check locations plus instructor according to this format!
"""
