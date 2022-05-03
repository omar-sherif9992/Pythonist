from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #if you get a deprecation warning in the console that's related to SQL_ALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    delete=request.args.get("id")
    print(f"del {delete}")
    if delete!=None and int(delete)>0:
        book_to_delete=Book.query.get(delete)
        print(book_to_delete)
        if book_to_delete!=None:
            db.session.delete(book_to_delete)
            db.session.commit()
    all_books=db.session.query(Book).all()
    if len(all_books)!=0:
        print(all_books[0].id)
    return  render_template("index.html",all_books=all_books,size=len(all_books))


@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        try:
            author=str(request.form["author"])
            rating=float(request.form["rating"])
            book_name=str(request.form["book_name"])
        except:
            return render_template("add.html",condition=1)

        try:

            new_book=Book(author=author,rating=rating,title=book_name)
            db.session.add(new_book)
            db.session.commit()
        except:
            return render_template("add.html", condition=3)


        return render_template("add.html", condition=2)

    return render_template("add.html",condition=0)

@app.route("/edit",methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    id_num=request.args.get('id')
    # book_selected = Book.query.filter_by(id=id_num).first()
    book_selected = Book.query.get(id_num)
    return render_template("edit_rating.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)

