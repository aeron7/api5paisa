#If you have cracked some more part of it. Contribute at https://forum.unofficed.com.
#Feel Free to discuss at https://www.unofficed.com/chat/

import requests
import json


class Api5Paisa:
    def __init__(self):
        self.scrip_map = {}
        self.session = requests.Session()
        self._header_dict ={
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
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8'
        }

    def login(self, username=None, password=None, twofa=None):
        if (twofa is None):
            username, password, twofa = self._read_config()
        login_request = {
            'login.UserName': username,
            'login.ClientCode': '',
            'login.Password': password,
            'login.DOB': twofa
        }
        self.session.get("https://www.5paisa.com/")
        self.post('/Home/VerifyEmailStatus', {"Email": username})
        self._update_cookie()
        login_response = self.post('/Home/Login', login_request)
        if login_response["Success"] != 1:
            raise Exception("Login Error %s" % (json.dumps(login_response),))
        #"{'Success': 0, 'Message': 'Too many incorrect attempts. Reset Password.'}"
        #'{"Success":1,"IsDormant":false,"IspasswordExpire":"0","ExpireMessage":"","Message":"success","ClientStatus":"2","IsMFOnly":"N","LoginRedirect":"https://trade.5paisa.com/trade/home"}'
        self._update_cookie()
        self.session.get("https://trade.5paisa.com/trade/home")
        self._update_cookie()
        self._revive_session()
        return login_response

    def _read_config(self):
        from os.path import expanduser
        with open(expanduser("~/.5paisa.conf"), 'r') as config:
            lines = config.readlines()
        lines = [line for line in lines if len(line)>0 and not line.startswith("#")]
        username = lines[0].replace("username=","").strip()
        password = lines[1].replace("password=","").strip()
        twofa = lines[2].replace("twofa=","").strip()
        return username, password, twofa

    def get_order_book(self):
        return self.post('/Trade/Home/GetOrderBook')

    def get_margin(self):
        return self.post('/Trade/Home/GetMarginData')

    def get_trade_book(self):
        return self.post('/Trade/Home/GetTradeBook')

    def search(self, scrip, cash_or_future='C', xchange=''):
        retry = 2
        while retry>0:
            search_response = self.post('/Trade/Home/GetCashDataforSearch', {'Exch': xchange,
                                                                         'ExchType': cash_or_future,
                                                                         'Symbol': scrip})
            #{'Status': -1, 'Message': 'Exception'}
            if search_response['Status'] != -1:
                break
            self._revive_session()
            retry-=1
        return search_response

    def futures_lookup(self, scrip):
        self._lookup_one(scrip, 'F', 'N')


    def cash_lookup(self, scrip):
        self._lookup_one(scrip, 'C', 'N')

    def _revive_session(self):
        watch_list = self.post('/Trade/Home/GetMWatchName')
        if watch_list['Status'] ==0 and len(watch_list["MarketWatchList"]) >0:
            first_watch_list = watch_list["MarketWatchList"][0]['MwatchName']
            self.post('/Trade/Home/_PartialWatchList', post_type='form', data='MWatchName=%s&IsExtendedView=false'%first_watch_list)
            return
        raise Exception('Unable to get watchlists')

    def _lookup_one(self, scrip, xtype, xchange):
        search_result = self.search(scrip, xtype, xchange)
        if (search_result["Status"] == 0 and len(search_result["SearchData"]) > 0):
            filtered = [f for f in search_result["SearchData"] if f['Exchange'] == xchange] #api is not filtering properly
            if len(filtered) == 1:
                return filtered[0]["ScripCode"]
        raise Exception("Error in looking up %s type %s xchange %s got %s"%(scrip, xtype, xchange, json.dumps(search_result)))

    def _headers(self):
        return self._header_dict

    def _update_cookie(self):
        self._header_dict.update({"cookie": "; ".join(["=".join(f) for f in self.session.cookies.items()])})

    def _url(self, path):
        if path.startswith("/Home"):
            return "https://www.5paisa.com%s"%path
        return "https://trade.5paisa.com%s"%path

    def post(self, path, data={}, post_type='json'):
        if (path.startswith("/Home")) or post_type=="form":
            self._headers().update({'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
            response = self.session.post(self._url(path), headers=self._headers(), data=data)
        else:
            self._headers().update({'content-type':"application/json"})
            response = self.session.post(self._url(path), headers=self._headers(), json=data)

        if response.status_code != 200:
            raise Exception("URL %s HTTP Error %s"%(path, response.status_code), response)

        return response.json()

    def order(self, scrip, price, quantity=1, xtype='C', xchange='N'):
        if not scrip in self.scrip_map.keys():
            scrip_code = self._lookup_one(scrip, xtype, xchange)
        else:
            scrip_code = self.scrip_map[scrip]
        str_price = "%.2f"%price
        payload = {
            "BuySell": "Buy",
            "ScripCode": scrip_code,
            "Quantity": str(quantity),
            "OrderValue": str_price,
            "CurrentPrice": str_price,
            "Exch": "N",
            "ExchType": "C",
            "DiscloseQty": "0",
            "RequestType": "P",
            "Symbol": "",
            "OldOrderNumber": "",
            "Series": "",
            "TriggerRate": "0",
            "IOC": "false", "ISSL": "false",
            "TerminalId": "", "AfterHrs": "false",
            "SLStatus": "false", "isAtMarket": "false", "sProduct": "", "Validity": "0",
            "ValideDate": "/Date(1595874600000)/", "disableBuySell": "false", "CallFrom": "", "currStatus": "",
            "TradedQty": "0", "smotrailsl": "", "Volume": "0", "AdvanceBuy": "false", "BidRate": "", "OffRate": "187.6",
            "ExchOrderID": "", "ExchOrderTime": "/Date(1595921955000)/", "AHPlaced": "false",
            "DelvIntra": "D", "LastRate": "187.50", "LimitPriceforSL": "0", "TriggerPriceforSL": "0", "TrailingSL": "0",
            "LimitPriceforProfitOrder": "0", "ISTMOOrder": "", "ISCoverOrder": "", "TriggerPriceSLforCoverOrder": "0",
            "TrailingSLforCoverOrder": "0", "TriggerRateTMO": "0", "TrailingSLForNormalOrder": "0", "TickSize": "0.05",
            "SourceAPP": "6", "SliceEnable": "N"
        }
        return self.post('/Trade/Orders/OrderProceed', data=payload, post_type='form')

