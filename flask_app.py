from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

def load_books():
    with open('/home/dushr/mysite/books.json', 'r') as file:
        return json.load(file)

@app.route('/books', methods=['GET'])
def get_books():
    print(os.getcwd())
    books = load_books()
    genre = request.args.get('genre')
    publish_year = request.args.get('publish_year', type=int)

    if genre:
        books = [book for book in books if book['genre'].lower() == genre.lower()]

    if publish_year:
        books = [book for book in books if book['publish_year'] == publish_year]

    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)