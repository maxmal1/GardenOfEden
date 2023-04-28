# main.py

from flask import Flask, render_template, flash, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from . import db

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from project.helper_functions import *

main = Blueprint('main', __name__)
location = location_finder()

@main.route('/', methods = ['GET'])
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=location[1],
        lng=location[0],
        markers=all_plots(),#[(37.4419, -122.1419)],
        #style="height:400px;width:600px;margin:0;",
        style = "height: 70vh;width: 90vw;margin:0",
    )
    return render_template('example.html', mymap=mymap)
"""def index():
    return render_template('index.html')"""
    

@main.route('/merch_delete/<mid>', methods = ['GET'])
@login_required
def merch_delete(mid):
        #merch = Plot_Location.query.filter_by(id=mid).first()
        #if merch:
        #msg_text = 'Merchant %s successfully removed' % str(merch)
        #Plot_Location.query.filter_by(id=mid).delete()
    Plot_Location.query.filter_by(id=mid).delete()
    db.session.commit()
    
        #flash(msg_text)
    return redirect(url_for('main.mapview'))

@main.route('/profile')
@login_required
def profile():

    plots = user_plots(current_user.id)

    return render_template('profile.html', name=current_user.name, user_plots = plots, merch_delete=merch_delete)

@main.route('/about')
def about():
    return render_template('about.html')