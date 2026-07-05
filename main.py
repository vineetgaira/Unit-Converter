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

def user_choice():
    valid_choices={1,2,3,4,5,6,7,8,9}
    while True:
        try:
            user_choice=int(input("Choose your category :"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please enter a valid category from the menu.")
        except ValueError:
            print("Please enter a valid integer option.")
            
        

def length():
    pass
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
    pass
def choose_to_unit():
    pass
def convert():
    pass
def show_result():
    pass

user_choice()