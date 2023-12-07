from flask import Blueprint, jsonify, request
from models.book import Book

books = Blueprint('books', __name__)

book = Book()


@books.route("/books")
def get_books():
    return jsonify(book.list_books())


@books.route("/books", methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(**data)
    book.insert_book(new_book)

    return jsonify({"message": "Libro creado correctament"}), 201
