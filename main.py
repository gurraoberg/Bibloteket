import csv
import os
import classes
import sqlite3

csv_path = "data/books.csv"
db_books = "data/books.db"
lb = "\n" # Linebreak

def menu():
    print("1. Add Media")
    print("2. Search Media")
    print("0. Exit")
    choice = input("Make a choice: ")
    if choice == "1":
        clear()
        print("1. Add Book")
        print("2. Add Movie")
        print("3. Add CD")
        print("0. Go back.")
        add_choice = input("Make a choice: ")
        if add_choice == "1":
            add_book()
        elif add_choice == "2":
            pass
        elif add_choice == "3":
            pass
        elif add_choice == "0":
            clear()
            menu()
    elif choice == "2":
        search_books()
    elif choice == "0":
        exit()

def import_books():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    with open(csv_path, "r", encoding = "utf-8") as file:
        bookdata = csv.reader(file)
        cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                       Title TEXT,
                       Author TEXT,
                       Pages TEXT,
                       Price TEXT,
                       Year TEXT)""")
        if db_books is None: # Doesnt work, prints duplicates. FIX LATER
            pass
        else:
            for row in bookdata:
                cursor.execute("""INSERT INTO books
                           VALUES(
                           ?,?,?,?,?)""", row)
            
        connection.commit()
        connection.close()

def search_books():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    search = input("Search for book title: ").lower()
    cursor.execute("SELECT * FROM books WHERE Title=?", (search,))
    book = cursor.fetchone()
    if book == None:
        print("Book not found.")
        menu()
    else:
        print(f"Title: {book[0]}{lb}Author: {book[1]}{lb}Pages: {book[2]}{lb}Purchase price: {book[3]}{lb}Publishing year: {book[4]}")
        print(f"Current value: ")
        back = input("\nGo back to menu, Enter 0: ")
        if back == "0":
            menu()
        else:
            print("Press 0 to go back to menu.")
    
def add_book():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    print("Enter information about your book.")
    title = input("Enter title: ").lower()
    cursor.execute("SELECT * FROM books WHERE title=?", (title,))
    add = cursor.fetchone()
    if add == None:
        author = input("Enter author: ").lower()
        pages = input("Enter pages: ").lower()
        price = input("Enter price: ").lower()
        year = input("Enter year: ").lower()
        cursor.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?)", (title, author, pages, price, year,))
        print(f"Added {title} to the library.")
        menu()
    else:
        print("This book already exists in the library.")
        menu()
    connection.commit()
    connection.close()

def clear(): # Clear the terminal
        os.system('cls' if os.name=='nt' else 'clear')

def book_value():
    pass
def main():
    import_books()
    menu()

if __name__ == "__main__":
    main()