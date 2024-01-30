from app import app, db
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user

from app.models import Contato
from app.forms import ContactForm, UserForm, LoginForm

@app.route('/', methods=['GET','POST'])
def homepage():
    usuario = 'Fulaninho'
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('index.html', usuario=usuario, form=form)

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

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save_user()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('register.html', form=form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))