import crawlingCoincheck
import insert

run = crawlingCoincheck.crawlingCoincheck()
insertRun = insert.InsertMongoDb()

data = run.GetPrice()
insertRun.insertData(data)