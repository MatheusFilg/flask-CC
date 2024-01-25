from app import app, db
from flask import render_template, url_for, request, redirect

from app.models import Contato
from app.forms import ContactForm

@app.route('/')
def homepage():
    usuario = 'Fulaninho'
    return render_template('index.html', usuario=usuario)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('contact.html', context=context, form=form)