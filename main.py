from configs.configs import NewConfig
from crawler.crawler import CrawlerContext,LcWaikiki

# Create database connection
App = NewConfig()

# Set strategy and fetch data
crawler = CrawlerContext().SetStrategy(LcWaikiki()).SetConfig(App)

data = crawler.ExecuteCrawling()

App.DB_Disconnect()
