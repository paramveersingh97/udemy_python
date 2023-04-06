class TooManyPagesReadError(ValueError):
    pass
        

class Book:
    def __init__(self, name: str, pages_count: int):
        self.name = name
        self.pages_count = pages_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    def read(self,pages: int):
        if self.pages_read + pages >  self.pages_count:
            raise TooManyPagesReadError(f"You tried to read {self.pages_read + pages} but this book has only {self.pages_count} pages.")
        
        self.pages_read = self.pages_read + pages
        print(f"You have now read {self.pages_read} pages out of {self.pages_count}")

python101 = Book("Python101", 500)
try:
    python101.read(500)
    python101.read(1000)
except TooManyPagesReadError as e:
    print(e)