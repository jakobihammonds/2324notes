class Converter:
    #all of the functions for our Unit Converter
    #first letter caps cus its a class
    #static method - can run without object
    @staticmethod #@ sign is decorator
    def inToFt(inches):
        return inches/12
    @staticmethod
    def meterstolightyears(meters):
        return meters/9.46e+15
    @staticmethod
    def ktof(kelvin):
        return((int(kelvin)-273.15)*1.8+32)
    @staticmethod
    def ftok(fahrenheit):
        return((((int(fahrenheit)-32)*5)/9)+273.15)
