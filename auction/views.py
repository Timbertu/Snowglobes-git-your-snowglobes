from flask import Blueprint, redirect, url_for, request, session, render_template
from .models import Listing, User, Watchlist, Bidding
from .forms import WatchlistAddForm, WatchlistRemForm
from . import db
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/watchlist')
@login_required
def watchlist():
    
    return render_template('watchlist.html')