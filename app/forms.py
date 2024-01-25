from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from app.models import Contato
from app import db

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