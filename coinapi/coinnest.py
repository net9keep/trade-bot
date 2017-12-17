import json
import requests
import urllib3.request
import ssl

#btc,bt1,bt2,bch,btg,bcd,eth,etc,ada,qtum,xlm,neo,gas,rpx,hsr,knc,tsl,tron,omg,wtc,mco,ink
api_link = "https://api.coinnest.co.kr/api/pub/ticker"

class btc:
    url = "?coin=btc"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("비트코인 : ", reqs.json())
class eth:
    url = "?coin=eth"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("이더리움 : ", reqs.json())
class bch:
    url = "?coin=bch"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("비트코인캐시 : ", reqs.json())
class btg:
    url = "?coin=btg"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("비트코인골드 : ", reqs.json())
class ada:
    url = "?coin=ada"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url, )
        print("에이다 : ", reqs.json())
class qtum:
    url = "?coin=qtum"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("큐텀 : ", reqs.json())
class neo:
    url = "?coin=neo"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("네오 : ", reqs.json())
class tsl:
    url = "?coin=tsl"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("에너고 : ", reqs.json())
class tron:
    url = "?coin=tron"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("트론 : ", reqs.json())
class omg:
    url = "?coin=omg"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("오미세고 : ", reqs.json())
class mco:
    url = "?coin=mco"
    def get(self):
        reqs = requests.get("https://api.coinnest.co.kr/api/pub/ticker"+self.url)
        print("모나코 : ", reqs.json())

