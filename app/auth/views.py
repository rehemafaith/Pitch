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
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitch login"
    return render_template('auth/login.html',login_form = login_form,title=title)
    
    # if login_form.validate_on_submit():
    #     user_email = login_form.email.data
    #     user_pass = login_form.password.data
    #     rem = login_form.remember_me.data

        
    #     user = User.query.filter_by(email = user_email).first()
     
    #     if user is not None and user.verify_password(login_form.password.data):
    #         login_user(user,login_form.remember.data)
    #         flash ("Welcome!")
    #         return redirect(request.args.get('next') or url_for('main.index'))
     
    # flash('Invalid username or Password')

    # title = "60 seconds login"
    # return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():   
        username = form.username.data
        email = form.email.data
        pass_sec = form.password.data
        profile_pic_path = "photos/download.png"
        bio = ""
        new_user = User(username = username, email = email, password = pass_sec, profile_pic_path = profile_pic_path,bio =bio)
        new_user.save_user()        
        mail_message("Welcome to 60sec pitch","email/welcome_user",new_user.email,new_user=new_user)
        return redirect (url_for('auth.login'))
        title = "New Account"

    return render_template('auth/register.html',registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("main.index"))