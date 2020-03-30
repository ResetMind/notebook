from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, NoteForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Note
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    all_notes = []
    notes = user.notes.all()
    for n in notes:
        all_notes.append({'id': n.id, 'header': n.header, 'body': n.body})
    print(all_notes)
    return render_template('index.html', title='Home', notes=notes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def note(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = NoteForm()
    if form.validate_on_submit():
        n = Note(header=form.header.data, body=form.body.data, author=user)
        db.session.add(n)
        db.session.commit()
        flash('Saved')
        all_notes = []
        notes = user.notes.all()
        for n in notes:
            all_notes.append({'id': n.id, 'header': n.header, 'body': n.body})
        return render_template('index.html', title='Home', notes=notes)
    return render_template('note.html', form=form)


@app.route('/user/<username>/edit/<id>', methods=['GET', 'POST'])
@login_required
def note_edit(username, id):
    user = User.query.filter_by(username=username).first_or_404()
    if user != current_user:
        return redirect(url_for('index'))
    note = Note.query.filter_by(id=id, author=user).first_or_404()
    print(note)
    form = NoteForm(header=note.header, body=note.body)
    if form.validate_on_submit():
        note.header = form.header.data
        note.body = form.body.data
        db.session.commit()
        flash('Saved')
        all_notes = []
        notes = user.notes.all()
        for n in notes:
            all_notes.append({'id': n.id, 'header': n.header, 'body': n.body})
        return render_template('index.html', title='Home', notes=notes)
    return render_template('note.html', form=form)
