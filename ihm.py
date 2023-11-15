from labo import *
import menu

'''
    Possible choices:
    "1 - Add someone to the lab", 
    "2 - Remove someone to the lab", 
    "3 - Change someone's office", 
    "4 - Change someone's name", 
    "5 - Check membership of the lab", 
    "6 - Get someone's office", 
    "7 - Get all people in the lab with the office displayed", 
    "8 - Get offices occupation", 
    "9 - Create an html file with offices occupation", 
    "0 - Quit"
'''

menu_list = ["1 - Add someone to the lab", 
             "2 - Remove someone to the lab", 
             "3 - Change someone's office", 
             "4 - Change someone's name", 
             "5 - Check membership of the lab", 
             "6 - Get someone's office", 
             "7 - Get all people in the lab with the office displayed", 
             "8 - Get offices occupation", 
             "9 - Create an html file with offices occupation", 
             "0 - Quit"]

# Ask choice of user
def get_choice():
    while True:
        try: 
            choice = int(input("Choice ? "))
            return choice
        except ValueError:
            print("Not valid")

# Treat the add options
def call_add(labo: dict) -> None:
    try:
        name = input("Name : ")
        check_absent(labo, name)
        office = input("Office : ")
        print()
        add(labo, name, office)
        print(name, ': added')
    except PresentException:
        print()
        print("Already member")
        print('No changes')

# Treat the remove options
def call_remove(labo: dict) -> None:
    try:
        name = input("Name to remove : ")
        print()
        check_present(labo, name)
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
        check_present(labo, name)
        print(f"old office : {labo[name]}")
        # Ask new office
        new_office = input("New office : ")
        print()
        change_office(labo, name, new_office)
        print(f"{name} is now in the office : {new_office}")
    except AbsentException:
        print(name, "is not in the lab")
        print('No changes')
    except SameException:
        print('Old office and new office are the same')
        print('No changes')
    
# Treat change name
def call_change_name(labo: dict) -> None:
    try:
        old_name = input("Old name : ")
        check_present(labo, old_name)
        new_name = input("New name : ")
        print()
        change_name(labo, old_name, new_name)
        print(f"{old_name} renamed {new_name}")
    except AbsentException:
        print(old_name, "is not in the lab")
        print('No changes')
    except SameException:
        print("Both are the same")
        print("No changes")

# Get membership of ther lab
def call_is_member(labo: dict) -> None:
    name = input("Name : ")
    print()
    print(f"{name} is in the lab" if is_member(labo, name) else f"{name} is not in the lab")

def call_get_office(labo: dict) -> None:
    try:
        name = input("Name of the person's office : ")
        print()
        office = get_office(labo, name)
        print(f"{name} is in office: {office}")
    except AbsentException:
        print(f"{name} is not in the lab")

# Get all people and their office
def call_people_office(labo: dict) -> None:
    try:
        for name, office in people_office(labo):
            print(f"name: {name} -> office: {office}")
    except EmptyException:
        print("Nobody registered")

# Get all offices and the people in it
def call_office_occupation(labo: dict) -> None:
    try:
        for office, names in office_occupation(labo):
            print(f"{office}:")
            for name in names:
                print(f"- {name}")
    except EmptyException:
        print("Nobody registered")

# Create an html with all offices and the people in it
def call_create_html(labo: dict) -> None:
    try:
        title = "office_occupation"
        print(f"Creating {title}.html")
        print()
        create_html(labo, title)
        print(f"{title}.html created !")
    except EmptyException:
        print("Labo is empty")
        print("No html file created")

# Treat the different choices    
def choices(labo: dict, choice: str) -> None:
    if choice == 1:
        call_add(labo)
    elif choice == 2:
        call_remove(labo)
    elif choice == 3:
        call_change_office(labo)
    elif choice == 4:
        call_change_name(labo)
    elif choice == 5:
        call_is_member(labo)
    elif choice == 6:
        call_get_office(labo)
    elif choice == 7:
        call_people_office(labo)
    elif choice == 8:
        call_office_occupation(labo)
    elif choice == 9:
        call_createhtml(labo)

def main():
    labo = laboratory()
    quit = False
    while not quit:
        menu.menu(menu_list)
        choice = get_choice()
        choices(labo, choice)
        quit = choice == 0
    

if __name__ == "__main__":
    main()