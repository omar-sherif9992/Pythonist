import html
import re
from datetime import datetime
from functools import wraps
from Projects.Notification.email_manager import EmailManager
from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
import calendar
from flask_gravatar import Gravatar
from forms import PostForm, RegisterForm, LoginForm, CommentForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, \
    fresh_login_required, confirm_login
from decouple import config
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# posts = requests.get("https://api.npoint.io/67e63bfb1de5467da49f").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['RECAPTCHA_PUBLIC_KEY'] = config("RECAPTCHA_PUBLIC_KEY")
app.config['RECAPTCHA_PRIVATE_KEY'] = config('RECAPTCHA_PRIVATE_KEY')

gravatar = Gravatar(app, size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    flash(message="First Login Please")
    return redirect(url_for("login_user_page"))


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users-blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    _tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    posts = db.relationship("BlogPost", backref="user")
    comments = relationship("Comment", backref="user")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date=db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


##CONFIGURE TABLE in DB
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    # Create reference to the User object, the "posts" refers to the posts property in the User class.
    img_url = db.Column(db.String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db.create_all()
@app.route('/')
def get_all_posts():
    ADMIN_USER = User.query.filter_by(id=1).first()
    posts = ADMIN_USER.posts
    print(posts)
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


@app.route("/delete/<int:index>")
@login_required
@admin_only
def delete_post(index):
    requested_post = BlogPost.query.get(index)
    db.session.delete(requested_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


def remove_tags(raw_html):
    raw_html = raw_html.replace("<p>&nbsp;</p>", "")
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    if "&nbsp;" in cleantext:
        cleantext = cleantext.replace("&nbsp;", "")

    return html.unescape(cleantext)


@app.route("/post/<int:index>", methods=["GET", "POST"])
def show_post(index):
    comment_form = CommentForm()
    requested_post = BlogPost.query.get(index)
    comment = ((str(comment_form.comment.data)).replace("<p>&nbsp;</p>", "")).strip()
    text = (remove_tags(str(comment))).strip()

    if request.method == "POST" and (comment_form.comment != None and comment != "" and len(text) > 0):
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login_user_page"))
        month = calendar.month_name[datetime.now().month]
        day = datetime.now().day
        year = datetime.now().year
        date = f"{month} {day},{year}"
        db.session.add(Comment(user=current_user, text=comment,date=date))
        db.session.commit()

        comment_form.comment.data = ""

    comments = Comment.query.all()
    comments=comments[::-1]
    print(comments)
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, form=comment_form,
                           comments=comments)


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


@app.route("/forum_entry", methods=["POST"])
@login_required
def login():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    phone = request.form["phone"]
    email_message = f"name: {name} \n" \
                    f"email: {email} \n" \
                    f"phone: {phone} \n\n" \
                    f"message: {message}\n"
    email_manager = EmailManager()
    email_manager.send_email(title="Omar's Blog Contact Forum", message=email_message + "message is recieved",
                             to_addrs=email, first_name=name, last_name="")
    email_manager.send_email(title="Omar's Blog Contact Forum", message=email_message + "message is recieved",
                             to_addrs="omar.sherif9991@gmail.com", first_name=name, last_name="")
    return render_template("message_sent.html", logged_in=current_user.is_authenticated)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
@login_required
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)

    post_form = PostForm(title=post.title,
                         subtitle=post.subtitle,
                         img_url=post.img_url,
                         body=post.body)
    if post_form.validate_on_submit() and request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        img_url = request.form['img_url']
        body = request.form['body']
        post.body = body
        post.subtitle = subtitle
        post.title = title
        post.img_url = post.img_url

        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, condition=1, logged_in=current_user.is_authenticated)


@app.route("/new-post", methods=["GET", "POST"])
@login_required
@admin_only
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit() and request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        img_url = request.form['img_url']
        body = request.form['body']
        month = calendar.month_name[datetime.now().month]
        day = datetime.now().day
        year = datetime.now().year
        date = f"{month} {day},{year}"
        ADMIN_USER = User.query.filter_by(id=1).first()
        post = BlogPost(title=title,
                        subtitle=subtitle,
                        date=date,
                        body=body,
                        img_url=img_url, user=ADMIN_USER
                        )
        print(post.title)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, condition=0, logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    resgister_forum = RegisterForm()
    if resgister_forum.validate_on_submit() and request.method == "POST":
        email = resgister_forum.email.data
        name = resgister_forum.name.data
        try:
            hash_and_salted_password = generate_password_hash(
                resgister_forum.password.data, method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email=email.lower(),
                name=name,
                password=hash_and_salted_password,
            )

            db.session.add(new_user)
            print(email)
            db.session.commit()
        except:
            # Send flash messsage
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login_user_page"))
        login_user(user=new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=resgister_forum, condition="", logged_in=current_user.is_authenticated)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    print(current_user.is_authenticated)
    return redirect(url_for('get_all_posts'))


@app.route("/login_user_page", methods=["GET", "POST"])
def login_user_page():
    login_form = LoginForm()
    if login_form.validate_on_submit() and request.method == "POST":
        email = (login_form.email.data).lower()
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user == None:
            return render_template('login.html', form=login_form, logged_in=current_user.is_authenticated,
                                   condition="Invalid Email")
        elif check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        else:
            return render_template('login.html', form=login_form, logged_in=current_user.is_authenticated,
                                   condition="Invalid Password")

    return render_template('login.html', form=login_form, logged_in=current_user.is_authenticated, condition="")




if __name__ == "__main__":
    app.run(debug=True)
