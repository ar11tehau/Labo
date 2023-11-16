import inspect

class Menu:
    '''
    
    '''
    def __init__(self):
        self.entries = []
    
    def add(self, txt: str, func):
        self.entries.append([txt, func])  
    
    def delete_all(self):
        self.entries = []
    # Modify the given choice description
    # Choice start at 1 but list at 0
    def mod_txt(self, choix: int, txt: str):
        self.entries[choix + 1] = txt 

    # Modify the given choice function
    def mod_func(self, choix: int, func: str):
        self.entries[choix + 1] = func 

    # Display the menu
    def display_menu(self):
        print()
        for numero, (txt, _) in enumerate(self.entries, 1):
            print(f"{numero:2} - {txt}")
        print(" 0 - Quit")
        print()
    
    # Get the user choice
    def __get_choice(self):
        while True:
            try:
                choice = int(input("Your choice: "))
                if choice > len(self.entries):
                    raise ValueError
                return choice
            except:
                print("Not valid")
                print()
    
    # Launch the function's choice
    def manage(self):
        self.display_menu()
        choice = self.__get_choice()
        if 0 < choice <= len(self.entries):
            print()
            return self.entries[choice - 1][1]()
        else:
            return choice        

    # Handle the print output
    def __str__(self):
        descriptions = str()
        for description, _ in self.entries:
            descriptions += description + "\n"
        return f'Texte description : {descriptions}'