from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm
from app.models import Contact
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@app.route('/index/<name>', methods=['GET'])
def index(article1='MY HOBBIES', article2 ='MY GOAL'):
    return render_template('index.html', article1=article1, article2=article2, title='HOME')
#*************************************
#*************************************

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    # when form is submitted appends to post lists, re-render posts page
    if form.validate_on_submit():
        info = form.info.data
        contact = Contact(info=info)

        # add post variable to database stage, then commit
        db.session.add(contact)
        db.session.commit()

        return redirect(url_for('contact'))

    info = Contact.query.all()

    return render_template('contact.html', title='Contact', form=form, info=info)

# @app.route('/title', methods=['GET', 'POST'])
# def title():
#     form = TitleForm()
#
#     # when form is submitted, rediret to home page, and pass itle to change what the h1 tag says
#     if form.validate_on_submit():
#         header = form.title.data
#         return redirect(url_for('index', header=header))
#*************************************
