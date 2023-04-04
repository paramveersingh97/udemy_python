class Book:
    TYPES = ("hardcover","paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls,name,page_weight):
        # return Book(name, Book.TYPES[0], page_weight + 100)    #cls and classname are interchangable
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls,name,page_weight):
        # return Book(name, Book.TYPES[1], page_weight)    #cls and classname are interchangable
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 900)
print(book)
book2 = Book.paperback("Essays",200)
print(book2)