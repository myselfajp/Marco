from configs.configs import NewConfig

config = NewConfig()

config.DB_Connect()


print(config.DataBase.Client)
