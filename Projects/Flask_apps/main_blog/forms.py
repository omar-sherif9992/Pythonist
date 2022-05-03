from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, EqualTo, Length,Email
from flask_ckeditor import CKEditorField


##WTForm
class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # Notice body's StringField changed to CKEditorField
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[Email("This field requires a valid email address"),DataRequired(), Length(min=6, max=35)])
    password = PasswordField(label='New Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'),Length(min=6, max=35) ])
    confirm = PasswordField(label='Repeat Password')
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Submit")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[Email("This field requires a valid email address"),DataRequired(), Length(min=6, max=35)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField(label="Submit")

class CommentForm(FlaskForm):
    comment=CKEditorField("Comment",validators=[Length(min=6, max=35)])
    submit = SubmitField('Submit')
