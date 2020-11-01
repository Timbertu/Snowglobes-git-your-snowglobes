from flask import Blueprint, redirect, url_for, request, session, render_template
from .models import Listing, User
from . import db
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, current_user

# Use of blue print to group routes,
# name - first argument is the blue print name
# import name - second argument - helps identify the root url for it
bp = Blueprint('categories', __name__, url_prefix='/category')


@bp.route('/fancy')
def fancy():
    fancyQuery = Listing.query.filter(Listing.category.like('Fancy')).all()
    return render_template('category.html', listings=fancyQuery)


@ bp.route('/novelty', methods=['GET', 'POST'])
def novelty():
    noveltyQuery = Listing.query.filter(Listing.category.like('Novelty')).all()
    return render_template('category.html', listings=noveltyQuery)


@ bp.route('/mundane', methods=['GET', 'POST'])
def mundane():
    mundaneQuery = Listing.query.filter(Listing.category.like('Mundane')).all()
    return render_template('category.html', listings=mundaneQuery)