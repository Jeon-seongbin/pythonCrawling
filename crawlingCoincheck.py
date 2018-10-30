import json
import urllib2
import datetime
import time

class crawlingCoincheck:

    #defind of URL
    Url = "https://coincheck.com/api/ticker.json?pair=btc_jpy"

    #defind of exchange
    exchange = "coincheck"

    def GetPrice(self):


        ts = time.time();
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        result = []

        data = urllib2.urlopen(self.Url)

        #url check
        urlResult = data.getcode()

        #check
        if urlResult != 200:
            return False

        data = json.load(data)

        #check
        if data['last'] is None:
            return False

        priceData = data['last']
        result.append({"price": priceData, "exchange": self.exchange, "time": st})
        print result
        return result