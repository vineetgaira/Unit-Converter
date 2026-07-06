import colorama 
from colorama import Fore
colorama.init(autoreset=True)

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
    2: 0.2777777778,
    3: 0.44704
}

AREA_UNITS={
    1: 1,
    2: 1000000,
    3: 10000,
    4: 4046.86
}
            
VOLUME_UNITS={
    1: 1,
    2: 1000,
    3: 1000000,
    4: 3785.41
}

UNIT_NAMES = {
    1: {
        1: "Meter",
        2: "Kilometer",
        3: "Centimeter",
        4: "Millimeter",
        5: "Inch",
        6: "Foot",
        7: "Yard",
        8: "Mile"
    },

    2: {
        1: "Gram",
        2: "Kilogram",
        3: "Pound",
        4: "Ounce",
        5: "Ton"
    },

    3: {
        1: "Second",
        2: "Minute",
        3: "Hour",
        4: "Day",
        5: "Week"
    },

    4: {
        1: "m/s",
        2: "Km/h",
        3: "mph"
    },

    5: {
        1: "Square meter",
        2: "Square Kilometer",
        3: "Hectare",
        4: "Acre"
    },
    6: {
        1: "Milliliter",
        2: "Liter",
        3: "Cubic meter",
        4: "Gallon"
    },
    7: {
        1 : "Celcius(°C)",
        2 : "Farhenheit(°F)",
        3 : "Kelvin(K)"
    }

}

UNITS = {
    1: LENGTH_UNITS,
    2: WEIGHT_UNITS,
    3: TIME_UNITS,
    4: SPEED_UNITS,
    5: AREA_UNITS,
    6: VOLUME_UNITS
}

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
    
def choose_from_unit(max_option):

    valid_choices=set(range(1, max_option+1))
    while True:
        try:
            user_from_unit_choice=int(input(Fore.LIGHTBLUE_EX+"From unit :"))
            if user_from_unit_choice in valid_choices:
                return user_from_unit_choice
            else:
                print(Fore.RED+"Please enter a valid option from the menu.")
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option.")    

def choose_to_unit(max_option):
    valid_choices=set(range(1, max_option+1))
    while True:
        try:
            user_to_unit_choice=int(input(Fore.LIGHTBLUE_EX+"To unit :"))
            if user_to_unit_choice in valid_choices:
                return user_to_unit_choice
            else:
                print(Fore.RED+"Please enter a valid option from the menu.")
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option.")  

def convert_temperature(from_unit,to_unit,value,category):
    
    if from_unit==to_unit:
        result == value
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==1 and to_unit==2:
        result=(value*9/5)+32
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==1 and to_unit==3:
        result=(value)+273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==2 and to_unit==1:
        result=(value-32)*5/9
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==2 and to_unit==3:
        result=(value-32)*5/9+273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==3 and to_unit==1:
        result=value-273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    elif from_unit==3 and to_unit==2:
        result=(value-273.15)*9/5+32
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    return result

def convert(category,from_unit,to_unit):

    while True:
        try:
            value=float(input(Fore.LIGHTBLUE_EX+"Enter a value :"))
            break
        except ValueError:
            print(Fore.RED+"Please enter a valid value.")

    units=UNITS[category]
    base_value=value*units[from_unit]
    result=base_value/units[to_unit]
    print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")

    if category==7:
        result=convert_temperature(from_unit,to_unit,value,category)
    return result
              
def show_result():
    while True:
        display_menu()
        category=user_input()
        if category==1:
            length()
            max_option=8
        elif category==2:
            weight()
            max_option=5
        elif category==3:
            time()
            max_option=5
        elif category==4:
            speed()
            max_option=3
        elif category==5:
            area()
            max_option=4
        elif category==6:
            volume()
            max_option=4
        elif category==7:
            temperature()
            max_option=3
        from_unit=choose_from_unit(max_option)
        to_unit=choose_to_unit(max_option)
        convert(category,from_unit,to_unit)
        exit_option=input(Fore.LIGHTGREEN_EX+"Convert one more value(y/n):")
        try:
            if exit_option.lower()=="n":
                print(Fore.GREEN+"Thanks for using....")
                break
            elif exit_option.lower()=="y":
                continue
            else:
                print(Fore.RED+"Please enter y/n.")
        except ValueError:
            print(Fore.RED+"Please enter y/n.")

if __name__=="__main__":
    show_result()