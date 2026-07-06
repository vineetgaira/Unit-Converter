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
        3: "Pound",
        4: "Ounce",
        5: "Ton"
    },

    "time": {
        1: "Second",
        2: "Minute",
        3: "Hour",
        4: "Day",
        5: "Week"
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
    "3 : Time\n" \
    "4 : Speed\n" \
    "5 : Area\n" \
    "6 : Volume\n"
    "7 : Temperature"+Fore.RESET)

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

def convert_temperature(from_unit,to_unit,user_value):
    if from_unit==1 and to_unit==2:
        result=(user_value*9/5)+32
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    elif from_unit==1 and to_unit==3:
        result=(user_value)+273.15
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    elif from_unit==2 and to_unit==1:
        result=(user_value-32)*5/9
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    elif from_unit==2 and to_unit==1:
        result=(user_value-32)*5/9+273.15
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    elif from_unit==3 and to_unit==1:
        result=user_value-273.15
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    elif from_unit==3 and to_unit==2:
        result=(user_value-273.15)*9/5+32
        print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}"+Fore.RESET)
    return result

def convert(user_choice):
    while True:
        from_unit=choose_from_unit()
        to_unit=choose_to_unit()
        user_value=float(input(Fore.LIGHTBLUE_EX+"Enter a value :"+Fore.RESET))
        if user_choice==1:
            base_value=user_value*LENGTH_UNITS[from_unit]
            result=base_value/LENGTH_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["length"][from_unit]}: {result} {UNIT_NAMES["length"][to_unit]}"+Fore.RESET)
        elif user_choice==2:
            base_value=user_value*WEIGHT_UNITS[from_unit]
            result=base_value/WEIGHT_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["length"][from_unit]}: {result} {UNIT_NAMES["length"][to_unit]}"+Fore.RESET)
        elif user_choice==3:
            base_value=user_value*TIME_UNITS[from_unit]
            result=base_value/TIME_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["time"][from_unit]}: {result} {UNIT_NAMES["time"][to_unit]}"+Fore.RESET)
        elif user_choice==4:
            base_value=user_value*SPEED_UNITS[from_unit]
            result=base_value*SPEED_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["speed"][from_unit]}: {result} {UNIT_NAMES["speed"][to_unit]}"+Fore.RESET)
        elif user_choice==5:
            base_value=user_value*AREA_UNITS[from_unit]
            result=base_value/AREA_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["area"][from_unit]}: {result} {UNIT_NAMES["area"][to_unit]}"+Fore.RESET)
        elif user_choice==6:
            base_value=user_value*VOLUME_UNITS[from_unit]
            result=base_value/VOLUME_UNITS[to_unit]
            print(Fore.LIGHTCYAN_EX+f"{user_value} {UNIT_NAMES["volume"][from_unit]}: {result} {UNIT_NAMES["volume"][to_unit]}"+Fore.RESET)
        elif user_choice==7:
            result=convert_temperature(from_unit,to_unit,user_value)
        return result
              
def show_result():
    while True:
        display_menu()
        user_choice=user_input()
        if user_choice==1:
            length()
        elif user_choice==2:
            weight()
        elif user_choice==3:
            time()
        elif user_choice==4:
            speed()
        elif user_choice==5:
            area()
        elif user_choice==6:
            volume()
        elif user_choice==7:
            temperature()
        result=convert(user_choice)
        exit_option=input(Fore.LIGHTGREEN_EX+"Convert one more value(y/n):"+Fore.RESET)
        try:
            if exit_option.lower()=="n":
                print(Fore.GREEN+"Thanks for using...."+Fore.RESET)
                break
            elif exit_option.lower()=="y":
                continue
            else:
                print(Fore.RED+"Please enter y/n."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter y/n."+Fore.RESET)

if __name__=="__main__":
    show_result()