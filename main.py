import colorama 
from colorama import Fore, Back, Style

def display_menu():
    print(Fore.LIGHTGREEN_EX+"...Welcome to unit converter...\n" \
    "Choose category:\n" \
    "1 : Length\n" \
    "2 : Weight\n" \
    "3 : Temperature\n" \
    "4 : Time\n" \
    "6 : Speed\n" \
    "8 : Area\n" \
    "9 : Volume\n"
    "10 : Exit"+Fore.RESET)

def user_input():
    valid_choices={1,2,3,4,5,6,7,8,9}
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
    "2 : Kilomter(km)\n" \
    "3 : Centimeter(cm)\n" \
    "4 : Milimeter(mm)\n" \
    "5 : Inch\n" \
    "6 : Foot\n" \
    "7 : Yard\n" \
    "8 : Mile"+Fore.RESET)

def weight():
    pass
def temperature():
    pass
def time():
    pass
def speed():
    pass
def area():
    pass
def volume():
    pass
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
    length_units = {
    1: 1,
    2: 1000,
    3: 0.01,
    4: 0.001,
    5: 1609.34,
    6: 0.3048,
    7: 0.0254,
    8: 0.9144
}  
    from_unit=choose_from_unit()
    to_unit=choose_to_unit()
    while True:
        try:
            user_value=int(input(Fore.LIGHTBLUE_EX+"Enter a value :"+Fore.RESET))
            base_value=user_value * length_units[from_unit]
            result=base_value/length_units[to_unit]
            return result
        except ValueError:
            print(Fore.RED+"Please enter a valid integer option."+Fore.RESET)  
            
            
def show_result():
    display_menu()
    user_choice=user_input()
    if user_choice==1:
        length()
        result=convert()
    print(Fore.GREEN+f"After conversion :{result}"+Fore.RESET)

if __name__=="__main__":
    show_result()