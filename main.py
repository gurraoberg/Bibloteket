import os
import sqlite3
import borrow
import functions

library_db = "data/library.db"
connection = sqlite3.connect(library_db)
cursor = connection.cursor()

def menu(): # Menu
    print("""
    1. Add Media
    2. Search Media
    3. Check Value
    4. Borrow Media
    5. Return Media
    6. Borrowed Media
    0. Exit Program
          """)
    choice = input("Make a choice: ")
    if choice == "1": # Add
        functions.clear()
        functions.add_media()
        functions.menu_back()
    elif choice == "2": # Search
        functions.clear()
        print("""
    1. Search the library
    2. Check the libraries content
    0. Go back.
        """)
        search_choice = input("Make a choice: ")
        if search_choice == "1":
            functions.search()
            menu_back()
        elif search_choice == "2":
            functions.sorted_database()
            menu_back()
        elif search_choice == "0":
            functions.clear()
            menu()
    elif choice == "3": # Value
        functions.clear()
        print("""
    1. Check value of Media
    2. Check total value of the library
    0. Go back.
        """)
        value_choice = input("Make a choice: ")
        if value_choice == "1":
            functions.check_value()
            menu_back()
        elif value_choice == "2":
            functions.whole_value()
            menu_back()
        elif value_choice == "0":
            functions.clear()
            menu()
    elif choice == "4":
        borrow.table_register()
        borrow.borrow()
        menu_back()
    elif choice == "5":
        borrow.return_media()
        menu_back()
    elif choice == "6":
        borrow.who_borrowed()
        menu_back()
    elif choice == "0":
        connection.close()
        exit()
        
def menu_back(): # Goes back to menu.
        back = input("\nGo back to menu, Enter 0: ")
        if back == "0":
            functions.clear()
            menu()
        else:
            print("Press 0 to go back to menu.")
            
def main():
    functions.clear()
    functions.import_library()
    menu()

if __name__ == "__main__":
    main()