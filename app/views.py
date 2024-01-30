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

@app.route('/contact/<int:id>/')
def contact_detail(id):
    obj = Contato.query.get(id)

    return render_template('contact_detail.html', obj=obj)

@app.route('/contact/list/')
def contact_list():

    if request.method == 'GET':
        search = request.args.get('search', '')
    data = Contato.query.order_by('name')
    if search != '':
        data = data.filter_by(name=search)

    context = {'data': data.all()}

    return render_template('contact_list.html', context=context)