from app import app, db
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

from app.models import Contato, Post
from app.forms import ContactForm, UserForm, LoginForm, PostForm, CommentForm

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

@app.route('/post/new/', methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        form.save_post(current_user.id)
        return redirect(url_for('homepage'))
    return render_template('new_post.html', form=form)

@app.route('/post/list',methods=['GET','POST'])
def post_list():
    posts = Post.query.all()
    return render_template('post_list.html', posts=posts)


@app.route('/post/<int:id>',methods=['GET','POST'])
def post(id):
    post = Post.query.get(id)
    form = CommentForm()
    if form.validate_on_submit():
        form.save_post(current_user.id, post.id)
        return redirect(url_for('post', id=id))
    return render_template('post.html', post=post, form=form)