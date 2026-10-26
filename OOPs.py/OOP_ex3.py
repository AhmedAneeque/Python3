'''
Write a Python program to create a Book class with a constructor that accepts the title, author
, and price of a book. Create functions to display the book details, apply a discount on the 
price, and display the final price. Create an object of the class and demonstrate all the 
functions.
'''

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        print("Book Details")

    def book_data(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print(f"Price with 10% discount: {round(self.price-(self.price*0.1))}")

b1=Book("Spiderman","annonymous",4000)
b1.book_data()

        