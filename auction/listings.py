from flask import Blueprint, redirect, url_for, request, session, render_template
from .models import Listing, User, Watchlist, Bidding
from .forms import ListingForm, BiddingForm, WatchlistAddForm, WatchlistRemForm
from . import db
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, current_user

# Use of blue print to group routes,
# name - first argument is the blue print name
# import name - second argument - helps identify the root url for it
bp = Blueprint('listing', __name__, url_prefix='/listings')


@bp.route('/<id>', methods=['GET', 'POST'])
def show(id):
    listing = Listing.query.filter_by(id=id).first()
    bids = Bidding.query.filter_by(lis_id=listing.id).order_by(
        Bidding.sub_bid.desc()).limit(1).all()
    bidform = BiddingForm()
    if bidform.validate_on_submit():
        bid = Bidding(sub_bid=bidform.bid_amount.data,
                      usr_id=current_user.id,
                      lis_id=listing.id)
        # add the object to the db session
        db.session.add(bid)
        # commit to the database
        db.session.commit()
        return redirect(url_for('listing.show', id=id, lis_id=listing, bidtest=bids))

    watchform = WatchlistAddForm()
    if watchform.validate_on_submit():
        watchadd = Watchlist(user_id=current_user.id,
                             list_id=listing.id)
        # add the object to the db session
        db.session.add(watchadd)
        # commit to the database
        db.session.commit()
        return redirect(url_for('listing.show', id=id))
    return render_template('listings/show.html', listing=listing, bids=bids, bidform=bidform, watchform=watchform)


def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)

    upload_path = os.path.join(
        BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ListingForm()
    print('Method type: ', request.method)
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        listing = Listing(uname=form.name.data,
                          size=form.size.data,
                          origin=form.origin.data,
                          colour=form.colour.data,
                          age=form.age.data,
                          category=form.category.data,
                          description=form.description.data,
                          startbid=form.startbid.data,
                          image=db_file_path,
                          upost=current_user.name)
        u1 = User.query.filter_by(name=uname).first()
        if u1:
            flash('Item created successfully')

        # add the object to the db session
        db.session.add(listing)
        # commit to the database
        db.session.commit()
        return redirect(url_for('listing.create'))
    return render_template('listings/create.html', form=form)
