class library:
    def __init__(self, books):
        self.books=books
        
    def display_available_books(self):
        print('Books present in this library are: ')
        for books in self.books:
            print("\t", books)
            
    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} book")
            self.books.remove(bookname)
            return True
        else:
            print("sorry, This book has been already been issued to someone else")
            return False
            
    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this books")
        
class student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returnbook(self):
        self.book=input ("Enter the name of the book which you want to return: ")

lib=library(['Python', 'Java', 'C++', 'django', 'Flask', 'DSA', 'operating system', 'DBMS', ])
stud= student()

while (True):
    welcomemsg='''\n\n**************Welcome to the Library****************
    1. Listing all the books
    2. Request a book
    3. Return a book
    4. Exit
    '''
    print(welcomemsg)
    a = int(input("Enter the choice: "))
    if a == 1:
        lib.display_available_books()
    elif a == 2:
        lib.borrowBook(stud.requestbook())
    elif a == 3:
        lib.returnbook(stud.returnbook())
    elif a == 4:
        exit()
    else:
        print("Invalid choice")
   