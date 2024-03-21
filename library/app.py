from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def save_to_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

users = []
books = []

@app.route('/')
def index():
    return render_template('index.html', users=users, books=books)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_name = request.form['user_name']
        users.append(user_name)
        save_to_json('users.json', users) 
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_title = request.form['book_title']
        books.append(book_title)
        save_to_json('books.json', books)  
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == '__main__':
  
    users = load_from_json('users.json')
    books = load_from_json('books.json')
    app.run(debug=True)
