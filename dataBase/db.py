import os
from pymongo.mongo_client import MongoClient


class MongoDB:
    def __init__(self) -> None:
        self.Client = None
        self.DataBase = None
        self.Products = None

    def Connect(self):
        uri = os.environ.get("URI")
        if not uri:
            raise ValueError("URI environment variable not set!")

        dbName = os.environ.get("DBNAME")
        if not dbName:
            raise ValueError("DBNAME environment variable not set!")

        products = os.environ.get("PRODUCTS_COLL")
        if not products:
            raise ValueError("PRODUCTS_COLL environment variable not set!")

        self.Client = MongoClient(uri)
        try:
            self.Client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Error connecting to MongoDB.")
            raise e
        self.DataBase = self.Client[dbName]
        self.Products = self.DataBase[products]

    def Disconnect(self):
        if self.Client:
            self.Client.close()
            print("Disconnected from MongoDB.")