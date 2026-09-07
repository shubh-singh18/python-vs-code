# 8. Library Management System — Classes + Encapsulation

# Create:
# - Book class
# - Member class
# - Library class

# Requirements:
# - A book should have title, author, and availability status.
# - A member should be able to borrow a book.
# - A member should be able to return a book.
# - Book availability should be encapsulated.
# - A book cannot be borrowed if it is already borrowed


class book:
    def __init__(self,book_name,stock):
        self.book=book_name
        self.stock=stock

class member(book):
    def issue(self,book):
        self.issue_book=book
        if self.issue_book in self.book and self.stock>0:
            print(f"you issued the book{self.book}succssfully")
        else:
            print("this book is not available")

    def return_book(self,book_name):
        self.book_return=book_name
        print(f"you returned the book {self.book_return}successfully")
class library(book):
    def search(self,book_title):
        self.search_book=book_title
        if self.search_book in self.book and self.stock>0:
            print("this book is available in stock")
        else:
            print("this is not in our stock")

m=member("abc",45)
m1=member("bcd",34)
m2=member("xyz",23)
m.issue("abc")
m.return_book("bcd")
l=library("vhj",78)
l.search("bcd")