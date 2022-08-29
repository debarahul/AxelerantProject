import configparser

config = configparser.RawConfigParser()
config.read(".\\Confrigurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURl():
        url = config.get('details info', 'baseURL')
        return url

    @staticmethod
    def getemailId():
        email = config.get('details info', 'emailid')
        return email

    @staticmethod
    def getPassword():
        password = config.get('details info', 'password')
        return password

    @staticmethod
    def getsubemail():
        subemailid = config.get('details info', 'subemailid')
        return subemailid

    @staticmethod
    def getsearchvalue():
        searchvalue = config.get('details info', 'searchvalue')
        return searchvalue
