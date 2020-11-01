from flask import Blueprint, redirect, url_for, request, session, render_template
from .models import Listing, User
from . import db
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, current_user

# Create categories Blueprint with prefix 
bp = Blueprint('categories', __name__, url_prefix='/category')

# All three routes make up the categories drop-down options
# It also returns a listing to its respective category when a listing is made

#Create route 
@bp.route('/fancy')
def fancy():
    #Query databse for all listings with the category option 'Fancy'
    fancyQuery = Listing.query.filter(Listing.category.like('Fancy')).all()
    #Render the page 
    return render_template('category.html', listings=fancyQuery, heading='Fancy')


@ bp.route('/novelty', methods=['GET', 'POST'])
def novelty():
    #Query databse for all listings with the category option 'Novelty'
    noveltyQuery = Listing.query.filter(Listing.category.like('Novelty')).all()
    #Render the page 
    return render_template('category.html', listings=noveltyQuery, heading='Novelty')


@ bp.route('/mundane', methods=['GET', 'POST'])
def mundane():
    #Query databse for all listings with the category option 'Mundane'
    mundaneQuery = Listing.query.filter(Listing.category.like('Mundane')).all()
    #Render the page 
    return render_template('category.html', listings=mundaneQuery, heading='Mundane')