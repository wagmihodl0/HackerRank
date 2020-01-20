from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Inside Book constructor")

    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        print("Inside MyBook Constructor")

    def display(self):
        print("Entered display() function")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
