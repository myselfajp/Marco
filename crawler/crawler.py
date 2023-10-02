from abc import ABC, abstractmethod
from configs.configs import App
import threading
import queue

class AbstractCrawler(ABC):
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
        self.numThreads = 1

    def FetchLinks(self):
        from crawler.lcWaikiki.fetchLink import FetchLink
        self.links = FetchLink()

    def RunTest(self):
        from crawler.lcWaikiki.crawler import crawler
        links = self.links
        numThreads = self.numThreads
        chunkSize = len(links) // numThreads
        remainder = len(links) % numThreads
        resultQueue = []
        threads = []

        def crawl_data(data):
            for item in data:
                result = crawler(url=item["url"], categories=item["categories"])
                if result:
                     resultQueue.append(result)
                     return
        start = 0
        for i in range(numThreads):
            end = start + chunkSize + (1 if i < remainder else 0)
            thread = threading.Thread(target=crawl_data, args=(links[start:end],))
            threads.append(thread)
            thread.start()
            start = end
        for thread in threads:
            thread.join()

        for product in resultQueue:
            print(product,"\n\n")

class Zara(AbstractCrawler):
    def __init__(self) -> None:
        self.links = None
        self.name = "زارا"
        self.numThreads = 1
        
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
        self._strategy.numThreads = self._app.numThreads
        self._strategy.FetchLinks()
        data = self._strategy.RunTest()
        # for obj in data:
        #     id = self._app.DataBase.CreateOne(obj,"LcWaikiki")
        #     if id :
        #         print(f"data added with id : {id}")
        #     else:
        #         print(f"data was :{data}")

def GetStrategy(brandName : str) -> AbstractCrawler:
    if brandName == "LcWaikiki":
        return LcWaikiki()