#If you have cracked some more part of it. Contribute at https://forum.unofficed.com.
#Feel Free to discuss at https://www.unofficed.com/chat/

import requests
import json

s =requests.Session()

def VerifyEmailStatus(s,username):
    data={
        "Email": str(username)
        }
    url="https://www.5paisa.com/Home/VerifyEmailStatus"
    r = s.post(url,data=data)
    return r

headers = {
    'authority': 'www.5paisa.com',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.5paisa.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.5paisa.com/',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
}

def Login(s,username,password,twofa):
    data={
    'login.UserName': username,
    'login.ClientCode': '',
    'login.Password': password,
    'login.DOB': twofa
    }

    r = s.post('https://www.5paisa.com/Home/Login', headers=headers, data=data)
    return r,s

def getHome(s):
    r = s.get('https://trade.5paisa.com/trade/home/', headers=headers)
    return r,s

def GetMarginData(s):
    r = s.post('https://trade.5paisa.com/Trade/Home/GetMarginData', headers=headers).json()
    return r
