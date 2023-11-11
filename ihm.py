from labo import *
import menu

menu_list = ["1 - Add someone to the lab", "2 - Remove someone to the lab", "3 - Change someone's office", "4 - Change someone's name", "5 - Check membership of the lab", "6 - Get someone's office", "0 - Quit"]

# Print menu
# def menu():
#     print("1 - Add someone to the lab")
#     print("2 - Remove someone to the lab")
#     print("3 - Change someone's office")
#     print("4 - Change someone's name")
#     print("5 - Check membership of the lab")
#     print("6 - Get someone's office")
#     print("0 - Quit")

# Ask choice of user
def ask_choice():
    try: 
        choice = int(input("Choice ? "))
        return choice
    except ValueError:
        print("Not valid")

# Treat the labo options
def labo_handler() -> dict:
    return laboratory()

# Treat the add options
def call_add(labo: dict) -> None:
    try:
        name = input("Name : ")
        is_not_present(labo, name)
        office = input("Office : ")
        add(labo, name, office)
        print(name, ': added')
    except PresentException:
        print("Already member")
        print('No changes')

# Treat the remove options
def call_remove(labo: dict) -> None:
    try:
        name = input("Name to remove : ")
        is_not_absent(labo, name)
        remove(labo, name)
        print(name, "removed")
    except AbsentException:
        print("Not a member of the labo")
        print('No changes')

# Treat change office
def call_change_office(labo: dict) -> None:
    try:
        # Ask name
        name = input("Name of the person changing office : ")
        is_not_absent(labo, name)
        print(f"old office : {labo[name]}")
        # Ask new office
        new_office = input("New office : ")
        change_office(labo, name, new_office)
        print(f"{name} is now in the office : {new_office}")
    except AbsentException:
        print(name, "is not in the lab")
    except SameException:
        print('Old office and new office are the same')
        print('No changes')
    
# Treat change name
def call_change_name(labo: dict) -> None:
    try:
        old_name = input("Old name :")
        is_not_absent(labo, old_name)
        new_name = input("New name :")
        change_name(labo, old_name, new_name)
        print('Done !')
    except AbsentException:
        print(old_name, "is not in the lab")
        print('No changes')
    except SameException:
        print("Both are the same")
        print("No changes")

def call_check_member(labo: dict) -> None:
    name = input("Name : ")
    print(f"{name} is in the lab" if check_member(labo, name) else f"{name} isn't in the lab")

def call_get_office(labo: dict) -> None:
    try:
        name = input("Name of the person's office : ")
        office = get_office(labo, name)
        print(f"{name} is in the {office}")
    except AbsentException:
        print(f"{name} isn't in the lab")

def call_get_all_office(labo: dict) -> None:
    print(get_all_office(labo))

# Treat the different choices    
def handle_choice(labo: dict, choice: str) -> None:
    if choice == 1:
        call_add(labo)
    elif choice == 2:
        call_remove(labo)
    elif choice == 3:
        call_change_office(labo)
    elif choice == 4:
        call_change_name(labo)
    elif choice == 5:
        call_check_member(labo)
    elif choice == 6:
        call_get_office(labo)
    elif choice == 7:
        call_get_all_office(labo)

def main():
    labo = labo_handler()
    quit = False
    while not quit:
        menu.menu(menu_list)
        choice = ask_choice()
        handle_choice(labo, choice)
        quit = choice == 0
        print(labo)
    

if __name__ == "__main__":
    main()