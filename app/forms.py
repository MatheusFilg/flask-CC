from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Contato, User
from app import db, bcrypt

class ContactForm(FlaskForm):
    name= StringField('name', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired(), Email()])
    message= StringField('message', validators=[DataRequired()])
    subject= StringField('subject', validators=[DataRequired()])
    btn_submit= SubmitField('submit')

    def save(self):
        contato = Contato(
            name= self.name.data,
            email= self.email.data,
            message= self.message.data,
            subject= self.subject.data,
        )
        db.session.add(contato)
        db.session.commit()

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    btn_submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter().first():
            return ValidationError('Email already been taken')
    
    def save_user(self):
        password = bcrypt.generate_password_hash(self.password.data.encode('utf-8'))
        user = User(
            name = self.name.data,
            email = self.email.data,
            password = password,
        )
        db.session.add(user)
        db.session.commit()
        return user
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    btn_submit = SubmitField('Login')

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, self.password.data.encode('utf-8')):
                return user
            else:
                raise Exception('Wrong Password')
        else:
            raise Exception('User not found')