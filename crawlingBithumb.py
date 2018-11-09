import urllib3 as urllib
import json
import datetime
import time

class crawlingBithumb:

    http = urllib.PoolManager()

    #defind of URL
    url = "https://api.bithumb.com/public/ticker/BTC"

    #defind of exchange
    exchange = "bithumb"

    #defind of Key
    apiPriceKey = ['data','closing_price']

    def getPrice(self):

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  
        urllib.disable_warnings()
        response = self.http.request('Get',self.url)

        #server check
        if response.status != 200:
            return False

        data = response.data.decode('utf-8')
        data = json.loads(data)

        priceData = data[self.apiPriceKey[0]][self.apiPriceKey[1]]

        #Api check
        if priceData is None:
            return False

        result = {"price": priceData, "exchange": self.exchange, "time": st}
        return result