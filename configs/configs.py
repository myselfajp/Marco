from dotenv import load_dotenv
from dataBase.db import MongoDB as DataBase

class Configs :
    def __init__(self) -> None:
        self.DataBase = DataBase()
        self.Brand = None

    def DB_Connect(self):
        self.DataBase.Connect()
    def DB_Disconnect(self):
        self.DataBase.Disconnect()

def ActiveEnv() -> None:
    isLoaderActive = load_dotenv('.env')
    if not isLoaderActive :
        raise SystemExit(".env file not found")
