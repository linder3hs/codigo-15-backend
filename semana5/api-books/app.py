from flask import Flask
from routes.books import books

# instancia de flask
app = Flask(__name__)


app.register_blueprint(books)


if __name__ == "__main__":
    app.run(debug=True)
