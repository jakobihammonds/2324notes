from conversions import Converter


yippee = "tbd function"
userinterface = '''
       1- meters to lightyears
       2- inches to feet
       3- moles to kg
       4- m\s to ft\s
       5- lb to kg
       6- k to f
       7 f to k
       - quit to quit the program
'''
ui = input(userinterface)
while(ui!="quit"):
    if ui == "1":
        meters = int(input("meters: "))
        print(Converter.meterstolightyears(meters))
    elif ui == "2":
        inches = int(input("inches: "))
        print(Converter.inToFt(inches))
    elif ui == "3":
        print(yippee)
    elif ui == "4":
        print(yippee)
    elif ui == "5":
        print(yippee)
    elif ui == "6":
        kelvin = int(input("kelvin: "))
        print(Converter.ktof(kelvin))
    elif ui == "7":
        fahrenheit = int(input("fahrenheit: "))
        print(Converter.ftok(fahrenheit))
    else:
        print("sorry didnt get that")
    ui = input(userinterface)





