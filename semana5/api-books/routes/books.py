from flask import Blueprint, jsonify, request
from models.book import Book
from utils import response_error, response_success

books = Blueprint('books', __name__, url_prefix="/api/v1/books")

book = Book()


@books.route("/")
def get_books():
    return response_success(book.list_books())


@books.route("/", methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        book.insert_book(new_book)

        return response_success("Libro creado correctamente", 201)
    except Exception as e:
        return response_error(str(e))


@books.route("/<int:book_id>")
def get_book(book_id):
    try:
        searched = book.search_book_by_id(book_id)
        if not searched:
            return response_error("No se encontro el libro")
        return response_success(searched)
    except Exception as e:
        return response_error(str(e))


@books.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        json_from_postman = request.get_json()
        return response_success(book.update_book(book_id, json_from_postman))
    except Exception as e:
        return response_error(str(e))


@books.route("/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    try:
        return response_success(book.delete_book_by_id(book_id))
    except Exception as e:
        return response_error(str(e))
