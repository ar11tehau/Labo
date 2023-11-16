from labo import *
from menu import *

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

# Add someone to the lab in a office
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

# Remove someone from the lab
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

# Change someone's office
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
    
# Change someone's name
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

# Check membership of ther lab
def call_is_member(labo: dict) -> None:
    name = input("Name : ")
    print()
    print(f"{name} is in the lab" if is_member(labo, name) else f"{name} is not in the lab")

# Get someone office
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
        for name, office in people_office(labo).items():
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

# Get json name from user
def get_json_name() -> None:
    return input("json file name : ")

def get_json_export_comfirm() -> None:
    while True:
        print("Your current laboratory is not empty")
        print("Import json_file will erase the current laboratory data")
        confirm = input("Continue ? [Y/n]: ").lower() or "y"
        if confirm in ["y", "yes", "n", "no"]:
            return confirm.lower() in ["y", "yes"]

# Export json
def call_json_import(labo: dict) -> dict:
    if is_empty(labo):
        return json_import(get_json_name())
    else:
        if get_json_export_comfirm():
            return json_import(get_json_name())

# Create the menu
def call_menu(get_labo: list, menu: Menu):
    menu.add("Add someone to the lab", lambda: call_add(get_labo[0]))
    menu.add("Remove someone to the lab", lambda: call_remove(get_labo[0]))
    menu.add("Change someone's office", lambda: call_change_office(get_labo[0]))
    menu.add("Check membership of the lab", lambda: call_is_member(get_labo[0]))
    menu.add("Get someone's office", lambda: call_get_office(get_labo[0]))
    menu.add("Get all people in the lab with the office displayed", lambda: call_people_office(get_labo[0]))
    menu.add("Get offices occupation", lambda: call_office_occupation(get_labo[0]))
    menu.add("Get offices occupation", lambda: call_create_html(get_labo[0]))
    menu.add("Create an html file with offices occupation", lambda: call_add(get_labo[0]))
    menu.add("Export", lambda: json_export(get_labo[0], get_json_name()))
    menu.add("Import", lambda: call_json_import(get_labo[0]))


def main():
    labo = laboratory()
    get_labo = list()
    get_labo.append(labo)
    my_menu = Menu()  
    call_menu(get_labo, my_menu)
    quit = False
    while not quit:
        response = my_menu.manage()
        if response not in [None, 0]:
            labo = response
            get_labo[0] = labo    
        quit = response == 0
    
if __name__ == "__main__":
    main()