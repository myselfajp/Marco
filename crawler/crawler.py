from abc import ABC, abstractmethod
from configs.configs import App

class AbstractCrawler(ABC):
    def __init__(self) -> None:
        self.Categories = None
    @abstractmethod
    def FetchLinks(self):
        pass
    @abstractmethod
    def RunTest(self):
        pass


class LcWaikiki(AbstractCrawler):
    def __init__(self) -> None:
        self.links = None
        self.name = "ال سی وایکیکی"
    def FetchLinks(self):
        from crawler.lcWaikiki.fetchLink import FetchLink
        self.links = FetchLink()

    def RunTest(self):
        from crawler.lcWaikiki.crawler import crawler
        for product in self.links:
            data=crawler(url=product["url"], categories=product["categories"])
            if data:
                yield data

class Zara(AbstractCrawler):
    def FetchLinks(self):
        from zara.fetchLink import FetchLink
        FetchLink()
    def RunTest(self):
        pass

class CrawlerContext:
    def __init__(self):
        self._strategy = None
        self._app = None
    def SetStrategy(self, strategy: AbstractCrawler):
        self._strategy = strategy
        return self
    def SetConfig(self,config : App):
        self._app = config
        return self
    def ExecuteCrawling(self):
        self._strategy.FetchLinks()
        data = self._strategy.RunTest()
        for obj in data:
            id = self._app.DataBase.CreateOne(obj,"LcWaikiki")
            if id :
                print(f"data added with id : {id}")
            else:
                print(f"data was :{data}")
