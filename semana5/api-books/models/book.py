from utils import generate_id, search_book


class Book:
    books = []

    def __init__(self, title=None, isbn=None, author=None, description=None, summary=None, image_url=None):
        self.id = None
        self.title = title
        self.isbn = isbn
        self.author = author
        self.description = description
        self.summary = summary
        self.image_url = image_url

    def list_books(self):
        return [item.to_json() for item in self.books]

    def search_book_by_id(self, book_id):
        book_searched = search_book(self.books, book_id)

        if book_searched is not None:
            return book_searched.to_json()
        return None

    def insert_book(self, book):
        book.id = generate_id(self.books)
        self.books.append(book)

    def update_book(self, book_id, json_from_postman):
        book_searched = search_book(self.books, book_id)

        if book_searched is None:
            return "Libro no encontrado"

        # si no actualiza la info
        book_searched.title = json_from_postman.get("title", book_searched.title)
        book_searched.author = json_from_postman.get("author", book_searched.author)
        book_searched.isbn = json_from_postman.get("isbn", book_searched.isbn)
        book_searched.image_url = json_from_postman.get("image_url", book_searched.image_url)
        book_searched.summary = json_from_postman.get("summary", book_searched.summary)
        book_searched.description = json_from_postman.get("description", book_searched.description)

        return book_searched.to_json()

    def delete_book_by_id(self, book_id):
        current_book = search_book(self.books, book_id)
        try:
            self.books.remove(current_book)
            return 'Eliminado correctamente'
        except Exception as e:
            return str(e)

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
