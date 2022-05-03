import html
import re
from datetime import datetime
from functools import wraps
import requests
import stripe
from werkzeug.utils import secure_filename
from Projects.Notification.email_manager import EmailManager
from flask import Response, Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
import calendar
from flask_gravatar import Gravatar
from forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, \
    fresh_login_required
from flask_mail import Mail,Message
from sqlalchemy import Table, Column, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os
from datetime import timedelta
from itsdangerous import URLSafeTimedSerializer,SignatureExpired,BadTimeSignature

#Loading My Keys
load_dotenv()
RECAPTCHA_PRIVATE_KEY=os.environ.get("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_PUBLIC_KEY= os.environ.get("RECAPTCHA_PUBLIC_KEY")
APP_SECRET_KEY=os.environ.get("SECRET_KEY")
CHECKOUT_PUBLIC_KEY=os.environ.get('PUBLISHABLE_API_KEY')
CHECKOUT_SECRET_KEY=os.environ.get('SECRET_API_KEY')
MY_EMAIL=os.environ.get('MY_EMAIL')


#App Configuration
app = Flask(__name__)
app.config["SECRET_KEY"] = APP_SECRET_KEY
app.config["RECAPTCHA_PUBLIC_KEY"] = RECAPTCHA_PUBLIC_KEY
app.config["RECAPTCHA_PRIVATE_KEY"] = RECAPTCHA_PRIVATE_KEY
app.config["REMEMBER_COOKIE_DURATION"]=timedelta(seconds=3.154e+7) #For a Year
app.config.from_pyfile('config.cfg')
app.config['STRIPE_PUBLIC_KEY']=CHECKOUT_PUBLIC_KEY
app.config['STRIPE_SECRET_KEY']=CHECKOUT_SECRET_KEY
stripe.api_key=os.environ.get('SECRET_API_KEY')


Bootstrap(app)
ckeditor = CKEditor(app)

#Email verfication configuration
mail=Mail(app)
serializer=URLSafeTimedSerializer(APP_SECRET_KEY)



# Database Connection
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///BestBuy.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.app = app
db.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,unique=True, primary_key=True)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    country=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(100),unique=True, nullable=False)
    username = db.Column(db.String(1000),nullable=False)
    verified=db.Column(db.Boolean(),nullable=False)
    wish_list = db.relationship("WishList", backref="user")
    user_pic=db.relationship("UserPicture", backref="user")
    comments = db.relationship("Comment", backref="user")


class UserPicture(db.Model):
    """User picture model."""
    __tablename__ = 'user_picture'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    pic_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f'Pic Name: {self.name} Data: {self.data} text: {self.text} created on: {self.pic_date} location: {self.location}'



class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date=db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class WishList(db.Model):
    __tablename__ = "wish_list"
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.Text, nullable=False)
    date=db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# Creates the logs tables if the db doesnt already exist
with app.app_context():
    db.create_all()


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message="You can't access that Page, You need to login first."
login_manager.refresh_view='login'
login_manager.needs_refresh_message="You need to login again!"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    """For Login Required Pages"""
    flash(message="First Login Please")
    return redirect(url_for("loginPage"))

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


#avatar builder
gravatar = Gravatar(app, size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

#Admin-check
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return render_template("error404.html")
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error404.html'), 404



#Home Page
@app.route("/")
def homePage():
    return render_template("homePage.html",logged_in=current_user.is_authenticated)

#Login Page
@app.route("/login",methods=["GET","POST"])
def loginPage():
    login_form=LoginForm()
    if request.method=="POST" and login_form.validate_on_submit():
        remember = login_form.checkbox.data
        print(remember)
        email = str(login_form.email.data).lower()
        password=login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user == None:
            flash("Invalid Email")
            return render_template('loginPage.html',form=login_form,logged_in=current_user.is_authenticated
                                   )
        elif check_password_hash(user.password, password):
            login_user(user,remember=remember)
            return redirect(url_for("homePage"))
        else:
            flash("Invalid Password")
            return render_template('loginPage.html',form=login_form,logged_in=current_user.is_authenticated)
    return render_template('loginPage.html', form=login_form, logged_in=current_user.is_authenticated)


def perfect_password(inputString:str)->bool:
    """Checks if the password contains  digits and uppercase letter"""
    return any(char.isdigit() for char in inputString) and any(char.isupper() for char in inputString)

def check_email(email_address:str)-> bool:
    """Email Validator that checks if it was real email or No"""
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': email_address.lower()})
    status = response.json()['status']
    if status == "valid":
        return True
    else:
        return False

@app.route("/register",methods=["GET","POST"])
def registerPage():
    register_form = RegisterForm()
    if request.method=="POST" and register_form.validate_on_submit():
        username = str(register_form.username.data)
        email = str(register_form.email.data)
        phone=str(register_form.phone.data)
        country=str(register_form.country.data)
        print(username)
        try:

            if (not check_email(email_address=email)):
                flash("Email does not Exists")
                return redirect(url_for('registerPage'))

            if (not perfect_password(register_form.password.data)):
                flash("Password must contain numbers and uppercase")
                return redirect(url_for('registerPage'))

            hash_and_salted_password = generate_password_hash(
                register_form.password.data, method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email=email.lower(),
                username=username.lower(),
                password=hash_and_salted_password,
                phone=phone,
                country=country,
                verified=False
            )
            print(new_user)
            db.session.add(new_user)
            db.session.commit()
            print('user added')
            f = request.files['file']
            if f != "":
                filename = secure_filename(f.filename)
                mimetype = f.mimetype
                if not filename or not mimetype:
                    pass
                else:

                    newFile = UserPicture(user=new_user,img=f.read(), name=filename, mimetype=mimetype)
                    db.session.add(newFile)
                    db.session.commit()
                    print('image uploaded')
        except:
            # Send flash messsage
            flash("You've already signed up before, log in instead!")
            return redirect(url_for("loginPage"))
        #For remember me
        remember =register_form.checkbox.data
        login_user(user=new_user, remember=remember)
        #for email-verification
        token=serializer.dumps(email,salt='email-confirm')
        msg=Message('Confirm Email',sender=MY_EMAIL,recipients=[email])
        link=url_for('verify_email',token=token,id=new_user.id,_external=True)
        msg.body=f"Please open this link to verify your email:\n {link} "
        mail.send(msg)
        flash("Email is sent ,please verify your Email")
        return redirect(url_for("homePage"))
    return render_template("registerPage.html", form=register_form, logged_in=current_user.is_authenticated)


@app.route('/verifyemail',methods=["GET","POST"])
def verify_email():
    """Email verification page with a token that expires in an hour"""
    id=request.args['id']
    token=request.args['token']
    try:
        email=serializer.loads(token,salt='email-confirm',max_age=3600)
        user = User.query.filter_by(id=id).first()
        if request.method=="POST":
            user.verified=True
            print("fd")
            db.session.commit()
            login_user(user)
            flash("Email is Verified")
            return redirect(url_for('homePage'))
        print(id)
        return render_template('email-verified.html',name=user.username,id=id,token=token)
    except :
        #means token expired
        flash("Token Expired")
        return render_template('error404.html')


@fresh_login_required
@app.route("/buy-product/<int:id>")
def buyProductPage(id:int):
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route('/<int:id>')
def get_img(id):
    img = UserPicture.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)



@app.route('/checkout')
def checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1JbAgBJ7jm9XcHmJTNp2mbuk', #price id
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('thanksPage', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('homePage', _external=True),
    )
    return render_template("trial.html",checkout_session_id=session['id'],checkout_public_key=CHECKOUT_PUBLIC_KEY)



@app.route('/thanks')
def thanksPage():
    return render_template('thanksPage.html')
@app.route('/Privacy&Policy')
def Privacy_Policy():
    return render_template('Privacy-Policy.html')
if __name__=="__main__":
    app.run(debug=True)