from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_title = request.form['book_title']
        books.append(book_title)
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
