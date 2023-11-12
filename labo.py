#/usr/bin/env python3
from bs4 import BeautifulSoup

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

def is_not_empty(labo: dict):
    if labo == {}:
        raise EmptyException

# Raise PresentException
def is_not_present(labo: dict, name: str) -> None:
    if name in labo:
        raise PresentException
    
# Raise AbsentException
def is_not_absent(labo: dict, name: str) -> None:
    if name not in labo:
        raise AbsentException

# Create and return an empty dict labo object
def laboratory():
    return {}


# Add someone to the lab in a office
def add(labo: dict, name: str, office: str) -> None:
    if name in labo:
        raise PresentException
    labo[name] = office


def remove(labo: dict, name: str) -> None:
    try:
        del labo[name]
    except KeyError:
        raise AbsentException


def change_office(labo: dict, name: str, new_office: str) -> None:
    if name not in labo:
        raise AbsentException
    elif labo[name] == new_office:
        raise SameException
    labo[name] = new_office


def change_name(labo: dict, old_name: str, new_name: str) -> str:
    try:
        if old_name == new_name:
            raise SameException
        labo[new_name] = labo.pop(old_name) 
    except KeyError:
        raise AbsentException


def is_member(labo: dict, name: str) -> bool: 
    return name in labo


def get_office(labo: dict, name: str) -> str :
    try:
        return labo[name]
    except KeyError:
        raise AbsentException


def people_office(labo: dict) -> list:
    is_not_empty(labo)

    # Create an ordered dict
    ord_people_office = dict()
    for name, office in sorted(labo.items()):
        ord_people_office[name] = office
    return ord_people_office


def office_occupation(labo: dict) -> dict:
    is_not_empty(labo)

    # Create office dict
    office_occ = dict()
    for name, office in sorted(labo.items()):
        if office not in office_occ:
            office_occ[office] = [name]
        else:
            office_occ[office] += [name]
    
    # Sort d_office by key, then by value
    ord_office_occ = dict()
    for office, names in sorted(office_occ.items()):
        ord_office_occ[office] = names
    for office, names in ord_office_occ.items():
        office_occ[office] = sorted(names)

    return ord_office_occ


def createhtml(labo: dict, your_title: str) -> BeautifulSoup:
    is_not_empty(labo)
    
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

# all office -> sorted(set(labo.values()))

def main():
    '''
    
    '''
    pass

if __name__ == "__main__":
    main()