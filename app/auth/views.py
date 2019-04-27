from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from ..email import mail_message 




@auth.route('/login',methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_email = form.email.data
        user_pass = form.password.data
        rem = form.remember_me.data

        user = User.query.filter_by(email = user_email).first()
    if user is not None and user.verify_password(login_form.password.data):
        login_user(user,login_form.remember.data)
        flash ("Welcome!")
        return redirect(request.args.get('next') or url_for('main.index'))
     
    flash('Invalid username or Password')

    title = "60 seconds login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():   
        name = form.username.data
        email = form.email.data
        pass_sec = form.password.data
        profile_pic = "photos/download.png"
        bio = ""
        new_user = User(name = name, email = email, password = pass_sec, profile_pic = profile_pic,bio =bio)
        new_user.save_user()        
        mail_message("Welcome to 60sec pitch","email/welcome_user",user.email,user=user)
        return redirect (url_for('auth.login'))
        title = "New Account"

    return render_template('auth/register.html',registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("main.index"))