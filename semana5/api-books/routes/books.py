from flask import Blueprint, jsonify, request
from models.book import Book

books = Blueprint('books', __name__, url_prefix="/api/v1/books")

book = Book()


@books.route("/")
def get_books():
    return jsonify(book.list_books())


@books.route("/", methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        book.insert_book(new_book)

        return jsonify({"message": "Libro creado correctamente"}), 201
    except Exception as e:
        return jsonify({"message": str(e)})


@books.route("/<int:book_id>")
def get_book(book_id):
    try:
        searched = book.search_book_by_id(book_id)
        if not searched:
            return jsonify({"message": "No se encontro el libro"})
        return searched
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@books.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        json_from_postman = request.get_json()
        return jsonify({"message": book.update_book(book_id, json_from_postman)})
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@books.route("/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    try:
        return jsonify({"message": book.delete_book_by_id(book_id)})
    except Exception as e:
        return jsonify({"message": str(e)}), 500
