from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, \
    fresh_login_required,confirm_login

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()


@app.route('/')
def home():
    logout_user()
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=12)
        flag = False
        try:
            user = User(email=email, name=name, password=password)
            db.session.add(user)
            db.session.commit()
            flag = True
        except:
            return render_template("register.html", condition="Used Email")
        if flag:
            login_user(user)
            return redirect(url_for("secrets"))


    return render_template("register.html", condition="registering",logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user == None:
            return render_template("login.html", condition="Invalid Email",logged_in=current_user.is_authenticated)
        elif not check_password_hash(user.password, password):
            return render_template("login.html", condition="Invalid Password",logged_in=current_user.is_authenticated)
        else:
            login_user(user)
            return redirect(url_for("secrets"))
    return render_template("login.html", condition="logging in",logged_in=current_user.is_authenticated)



@app.route('/secrets')
@login_required
@fresh_login_required
def secrets():
    return render_template("secrets.html", name=current_user.name,logged_in=current_user.is_authenticated)



@app.route('/logout')
@fresh_login_required
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods=['GET'])
@login_required
def download():
    return send_from_directory(app.static_folder,
                               'files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
