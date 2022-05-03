import re

from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FileField,IntegerField
from wtforms.validators import DataRequired, URL, EqualTo, Length, Email, ValidationError
from flask_ckeditor import CKEditorField
from wtforms import SelectField
import pycountry
import phonenumbers
from flags import get_flags

class CheckoutForm(FlaskForm):
    credit_card_name = StringField(label="", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    credit_card_name = StringField(label="", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField(label="", validators=[Email("This field requires a valid Email Address"), DataRequired(),
                                              Length(min=6, max=35)], render_kw={"placeholder": "Email"})
    credit_card_number=StringField(label="",validators=[DataRequired()], render_kw={"placeholder": "Phone Number ex: +209996752223"})
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Register")
    checkbox = BooleanField(label="Remember Me")

    def validate_credit_card_number(self, credit_card_number):
        try:
            lst=[credit_card_number for credit_card_num in credit_card_number ]
            if len(lst) == 16:
                for i in range(0, len(lst)):
                    lst[i] = int(lst[i])
                # print(lst)
                last = lst[15]
                first = lst[:15]
                # print(first)
                # print(last)
                first = first[::-1]
                # print(first)
                for i in range(len(first)):
                    if i % 2 == 0:
                        first[i] = first[i] * 2
                    if first[i] > 9:
                        first[i] -= 9
                sum_all = sum(first)
                # print(first)
                # print(sum_all)
                t1 = sum_all % 10
                t2 = t1 + last
                if t2 % 10 is 0:
                    print("Valid Credit Card")
                else:
                    print("Invalid Credit Card!")
                    raise ValueError()

            else:
                print("Credit Card number limit Exceeded!!!!")
                raise ValueError()

        except ( ValueError):
          raise ValidationError('Invalid phone number')


class LoginForm(FlaskForm):
    email = StringField(label="", validators=[Email("This field requires a valid email address"), DataRequired(),
                                              Length(min=6, max=35)], render_kw={"placeholder": "Email"})
    password = PasswordField(label="", validators=[DataRequired(), Length(min=6, max=35)],
                             render_kw={"placeholder": " Password"})
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Login")
    checkbox = BooleanField(label="Remember Me")





class CountrySelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountrySelectField, self).__init__(*args, **kwargs)
        self.choices = [(country.alpha_2, country.name) for country in pycountry.countries]




class RegisterForm(FlaskForm):
    # image=FileField(label="Profile Image",render_kw={"placeholder": "Profile Image"})
    username = StringField(label="", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField(label="", validators=[Email("This field requires a valid Email Address"), DataRequired(),
                                              Length(min=6, max=35)], render_kw={"placeholder": "Email"})
    password = PasswordField(label="", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'),
                                                   Length(min=6, max=35)], render_kw={"placeholder": "New Password"})
    confirm = PasswordField(label="", render_kw={"placeholder": "Repeat Password"})
    country=CountrySelectField(label="Choose Your Country",validators=[DataRequired()], render_kw={"placeholder": "Choose Your Country"})
    phone=StringField(label="",validators=[DataRequired()], render_kw={"placeholder": "Phone Number ex: +209996752223"})
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Register")
    checkbox = BooleanField(label="Remember Me")

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')





