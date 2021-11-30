import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getfirstName():
        firstName = config.get('user info', 'firstName')
        return firstName

    @staticmethod
    def getlastName():
        lastName = config.get('user info', 'lastName')
        return lastName

    @staticmethod
    def getPostalCode():
        postalCode = config.get('user address', 'postal_code')
        return postalCode

    @staticmethod
    def getCity():
        city = config.get('user address', 'city')
        return city

    @staticmethod
    def getStreet():
        street = config.get('user address', 'street')
        return street

    @staticmethod
    def getNumber():
        number = config.get('user address', 'number')
        return number

    @staticmethod
    def getVoucher():
        voucher = config.get('vouchers', 'qavoucher')
        return voucher
