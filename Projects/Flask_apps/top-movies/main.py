from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired, InputRequired, EqualTo
import requests
from decouple import config

TMDB_API_KEY = config('TMDB_API_KEY')
TMDB_API_URL = "https://api.themoviedb.org/3/movie/550"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # if you get a deprecation warning in the console that's related to SQL_ALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)


# Create a sheet
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.String(250), nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)


# db.session.add(new_movie)
# db.session.commit()

class UpdateForm(FlaskForm):
    review = StringField(label='Your Review :', validators=[DataRequired()])
    rating = StringField('Your Rating out of 10 e.g.7.5', [DataRequired()])
    submit = SubmitField(label='Submit')


class NewMovieForm(FlaskForm):
    title = StringField(label='Movie Name :', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    delete_id = request.args.get("id")
    if delete_id != None and int(delete_id) > 0:
        movie_to_delete = Movie.query.get(delete_id)
        if movie_to_delete != None:
            print(f" {movie_to_delete} is deleted ! ")
            db.session.delete(movie_to_delete)
            db.session.commit()
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", size=len(all_movies), all_movies=all_movies)


@app.route("/edit", methods=["POST", 'GET'])
def edit():
    update_form = UpdateForm()
    id = request.args.get("id")
    if update_form.validate_on_submit() and request.method == "POST":  # this makes the form not to complete till the user enter correct format data
        rating = str(request.form["rating"])
        review = request.form["review"]
        try:
            if not (float(rating) >= 0 and float(rating) <= 10) or review == "":
                raise Exception
        except:
            return render_template('edit.html', form=update_form, condition=1)

        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=update_form, condition=0)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    movie_form = NewMovieForm()
    if movie_form.validate_on_submit():
        movie_title = movie_form.title.data
        response = requests.get(url=MOVIE_DB_SEARCH_URL, params={"api_key": TMDB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        if data == None or data == []:
            return render_template("add.html", form=movie_form, condition=1)

        return render_template("select.html", options=data)
    return render_template("add.html", form=movie_form, condition=0)


@app.route("/find")
def movie_info():
    id = request.args.get('id')
    url = f"{MOVIE_DB_INFO_URL}/{id}"
    data = requests.get(url=url, params={"api_key": TMDB_API_KEY, "language": "en-US"}).json()
    image_url = f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}"
    new = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=image_url,
        description=data["overview"],
    )
    db.session.add(new)
    db.session.commit()
    return redirect(url_for("edit", id=new.id))


if __name__ == '__main__':
    app.run(debug=True)
