from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField, FileRequired

class AddProduct(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    price = IntegerField("Product Price", validators=[DataRequired()])
    image_url = StringField("Image")
    image = FileField("Image", validators=[FileRequired()])
    text = StringField("Description")
    submit = SubmitField("Submit")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", 
                                      validators=[DataRequired(), Length(min=8), EqualTo("password", message="Passwords Must Match")])
    receive_updates = BooleanField("Receive news and updates", default=True)
    terms = BooleanField("I agree to the terms and privacy policy", validators=[DataRequired()]) 
    submit = SubmitField("Sign up")

class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
