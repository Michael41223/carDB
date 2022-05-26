# michaels carDB for 12 credits

from flask import Flask, render_template, abort, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from forms import Select_Movie

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carsV2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'correcthorsebatterystaple'

db = SQLAlchemy(app)

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'sup3r_secr3t_passw3rd'

# need db to import models
import models

######################## HOME ########################
# home route
@app.route('/')
def home():
    return render_template('home.html', page_title='IT WORKS!')


######################## about us ########################
# about_us route

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', page_title='IT WORKS!')

######################## list all cars ########################
  
# list all the cars
@app.route('/all_cars')
def all_cars():
    cars = models.Cars.query.all()
    return render_template('all_cars.html', page_title="ALL CARS", cars = cars)

######################## DISPLAY car ########################

@app.route('/car/<int:id>')
def car():
  return render_template('car.html', page_title="Display car")

######################## DISPLAY car ########################
  
@app.route('/feed_back')
def feed_back():
  return render_template('feed_back.html', page_title="FEEDBACK")

######################## 404 ########################

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html")

######################## start server ########################

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)