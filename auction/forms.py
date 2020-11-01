
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#Define acceptable image files 
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}


#Create Login form to provide login information (all with validators and error handling messages)
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#Create Register Form with all register information (all with validators and error handling messages)
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    contact_num = StringField("Contact Number", validators=[
                              InputRequired("Please enter a valid email")])
    address = StringField("Address", validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #Submit form button 
    submit = SubmitField("Register")


#Create Listing Form with all item listing information (all with validators and error handling messages)
class ListingForm(FlaskForm):
    name = StringField("Item Name", validators=[
                       InputRequired('Enter item name')])
    size = SelectField("Size", choices=[
                           ('Tiny'), ('Small'), ('Medium'), ('Large'), ('Gargantuan')])
    origin = StringField("Location of Origin", validators=[
                         InputRequired('Enter item location of origin')])
    colour = StringField("Primary Colour", validators=[
                         InputRequired('Enter item colour')])
    age = StringField("Age (In years)", validators=[
                      InputRequired('Enter item age')])
    category = SelectField("Category", choices=[
                           ('Fancy'), ('Novelty'), ('Mundane')])
    description = StringField("Item Description", validators=[
        InputRequired('Enter item description')])
    startbid = StringField("Starting Bid ($)", validators=[
                           InputRequired('Enter item starting bid')])
    image = FileField('Item Image', validators=[
        FileRequired(message='Image can not be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])
    #Submit form button
    submit = SubmitField("Create")

#Create Bidding Form with bid amount (all with validators and error handling messages)
class BiddingForm(FlaskForm):
    bid_amount=IntegerField("Bid Amount", validators=[InputRequired('Enter bid amount')])
    #submit button
    submit=SubmitField("Enter Bid")

#Create Watchlist Add Form
class WatchlistAddForm(FlaskForm):
    #submit button
    add_item=SubmitField("Add to Watchlist")

#Create Watchlist Remove Form
class WatchlistRemForm(FlaskForm):
    #submit button
    rem_item=SubmitField("Remove Item")

#Create Auction Close Form 
class CloseAucForm(FlaskForm):
    #submit button
    close_auction=SubmitField("Close Auction")
