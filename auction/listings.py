from flask import Blueprint, redirect, url_for, request, session, render_template, flash
from .models import Listing, User, Watchlist, Bidding
from .forms import ListingForm, BiddingForm, WatchlistAddForm, WatchlistRemForm, CloseAucForm
from . import db
from werkzeug.utils import secure_filename 
import os
from flask_login import login_required, current_user

#Create Blueprint for listing with prefix 
bp = Blueprint('listing', __name__, url_prefix='/listings')

# This lists the content of an item
@bp.route('/<id>', methods = ['GET', 'POST']) 
def show(id): 
  listing = Listing.query.filter_by(id=id).first()
  showbid = Bidding.query.filter_by(lis_id=id).order_by(Bidding.sub_bid.desc()).first()
  tablebid = Bidding.query.filter_by(lis_id=id).all()
  bidform = BiddingForm()
  if bidform.validate_on_submit():
    if int(bidform.bid_amount.data) < int(listing.startbid):
      flash("Bid amount too low, the bid must be higher than the starting price, or the current highest bid.")
    else:
      if showbid != None:
        if int(bidform.bid_amount.data) < int(showbid.sub_bid):
          flash("Bid amount too low, the bid must be higher than the current highest bid.")
        else:
          flash("Bid successful, I'm rooting for you!")
          bid = Bidding(sub_bid=bidform.bid_amount.data,
                        usr_id=current_user.id,
                        usr_name=current_user.name,
                        lis_id=listing.id)
          # add the object to the db session
          db.session.add(bid)
          # commit to the database
          db.session.commit()
          return redirect(url_for('listing.show', id=id))
      else:
        flash("Bid successful, I'm rooting for you!")
        bid = Bidding(sub_bid=bidform.bid_amount.data,
                      usr_id=current_user.id,
                      usr_name=current_user.name,
                      lis_id=listing.id)
        # add the object to the db session
        db.session.add(bid)
        # commit to the database
        db.session.commit()
        return redirect(url_for('listing.show', id=id))
    return redirect(url_for('listing.show', id=id))

# This adds watchlist content
  watchform = WatchlistAddForm()
  if watchform.validate_on_submit():
    #Add the data to db
    watchadd = Watchlist(user_name=current_user.name,
                        list_id=listing.id)
    # add the object to the db session
    db.session.add(watchadd)
    # commit to the database
    db.session.commit()
    return redirect(url_for('listing.show', id=id))
  
#This closes an auction
  closeform = CloseAucForm()
  if closeform.validate_on_submit():
    # update the object status to the db session
    listing.status=False
    # commit to the database
    db.session.commit()
    return redirect(url_for('listing.show', id=id))
  return render_template('listings/show.html', 
                            listing=listing, 
                            showbid=showbid, 
                            tablebid=tablebid, 
                            bidform=bidform, 
                            watchform=watchform,
                            closeform=closeform)

#checking image upload file    
def check_upload_file(form):
  fp = form.image.data
  filename = fp.filename
  BASE_PATH = os.path.dirname(__file__)
#adding file to folder and database 
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
  db_upload_path = '/static/image/'+ secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

#Create a route for creating listings 
@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  #Form used is ListingForm
  form = ListingForm()
  print('Method type: ', request.method)
  if form.validate_on_submit():
    db_file_path = check_upload_file(form)
    listing = Listing(name=form.name.data,
                    size=form.size.data,
                    origin=form.origin.data,
                    colour=form.colour.data,
                    age=form.age.data,
                    category=form.category.data,          
                    description=form.description.data,
                    startbid=form.startbid.data,
                    image=db_file_path,
                    upost=current_user.name)

    # add the object to the db session
    db.session.add(listing)
    # commit to the database
    db.session.commit()
    return redirect(url_for('listing.create'))
  return render_template('listings/create.html', form=form)
  