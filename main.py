import colorama 
from colorama import Fore

LENGTH_UNITS = {
    1: 1,
    2: 1000,
    3: 0.01,
    4: 0.001,
    5: 0.0254,
    6: 0.3048,
    7: 0.9144,
    8: 1609.34,
}  

WEIGHT_UNITS={
    1: 1,
    2: 1000,
    3: 453.59,
    4: 28.35,
    5: 907184.74
}

TIME_UNITS={
    1: 1,
    2: 60,
    3: 3600,
    4: 86400,
    5: 604800
}

SPEED_UNITS={
    1: 1,
    2: 3.6,
    3: 2.23694
}

AREA_UNITS={
    1: 1,
    2: 1000000,
    3: 0.0001,
    4: 0.000247105
}
            
VOLUME_UNITS={
    1: 1,
    2: 1000,
    3: 1000000,
    4: 3785.41
}

UNIT_NAMES = {
    "length": {
        1: "Meter",
        2: "Kilometer",
        3: "Centimeter",
        4: "Millimeter",
        5: "Inch",
        6: "Foot",
        7: "Yard",
        8: "Mile"
    },

    "weight": {
        1: "Gram",
        2: "Kilogram",
        3: "Milligram",
        4: "Pound",
        5: "Ounce"
    },

    "time": {
        1: "Second",
        2: "Minute",
        3: "Hour",
        4: "Day"
    },

    "speed": {
        1: "m/s",
        2: "Km/h",
        3: "mph"
    },

    "area": {
        1: "Square meter",
        2: "Square Kilometer",
        3: "Hectare",
        4: "Acre"
    },
    "volume": {
        1: "Milliliter",
        2: "Liter",
        3: "Cubic meter",
        4: "Gallon"
    },
    "temperature": {
        1 : "Celcius(°C)",
        2 : "Farhenheit(°F)",
        3 : "Kelvin(K)"
    }

}

def display_menu():
    print(Fore.LIGHTGREEN_EX+"...Welcome to unit converter...\n" \
    "Choose category:\n" \
    "1 : Length\n" \
    "2 : Weight\n" \
    "3 : Temperature\n" \
    "4 : Time\n" \
    "5 : Speed\n" \
    "6 : Area\n" \
    "7 : Volume\n"
    "8 : Exit"+Fore.RESET)

def user_input():
    valid_choices={1,2,3,4,5,6,7,8}
    while True:
        try:
            user_choice=int(input(Fore.LIGHTBLUE_EX+"Choose your category :"+Fore.RESET))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(Fore.RED+"Please enter a valid category from the menu."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option."+Fore.RESET)    

def length():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Meter(m)\n" \
    "2 : Kilometer(km)\n" \
    "3 : Centimeter(cm)\n" \
    "4 : Millimeter(mm)\n" \
    "5 : Inch\n" \
    "6 : Foot\n" \
    "7 : Yard\n" \
    "8 : Mile"+Fore.RESET)

def weight():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Gram(g)\n" \
    "2 : Kilogram(kg)\n" \
    "3 : Pound\n" \
    "4 : Ounce\n" \
    "5 : Ton\n"+Fore.RESET)


def time():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Second\n" \
    "2 : Minute\n" \
    "3 : Hour\n" \
    "4 : Day\n" \
    "5 : Week"+Fore.RESET)
        
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
    "4 : Acre"+Fore.RESET)
    
def volume():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Milliliter(ml)\n" \
    "2 : Liter(l)\n" \
    "3 : Cubic meter(m^3)\n" \
    "4 : Gallon"+Fore.RESET)

def temperature():
    print(Fore.LIGHTYELLOW_EX+"..Unit Options..\n" \
    "1 : Celcius(°C)\n" \
    "2 : Farhenheit(°F)\n" \
    "3 : Kelvin(K)"+Fore.RESET)
    
def choose_from_unit():
    valid_choices={1,2,3,4,5,6,7,8}
    while True:
        try:
            user_from_unit_choice=int(input(Fore.LIGHTBLUE_EX+"From unit :"+Fore.RESET))
            if user_from_unit_choice in valid_choices:
                return user_from_unit_choice
            else:
                print(Fore.RED+"Please enter a valid option from the menu."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option."+Fore.RESET)    

def choose_to_unit():
    valid_choices={1,2,3,4,5,6,7,8}
    while True:
        try:
            user_to_unit_choice=int(input(Fore.LIGHTBLUE_EX+"To unit :"+Fore.RESET))
            if user_to_unit_choice in valid_choices:
                return user_to_unit_choice
            else:
                print(Fore.RED+"Please enter a valid option from the menu."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option."+Fore.RESET)    

def convert():
    pass
            
def show_result():
    while True:
        display_menu()
        user_choice=user_input()
        if user_choice==1:
            length()
        elif user_choice==8:
            print(Fore.CYAN+"Thanks for using..."+Fore.RESET )
            break
        result=convert()
        print(Fore.GREEN+f"After conversion :{result}"+Fore.RESET)

if __name__=="__main__":
    show_result()