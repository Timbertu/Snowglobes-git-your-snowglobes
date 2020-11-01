from flask import Blueprint, flash, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash,check_password_hash
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db
from .models import User


#create a blueprint
bp = Blueprint('auth', __name__)

#create login route 
@bp.route('/login', methods=['GET','POST'])
def login():
    #import LoginForm() from forms.py
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #if no errors, set the login_user of flask_login to manage the user
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            #if error occurs 
            flash(error)
    #render the login page using user.html as a template 
    return render_template('user.html', form=login_form, heading='Login')


#create route for the register page 
@bp.route('/register', methods=['GET','POST'])
def register():
    #import the RegisterForm() from forms.py 
    register = RegisterForm()
    #the validation of the form is fine
    if (register.validate_on_submit() == True):
            #get username, password, email, phone number and address from the form
            uname=register.user_name.data
            pwd=register.password.data
            email=register.email_id.data
            phnum=register.contact_num.data
            addrs=register.address.data
            #check if a user with the same username already exists, flash error message if it does 
            u1 = User.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            #generate password hash 
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = User(name=uname, password_hash=pwd_hash, emailid=email, contact_num=phnum, address=addrs)
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            return redirect(url_for('main.index'))
    #the else is called when there is a GET message
    else:
        return render_template('user.html', form=register, heading='Register')

#create route for logout page 
@bp.route('/logout', methods=['GET','POST'])
#user is required to be logined to logout 
@login_required
def logout():
    #clear the user session and render the template 
    session.clear()
    return render_template('logout.html')