from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm, LoginForm, RegisterForm
from app.models import Contact, User # Post
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
@app.route('/index/<name>', methods=['GET'])
def index(article1='MY HOBBIES', article2 ='MY GOAL'):
    form = ContactForm()
    return render_template('index.html', form=form, article1=article1, article2=article2, title='HOME')
#*************************************
#*************************************

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    # when form is submitted appends to post lists, re-render posts page
    if form.validate_on_submit():
        contact = Contact(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data
        )

        db.session.add(contact)
        db.session.commit()
        flash('Thank you for your contact information!')
        return redirect(url_for('contact'))

    return render_template('contact.html', title='Contact', form=form)

#*************************************
# ***** post *****
# @login_required #decorator
# @app.route('/posts/<username>', methods=['GET', 'POST'])
# def posts(username):
#     form = PostForm()
#     # query database for proper person
#     person = User.query.filter_by(username=username).first()
#     # when form is submitted appends to post lists, re-render posts page
#     if form.validate_on_submit():
#         tweet = form.tweet.data
#         post = Post(tweet=tweet, user_id=current_user.id)
#         # add post variable to database stage, then commit
#         db.session.add(post)
#         db.session.commit()
#
#         return redirect(url_for('posts', username=username))
#
#     # tweets = Post.query.all()
#     return render_template('posts.html', person=person, title='Posts', form=form, username=username) #tweets=tweets,

# ***** title *****
# @app.route('/title', methods=['GET', 'POST'])
# def title():
#     form = TitleForm()
#     # when form is submitted, rediret to home page, and pass itle to change what the h1 tag says
#     if form.validate_on_submit():
#         header = form.title.data
#         return redirect(url_for('index', header=header))
#
#     return render_template('title.html', title='Title', form=form )

# ***** login *****
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = LoginForm()

    # check if form is submitted, log user in if so
    if form.validate_on_submit():
        #
        user = User.query.filter_by(username=form.username.data).first()
        # if user doesn't exit current page
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))
        # if user does exist, and credentials are correct, log them in and send them to their profile page
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in!')
        return redirect(url_for('index'))

    return render_template('login.html', title='Login', form=form)

# ***** register *****
@app.route('/register', methods=['GET', 'POST'])
def register():
    #
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            url = form.url.data,
            age = int(form.age.data),
            bio = form.bio.data,
        )

        # set the password hash
        user.set_password(form.password.data)

        # add to stage and commit to db, then flash and return
        db.session.add(user)
        db.session.commit()
        flash('Congratulation, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

# ***** logout *****
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#*************************************
