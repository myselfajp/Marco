from configs.configs import NewConfig
from crawler.crawler import CrawlerContext,GetStrategy

App = NewConfig()
App.numThreads = 8
strategy = GetStrategy("LcWaikiki")
crawler = CrawlerContext().SetStrategy(strategy).SetConfig(App)

data = crawler.ExecuteCrawling()

App.DB_Disconnect()