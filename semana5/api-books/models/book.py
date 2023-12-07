class Book:
    books = []

    def __init__(self, title=None, isbn=None, author=None, description=None, summary=None, image_url=None):
        self.id = id(isbn)
        self.title = title
        self.isbn = isbn
        self.author = author
        self.description = description
        self.summary = summary
        self.image_url = image_url

    def list_books(self):
        return [item.to_json() for item in self.books]

    def search_book_by_id(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return book
        return None

    def insert_book(self, book):
        self.books.append(book)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn,
            "author": self.author,
            "description": self.description,
            "summary": self.summary,
            "image_url": self.image_url
        }
