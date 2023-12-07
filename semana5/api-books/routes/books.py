from flask import Blueprint, jsonify, request
from models.book import Book

books = Blueprint('books', __name__)

book = Book()


@books.route("/books")
def get_books():
    return jsonify(book.list_books())


@books.route("/books", methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        book.insert_book(new_book)

        return jsonify({"message": "Libro creado correctament"}), 201
    except Exception as e:
        return jsonify({"message": str(e)})


@books.route("/books/<int:book_id>")
def get_book(book_id):
    try:
        searched = book.search_book_by_id(book_id)
        print("searched", searched)
        return searched
    except Exception as e:
        return jsonify({"message": str(e)})
