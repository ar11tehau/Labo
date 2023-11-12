from labo import *


def main():
    labo = laboratory()
    # That should word
    add(labo, "toto", "F310")
    add(labo, "tata", "F320")
    add(labo, "tete", "F320")
    add(labo, "tita", "F320")
    add(labo, "ana", "F320")
    add(labo, "arii", "F310")
    assert labo == {"toto": "F310", "tata": "F320", "tete": "F320", "tita": "F320", "ana": "F320", "arii": "F310"}

    remove(labo, "toto")
    assert labo == {"tata": "F320", "tete": "F320", "tita": "F320", "ana": "F320", "arii": "F310"}

    change_office(labo, "tata", "F350")
    assert labo == {"tata": "F350", "tete": "F320", "tita": "F320", "ana": "F320", "arii": "F310"}

    change_name(labo, "tete", "tito")
    assert labo == {"tata": "F350", "tito": "F320", "tita": "F320", "ana": "F320", "arii": "F310"}

    assert is_member(labo, "toto") == False
    assert is_member(labo, "tito") == True

    assert get_office(labo, 'tito') == "F320"

    assert people_office(labo) == {'ana': 'F320', 'arii': 'F310', 'tata': 'F350', 'tita': 'F320', 'tito': 'F320'}

    assert office_occupation(labo) == {'F310': ['arii'], 'F320': ['ana', 'tita', 'tito'], 'F350': ['tata']}

    createhtml(labo, "office_occupation")
    
    # That shouldn't work
    # add(labo, "toto", "")
    # remove(labo, "titi")
    # change_office(labo, "jack", "F300")
    # change_name(labo, "toto")


    #print(labo)

if __name__ == "__main__":
    main()