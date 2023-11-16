#/usr/bin/env python3
from bs4 import BeautifulSoup
import json

class LaboException(Exception):
    """ 
    Généralise les exceptions du laboratoire.
    """
    pass

class AbsentException(LaboException):
    pass

class PresentException(LaboException):
    pass

class SameException(LaboException):
    pass

class EmptyException(LaboException):
    pass

# Raise EmptyException
def is_empty(labo: dict) -> bool:
    return labo == {}

# Raise EmptyException
def check_not_empty(labo: dict):
    if labo == {}:
        raise EmptyException

# Raise PresentException
def check_absent(labo: dict, name: str) -> None:
    if name in labo:
        raise PresentException
    
# Raise AbsentException
def check_present(labo: dict, name: str) -> None:
    if name not in labo:
        raise AbsentException

# Create and return an empty dict labo object
def laboratory() -> dict:
    return {}

# Add someone to the lab in a office
def add(labo: dict, name: str, office: str) -> None:
    check_absent
    labo[name] = office

# Remove someone from the lab
def remove(labo: dict, name: str) -> None:
    try:
        del labo[name]
    except KeyError:
        raise AbsentException

# Change someone's office
def change_office(labo: dict, name: str, new_office: str) -> None:
    check_present(labo, name)
    if labo[name] == new_office:
        raise SameException
    labo[name] = new_office

# Change someone's name
def change_name(labo: dict, old_name: str, new_name: str) -> None:
    try:
        if old_name not in labo:
            raise SameException
        labo[new_name] = labo.pop(old_name) 
    except KeyError:
        raise AbsentException

# Check membership of ther lab
def is_member(labo: dict, name: str) -> bool: 
    return name in labo

# Get someone office
def get_office(labo: dict, name: str) -> dict:
    try:
        return labo[name]
    except KeyError:
        raise AbsentException

# Get all people and their office
def people_office(labo: dict) -> dict:
    check_not_empty(labo)

    # Create an ordered dict
    ord_people_office = dict()
    for name, office in sorted(labo.items()):
        ord_people_office[name] = office
    return ord_people_office

# Get all offices and the people in it
def office_occupation(labo: dict) -> dict:
    check_not_empty(labo)

    # Create office dict
    office_occ = dict()
    for name, office in labo.items():
        if office not in office_occ:
            office_occ[office] = [name]
        else:
            office_occ[office].append(name)
    
    # Sort d_office by key, then by value
    ord_office_occ = dict()

    # Sort offices
    for office, names in sorted(office_occ.items()):
        ord_office_occ[office] = names
    
    # Sort names for each offices
    for office, names in ord_office_occ.items():
        office_occ[office] = names.sort()
    
    return ord_office_occ

# Create an html with all offices and the people in it
def create_html(labo: dict, your_title: str) -> None:
    check_not_empty(labo)
    
    soup = BeautifulSoup(features="html.parser")

    # Create tags
    html_content = soup.new_tag('html')
    head = soup.new_tag('head')
    title = soup.new_tag('title')
    body = soup.new_tag('body')

    # Create the content of the main tags
    title.string = your_title

    # Append the main tags
    html_content.append(head)
    head.append(title)
    html_content.append(body)

    # Create and append the content of the remaining tags
    for office, names in office_occupation(labo).items():
        ul = soup.new_tag('ul')
        ul.string = "Office : " + office
        for name in names:
            li = soup.new_tag('li')
            li.string = name.capitalize() 
            ul.append(li)
            body.append(ul)

    # Print the HTML content
    #print(html_content.prettify())
    with open(f'{your_title}.html', 'w') as html:
        html.write(str(html_content))

# Export the lab into a json
def json_export(labo: dict, file_name: str) -> None:
    try:
        file_path = file_name + '.json'
        with open(file_path, 'w') as json_file:
            json.dump(labo, json_file)
            print(f"File saved to : {file_path}")
    except Exception as error:
        print("Something went wrong, didn't save the file")
        print(error)

# Import the json file then return lab dict
def json_import(file_name: str) -> dict:
    try:
        if not file_name.endswith(".json"):
            file_name += ".json"
        with open(file_name, 'r') as json_file:
            labo = json.load(json_file)
            print(f"{file_name} file imported")
            return labo
    except Exception as error:
        print("Something went wrong, nothing to return")
        print(error)

def main():
    '''
    '''
    pass

if __name__ == "__main__":
    main()