from labo import *


def main():
    labo = laboratory()
    # That should word
    add(labo, "toto", "F310")
    add(labo, "tata", "F320")
    add(labo, "tete", "F320")
    add(labo, "tita", "F320")
    assert labo == {"toto": "F310", "tata": "F320", "tete": "F320", "tita": "F320"}

    remove(labo, "toto")
    assert labo == {"tata": "F320", "tete": "F320", "tita": "F320"}

    change_office(labo, "tata", "F350")
    assert labo == {"tata": "F350", "tete": "F320", "tita": "F320"}

    change_name(labo, "tete", "tito")
    assert labo == {"tata": "F350", "tito": "F320", "tita": "F320"}

    assert is_member(labo, "toto") == False
    assert is_member(labo, "tito") == True

    assert get_office(labo, 'tito') == "F320"

    for name, office in informations(labo):
        print(f"{name}'s office : {office}")
    
    # That shouldn't work
    # add(labo, "toto", "")
    # remove(labo, "titi")
    # change_office(labo, "jack", "F300")
    # change_name(labo, "toto")

    print(labo)

if __name__ == "__main__":
    main()