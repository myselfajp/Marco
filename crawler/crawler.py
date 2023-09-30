from abc import ABC, abstractmethod
from configs.configs import App
import threading

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
               
        total_data = self.links + self.links[:4]
        
        num_threads = 3
        
        def crawl_data(data):
            for item in data:
                result = crawler(url=item["url"], categories=item["categories"])
                if result:
                    # print(result)
                    yield result

        threads = []

        chunk_size = len(total_data) // num_threads
        data_chunks = [total_data[i:i + chunk_size] for i in range(0, len(total_data), chunk_size)]
        print(len(data_chunks[2]))
        for data_chunk in data_chunks:
            thread = threading.Thread(target=crawl_data, args=(data_chunk,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        # print(data_chunk)
        # for product in self.links:
        #     data=crawler(url=product["url"], categories=product["categories"])
        #     if data:
        #         yield data

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
        # for obj in data:
        #     id = self._app.DataBase.CreateOne(obj,"LcWaikiki")
        #     if id :
        #         print(f"data added with id : {id}")
        #     else:
        #         print(f"data was :{data}")

def GetStrategy(brandName : str) -> AbstractCrawler:
    if brandName == "LcWaikiki":
        return LcWaikiki()