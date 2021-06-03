import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\lijin\\PycharmProjects\\NCL\\Configurations\\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url


