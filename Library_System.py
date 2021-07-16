class Library:

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lenddict = {}

    def display_book(self):
        print(f"Books which is available in the the library name ({self.library_name}) is ")
        for book_name in self.list_of_books:
            print("⚫", book_name)

    def lend_book(self, book_name, user):
        if book_name not in self.lenddict.keys():
            self.lenddict.update({book_name: user})
            print(f"Update!!! Lender Book Database is updated\nNow you can take your book ")
        else:
            print(f"Already taken by {self.lenddict[book_name]}\nNot available in Library ")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        print(f"New Book is added in the Library ")

    def return_book(self, book_name):
        self.lenddict.pop(book_name)


if __name__ == '__main__':
    CMRSports = Library(["No spin", "Playing it my way", "The test of my life", "At the close of the play",
                         "AB:The Autobiography", "Rahul Dravid: Timeless Steel"], "CMRIT")
    print(f"Welcome to Library {CMRSports.library_name}")
    while True:
        print("\nEnter your choice ")
        print("1.Display\n2.Lend Book\n3.Add Book\n4.Return Book")
        opt = input()
        if opt not in ['1', '2', '3', '4']:
            print("😞 Please enter a valid option 😞")
            continue
        else:
            opt = int(opt)
        if opt == 1:
            CMRSports.display_book()
        elif opt == 2:
            book_name = input("Enter the book name you want to lend: ")
            user = input("Enter your name macha: ")
            CMRSports.lend_book(book_name, user)
        elif opt == 3:
            book_name = input("Enter the book name you want to Add: ")
            CMRSports.add_book(book_name)
        elif opt == 4:
            book_name = input("Enter the book name you want to return: ")
            CMRSports.return_book(book_name)

        print("Press Q to quit OR C to continue")

        opt1 = ""
        while (opt1 != "q" and opt1 != "c") or (opt1 != "q" and opt1 != "c"):
            opt1 = input()
            if opt1 == "q" or "Q":
                break
            elif opt1 == "C" or "c":
                continue
