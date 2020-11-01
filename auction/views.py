from flask import Blueprint, redirect, url_for, request, session, render_template
from .models import Listing, User, Watchlist, Bidding
from .forms import WatchlistRemForm
from . import db
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)

#Create route for home page and render template 
@bp.route('/')
def index():
    listings = Listing.query.all()
    bids = Bidding.query.all()
    return render_template('home.html', listings=listings, bids=bids)

#Create route for wathclist and render template 
@bp.route('/watchlist')
@login_required
def watchlist():
    #showbid = Bidding.query.filter_by(lis_id=id).order_by(Bidding.sub_bid.desc()).first()
    #item = Watchlist.query.filter_by(user_id=id).first()
    return render_template('watchlist.html')