#/usr/bin/env python3
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

# Raise PresentException
def is_not_present(labo: dict, name: str) -> None:
    if name in labo:
        raise PresentException
    
# Raise AbsentException
def is_not_absent(labo: dict, name: str) -> None:
    if name not in labo:
        raise AbsentException

# Create and return a dict labo object
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


def check_member(labo: dict, name: str) -> bool: 
    return name in labo


def get_office(labo: dict, name: str) -> str :
    '''
    Take a name in and return the office
    '''
    try:
        return labo[name]
    except KeyError:
        raise AbsentException



def get_all_office(labo: dict) -> list:
    '''
    Take labo as input then return a sorted list of all offices
    '''
    return sorted(set(labo.values()))

def main():
    '''
    
    '''
    pass

if __name__ == "__main__":
    main()