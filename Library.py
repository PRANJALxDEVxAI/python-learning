import math 

class Library:
    def __init__ (self):
        self.books = []

    def add_books(self,book):
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book}' added to the library.")
            print()
        else:
            print("Book already exists.")
            print()
        

    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
            print()
        else:
            print(f"Book '{book}' not found in the library.")
            print()

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
            print()
        else:
            print("Books in the library:")
            for i in range(len(self.books)):
                print(f"{i+1}. {self.books[i]}")
                print()
            print(f"Total number of books in the library: {len(self.books)}")

    def search_book(self, book):
        for stored_book in self.books:
            if stored_book.lower() == book.lower():
                print(f"'{stored_book}' is available.")
                return

        print("Book not found.")

            


library = Library()
choice = 0
while choice !=4:
    try:
        choice  = int(input("Enter your choice:\n1. Add Book\n2. Remove Book\n3. Display Books\n4. Search Book\n5. Exit\n"))
    except ValueError:
        print("Please enter a number.")
        print()
        
    if choice == 1:
        book = input("Enter the name of the book to add: ")
        print()
        library.add_books(book)

    elif choice == 2:
        book = input("Enter the name of the book to remove: ")
        print()
        library.remove_books(book)

    elif choice == 3:
        library.display_books()

    elif (choice == 4):
        book_to_search = input("Enter book name to search: ")
        library.search_book(book_to_search)


    elif choice == 5:
        print("Exiting the program.")
        print()

        exit()

    else:
        print("Invalid choice. Please try again.")
        print()

    

    
        