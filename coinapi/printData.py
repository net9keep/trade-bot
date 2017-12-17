import time
from coinapi import coinnest

class Print:
    coin_list = {"btc" : coinnest.btc(), "bch" : coinnest.bch(), "btg" : coinnest.btg(),
                 "eth" : coinnest.eth(), "mco" : coinnest.mco(), "tsl" : coinnest.tsl(),
                 "neo" : coinnest.neo(), "omg" : coinnest.omg(), "qtum" : coinnest.qtum(),
                 "tron" : coinnest.tron()}
    def print(self):
        now = time.localtime()

        s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        print("현재 시간 : ", s)
        for coin in self.coin_list:
            print(coin)
            print("정보 : ", self.coin_list[coin].get())