import json
import urllib3 as urllib
import datetime
import time

class crawlingCoincheck:

    http = urllib.PoolManager()

    #defind of URL
    url = "https://coincheck.com/api/ticker.json?pair=btc_jpy"

    #defind of exchange
    exchange = "coincheck"

    def GetPrice(self):

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        result = []

        urllib.disable_warnings()
        response = self.http.request('Get',self.url)

        #check
        if response.status != 200:
            return False

        data = response.data.decode('utf-8')
        data = json.loads(data)

        #check
        if data['last'] is None:
            return False

        priceData = data['last']
        result.append({"price": priceData, "exchange": self.exchange, "time": st})

        return result