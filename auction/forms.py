
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#Define acceptable image files 
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    contact_num = StringField("Contact Number", validators=[
                              InputRequired("Please enter a valid email")])
    address = StringField("Address", validators=[InputRequired()])

    # add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")

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
    submit = SubmitField("Create")

class BiddingForm(FlaskForm):
    bid_amount=StringField("Bid Amount", validators=[InputRequired('Enter bid amount')])
    
    #submit button
    submit=SubmitField("Enter Bid")

class WatchlistAddForm(FlaskForm):
    add_item=SubmitField("Add to Watchlist")

class WatchlistRemForm(FlaskForm):
    rem_item=SubmitField("Remove Item")

