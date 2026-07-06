import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from constants import UNITS,UNIT_NAMES
from menu_functions import display_menu,user_input,length,weight,time,speed,area,volume,temperature
    
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

def convert_temperature(from_unit,to_unit,value):
    
    if from_unit==to_unit:
        result == value
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==1 and to_unit==2:
        result=(value*9/5)+32
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==1 and to_unit==3:
        result=(value)+273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==2 and to_unit==1:
        result=(value-32)*5/9
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==2 and to_unit==3:
        result=(value-32)*5/9+273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==3 and to_unit==1:
        result=value-273.15
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    elif from_unit==3 and to_unit==2:
        result=(value-273.15)*9/5+32
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES["temperature"][from_unit]}: {result} {UNIT_NAMES["temperature"][to_unit]}")
    return result

def convert(category,from_unit,to_unit):

    while True:
        try:
            value=float(input(Fore.LIGHTBLUE_EX+"Enter a value :"))
            break
        except ValueError:
            print(Fore.RED+"Please enter a valid value.")
    units=UNITS[category]
    if category in UNITS:
        base_value=value*units[from_unit]
        result=base_value/units[to_unit]
        print(Fore.LIGHTCYAN_EX+f"{value} {UNIT_NAMES[category][from_unit]}: {result} {UNIT_NAMES[category][to_unit]}")
    else:
        result=convert_temperature(from_unit,to_unit,value)
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
        while True:
            exit_option=input(Fore.LIGHTGREEN_EX+"Convert one more value(y/n):").lower()
            if exit_option=="y":
                break
            elif exit_option.lower()=="n":
                print(Fore.GREEN+"Thanks for using....")
                return
            else:
                print(Fore.RED+"Please enter y/n.")
                continue
            

if __name__=="__main__":
    show_result()