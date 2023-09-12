from configs.configs import ActiveEnv
from configs.configs import Configs

ActiveEnv()

config = Configs()

config.DB_Connect()


print(config.DataBase.Client)
