from flask import Flask, render_template, abort, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from forms import Select_Movie

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miniIMDB.db'
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

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', page_title='IT WORKS!')

######################## list all MOVIE ########################
  
# list all the movies
@app.route('/all_movies')
def all_movies():
    movies = models.Movie.query.all()
    return render_template('all_movies.html', page_title="ALL MOVIES", movies=movies)

######################## DISPLAY MOVIE ########################
  
# details of one movie
@app.route('/movie/<int:id>')
def movie(id):
  movie = models.Movie.query.filter_by(id=id).first()
  if movie == None:
    # throw 404
    return render_template("404.html")
  title = movie.title
  return render_template('movie.html',page_title=title,movie=movie)

@app.route('/add_movie')
def add_movie():
  movies = models.Movie.query.all()
  return render_template('add_movie.html', page_title='Add', movies = movies)

######################## CHOOSE MOVIE ########################
######################## NOT WORKING ########################
  
@app.route('/choose_movie', methods=['GET', 'POST'])
def choose_movie():
 form = Select_Movie()
 movies = models.Movie.query.all()
 form.movies.choices = [(movie.id, movie.title) for movie in movies]
 if request.method=='POST':
   if form.validate_on_submit():
     return redirect(url_for('movie', id=form.moviename.data))
   else:
     abort(404)
 return render_template('movies.html', title='Select A Movie', form=form) 

######################## DELETE MOVIE ########################

@app.route('/delete_movie', methods=['GET','POST'])
#@login_required
def delete_movie():
    #get the value of the hidden input named "movie_id" in the html template if the form exists from the post
    if request.form:
      movie_id = request.form.get("movie_id")
      # debug
      print(f"movie to delete = {movie_id}")
      #and do sql stuff to remove it! find the question we want to dlete from it's id
      movie_to_delete = models.Movie.query.filter_by(id=movie_id).first()
      # debug
      print(f"movie_to_delete = {movie_to_delete}")

# https://stackoverflow.com/questions/24291933/sqlalchemy-object-already-attached-to-session

      db.Session = db.Session.object_session(movie_to_delete)
      db.Session.delete(movie_to_delete)
      
      #db.session.delete(movie_to_delete)#delete it
      db.Session.commit()#commit change to db
      db.Session.close()
    #url_redirect = url_for("home")
    #print(url_redirect)
    return redirect(url_for("add_movie"))

######################## ADD MOVIE ########################

@app.route('/add_movie', methods=['GET','POST'])
def add_add_movie():
    '''this will add a movie to the database and redirect to the add_movie route again'''
    if request.form:
        #we got a form back now process by getting the items by their name
        new_title = request.form.get("Movie title")#get questions from form
        new_year = request.form.get("Year")     #get answer from form
        new_description = ""
        new_movie = models.Movie(title=new_title,year=new_year,description=new_description)  #create a new movie instance
        db.Session.add(new_movie)
        db.Session.commit()
    return redirect(url_for("add_movie"))

######################## 404 ########################

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html")

######################## start server ########################

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)