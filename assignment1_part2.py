
class Book:
    author = ''
    title = ''

    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author)


object1 = Book('J.K. Rowling', 'Harry Potter and the Goblet of Fire')
object2 = Book('Walter Scott', 'Ivanhoe:A Romance')

object1.display()
print()
object2.display()




