from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, SubmitField, validators,IntegerField
from wtforms.validators import DataRequired,InputRequired,EqualTo
from decouple import config
from flask_bootstrap import Bootstrap

MY_EMAIL=config("MY_EMAIL")
MY_PASSWORD=config("MY_PASSWORD")

app = Flask(__name__)
Bootstrap(app) #After loading, new templates are available to derive from in your templates.
csrf=CSRFProtect(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Length(min=10, max=30),DataRequired(),validators.Email(granular_message=True)])
    age = IntegerField('Age', [validators.NumberRange(min=18, max=70)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Password must match confirm Password'),validators.Length(min=8, max=30),DataRequired()])
    confirm = PasswordField('Repeat Password',validators=[InputRequired(),DataRequired()])
    submit=SubmitField(label='Log in')
    # date=DateTimeField("Birth-Date day/month/year",validators=[DataRequired()])

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods=["GET","POST"])

def login():
    login_form = LoginForm()
    login_form.validate_on_submit()# this makes the form not to complete till the user enter correct format data
    if request.method == "POST":
        print(login_form.email.data)
        print(login_form.password.data)
        if str(login_form.email.data)==MY_EMAIL and str(login_form.password.data)==MY_PASSWORD and login_form.age.data==20:
            return render_template("success.html")
        else:
            return render_template("denied.html")


    return render_template("login2.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
