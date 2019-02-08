from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    title_en = db.Column(db.String)
    audience = db.Column(db.Integer)
    open_date = db.Column(db.String)
    genre = db.Column(db.String)
    watch_grade = db.Column(db.String)
    score = db.Column(db.Float)
    poster_url = db.Column(db.TEXT)
    description = db.Column(db.TEXT)

class Star(db.Model):
    __tablename__ = "starrating"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Float)
    img_url = db.Column(db.TEXT)
    
db.create_all()

@app.route('/movies')
def movies():
    movies = Movie.query.all()
    
    return render_template('index.html', movies=movies)


@app.route('/movies/new')
def new():
    return render_template('new.html')
    
    
@app.route('/movies/<int:movie_id>')
def show(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    star = Star.query.filter_by(score=movie.score).first()
    
    return render_template('detail.html', movie=movie, star=star)
    
    
@app.route('/movies/create')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(movie)
    db.session.commit()
    
    return render_template('success.html')
    
    
@app.route('/movies/<int:movie_id>/delete')
def delete(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie)
    db.session.commit()
    
    return redirect('/movies')
    

@app.route('/movies/<int:movie_id>/edit')
def edit(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    
    return render_template('edit.html', movie=movie)
    

@app.route('/movies/<int:movie_id>/update')
def update(movie_id):
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie.query.filter_by(id=movie_id).first()
    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_date = open_date
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    db.session.commit()
    
    return redirect('/movies/{}'.format(movie_id))