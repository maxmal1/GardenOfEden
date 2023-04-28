# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Plot_Location, Individual_Plot
from . import db
from .helper_functions import street_to_loc
from datetime import date

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.mapview'))

@auth.route('/add_plot')
@login_required
def add_plot():
    return render_template('add_plot.html')

@auth.route('/add_plot', methods=['POST'])
@login_required
def add_plot_post():

    street_address = request.form.get('street_addr')
    size = request.form.get('size')

    #user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    """if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))"""

    lon_lat = street_to_loc(street_address)
    
    new_plot = Plot_Location(user_id = current_user.id, street_addr = street_address, lon  = lon_lat[0], lat = lon_lat[1],size = size)

    # add the new user to the database
    db.session.add(new_plot)
    db.session.commit()

    return redirect(url_for('main.profile'))

"""@auth.route('/add_plant')
@login_required
def add_plant():
    return render_template('add_plant.html')"""
    
@auth.route('/add_plant/<mid>', methods=['GET','POST'])
@login_required
def add_plant(mid):
    #plot = Plot_Location.query.filter_by(street_addr=mid).first()
    #print(mid)
    #print(plot)
    curr_date = date.today()
    
    if request.method == 'POST':
        mid = session.get('mid')
        plot = Plot_Location.query.filter_by(street_addr=mid).first()
        plant = request.form.get('plant')
        #print(plot)
        new_plant = Individual_Plot(plot_id = plot.id,plant = plant, date = curr_date, user_id = current_user.id)
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for('auth.add_plant', mid = mid))
    else:
        # handle GET request here
        session['mid'] = mid
        plot = Plot_Location.query.filter_by(street_addr=mid).first()
        plot = Individual_Plot.query.filter_by(plot_id = plot.id)
        #print(plot[0].user_id)
        #print(current_user.id)
        return render_template('add_plant.html', plot=plot, user_id = current_user.id)
    
@auth.route('/plant_delete/<mid>', methods = ['GET'])
@login_required
def plant_delete(mid):
        #merch = Plot_Location.query.filter_by(id=mid).first()
        #if merch:
        #msg_text = 'Merchant %s successfully removed' % str(merch)
        #Plot_Location.query.filter_by(id=mid).delete()
    Individual_Plot.query.filter_by(id=mid).delete()
    db.session.commit()
    
        #flash(msg_text)
    return redirect(url_for('main.mapview'))