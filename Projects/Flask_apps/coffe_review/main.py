from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, BooleanField, validators, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
from decouple import config
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'public'
RECAPTCHA_PRIVATE_KEY = 'private'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# recaptcha-start
app.secret_key = 'secret_'
# app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = config("RECAPTCHA_PUBLIC_KEY")
app.config['RECAPTCHA_PRIVATE_KEY'] = config('RECAPTCHA_PRIVATE_KEY')


# app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
# recaptcha-start

# form-boxes
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location Goggle Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])

    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])

    power_rating = SelectField("Power Socket Availability",
                               choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    accept_rules = BooleanField('I accept the site rules', [DataRequired()])

    recaptcha = RecaptchaField(label="reCAPTCHA")

    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            with open("cafe-data.csv", mode="a") as csv_file:
                csv_file.write(f"\n{form.cafe.data},"
                               f"{form.location.data},"
                               f"{form.open.data},"
                               f"{form.close.data},"
                               f"{form.coffee_rating.data},"
                               f"{form.wifi_rating.data},"
                               f"{form.power_rating.data}")
            return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, size=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
