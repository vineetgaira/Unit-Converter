import colorama
from colorama import Fore
colorama.init(autoreset=True)

def display_menu():
    print(Fore.LIGHTGREEN_EX+"...Welcome to unit converter...\n" \
    "Choose category:\n" \
    "1 : Length\n" \
    "2 : Weight\n" \
    "3 : Time\n" \
    "4 : Speed\n" \
    "5 : Area\n" \
    "6 : Volume\n"
    "7 : Temperature")

def user_input():
    valid_choices={1,2,3,4,5,6,7}
    while True:
        try:
            category=int(input(Fore.LIGHTBLUE_EX+"Choose your category :"))
            if category in valid_choices:
                return category
            else:
                print(Fore.RED+"Please enter a valid category from the menu.")
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option.")    

def length():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Meter(m)\n" \
    "2 : Kilometer(km)\n" \
    "3 : Centimeter(cm)\n" \
    "4 : Millimeter(mm)\n" \
    "5 : Inch\n" \
    "6 : Foot\n" \
    "7 : Yard\n" \
    "8 : Mile")

def weight():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Gram(g)\n" \
    "2 : Kilogram(kg)\n" \
    "3 : Pound\n" \
    "4 : Ounce\n" \
    "5 : Ton\n")

def time():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Second\n" \
    "2 : Minute\n" \
    "3 : Hour\n" \
    "4 : Day\n" \
    "5 : Week")
        
def speed():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n"
    "1 : m/s\n"
    "2 : Km/h\n"
    "3 : mph")

def area():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Square meter\n" \
    "2 : Square Kilometer\n" 
    "3 : Hectare\n" \
    "4 : Acre")
    
def volume():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Milliliter(ml)\n" \
    "2 : Liter(l)\n" \
    "3 : Cubic meter(m^3)\n" \
    "4 : Gallon")

def temperature():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Celcius(°C)\n" \
    "2 : Farhenheit(°F)\n" \
    "3 : Kelvin(K)")