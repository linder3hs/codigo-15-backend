from flask import jsonify


def response(ok, data, status):
    return jsonify({
        "ok": ok,
        "data": data
    }), status


def response_success(data, status=200):
    return response(True, data, status)


def response_error(data, status=500):
    return response(False, data, status)


def generate_id(data):
    return len(data) + 1


def search_book(books, book_id):
    for book in books:
        if book.id == book_id:
            return book
    return None
