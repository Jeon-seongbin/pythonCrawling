import crawlingCoincheck
import crawlingBithumb
import insert
import sys

def serverDownCheck(arg):
    if(arg is False):
        sys.exit(1)

#defind of dataStore
dataStore = []

#defind of Database instance
insertRun = insert.InsertMongoDb()

'''
instancing, get price , and append in datastore
duck typing
'''

#get coincheck of Bitcoin price
run = crawlingCoincheck.crawlingCoincheck()
dataStore.append(run.getPrice())

#get bithumb of Bitcoin price
run = crawlingBithumb.crawlingBithumb()
dataStore.append(run.getPrice())

#server down check
serverDownCheck(run)

#insert into database
insertRun.insertData(dataStore)