import sqlite3
import json
import os
import classes
import functions

def clear(): # Clear the terminal
        os.system('cls' if os.name=='nt' else 'clear')

class Menu:
    
    MAIN_MENU_TEXT = """
    Main menu
    
    1. Add media
    2. Search media
    
    0. Exit program
    """
    
    ADD_MENU_TEXT = """
    Add Media Menu
    
    What type of media would you like to add?
    1. Book
    2. Movie
    3. CD
    
    0. Go back.
    """
    
    SEARCH_MENU_TEXT = """
    Search Media Menu
    
    What type of media would you like to search for?
    1. Book
    2. Movie
    3. CD
    
    0. Go back.
    """
    
    def user_choice(self):
        return input("Make a choice: ")
    
    def wait_for_user(self):
        if self.running:
            input("Press any key to go back.")
            clear()
            
    def menu_commands(self, choice):
        if choice == "0":
            self.running = False
        elif choice == "1":
            clear()
            print(Menu.ADD_MENU_TEXT)
            add = input("Make a choice: ")
            if add == "1": # Add Media menu
                functions.add_media()
            elif add == "2":
                pass
            elif add == "3":
                pass
            elif add == "0":
                clear()
                print(Menu.MAIN_MENU_TEXT)
        elif choice == "2":
            clear()
            print(Menu.SEARCH_MENU_TEXT)
            search = input("Make a choice: ")
            if search == "1": # Search Media menu
                functions.search_database()
            elif search == "2":
                pass
            elif search == "3":
                pass
            elif search == "0":
                clear()
                print(Menu.MAIN_MENU_TEXT)
                
    def start_loop(self):
        self.running = True
        functions.import_database()
        while self.running:
            clear()   
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()
     
Menu().start_loop()