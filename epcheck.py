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
    "Cookie": "cf_clearance=965G96X6GfFetxBPiVQVolWLfGw5fLrUAWT_XJy8ExE-1744997826-1.2.1.1-pSXrFlkMsnprTWt917NmLlrQ1kWgPKnk6fEwi3dcNYH7xhbGgOuxW2ZNuu7GYBoaTxhki_sFHB2809gyPhZwcluzNvq35YhhbHsTNfh.rTHBmOdRe7c6lS4FphZGJk1zPx3Ub21HOt8xFlfB6gG7BHLga5D.Q7GrKAxSdqckrlpmVvUULXv9SkXJNbk1Jq7fpN.ARC_pDhuAlc7J6InAB8ZF4eHU_YB5jSjTZn35XEGu9XEMtRQpYlkyINgovtVm4QZn7Ji0DBrbGirbXpgZLrMScBoe.0huQxuwEAUoLCoT8IbGhRPVpjxStE9DYQc_HhYyx0rW6CID049bDQ8VmEvk.IA9HjGEqDGdRVIYVBQ; _ga=GA1.1.722034584.1744983240; _ga_D0BQXRE67D=GS1.1.1744997825.3.1.1744997826.0.0.0; _gat_gtag_UA_109814872_1=1; _gid=GA1.2.1294036962.1744983240; __cf_bm=3anHSifKg6gtD90mSBgeagZlRoYspN1IeOs1731o4XQ-1744997825-1.0.1.1-QOo_8Ohh_GxY5RejoPyoJw8APRtohuXeDhMgSyktHuhXTBGpoCSLzQkgAMTGHz_kIlN0ciS9sFQ38qoXjDjrExhy5TvDRuFDD7._O3pcxjw; PHPSESSID=rgkrl0hik615ne2ngnec30udg2; cf_clearance=sZY0LWAskHQ8FvQLJxlFO1KlEZbh8Q94vEJ2WRxoI_U-1739647395-1.2.1.1-A78tXzoqCt6V.RwzpRNlpwm2DHNzvVeGzOM2GEVvb.Mj4ZY7xgf1dtu0npUFjpsqPP0WvKDgibrK3YTKbEiARHIzW2jIjeimr4VxxwHvUb8CBTSp4iQRo6dd_tCQ3nogMJ1Uwmz7JOOt2zi2BcSvY_h0zBKF0R1oAiHBbI_nqmj6lod_UwwbQ8IlEpazfscddWPSgjCFb9zVXAx1R3MQxyi1KIVhdQitTOxK8uaIjAFBTXwULbIFpoPGsK_.ep4DO.5Q0hIE1DGuye_Y0NDCDlzfu.GTTmZ37fiojRMdiCA",  # From your devtools
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
    print(response.text[:1000])  # fallback to raw text
