from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return


@app.route('/articles')
def articles():
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "SELECT id, title FROM articles"
    c.execute(sql)
    data = c.fetchall()
    
    return render_template('articles.html', data=data)
    
    
@app.route('/articles/<int:article_id>')
def article(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE id = {}".format(article_id)
    c.execute(sql)
    data = c.fetchone()
    
    return render_template('detail.html', data=data)
    
    
@app.route('/articles/new')
def new():
    return render_template('new.html')
    
    
@app.route('/articles/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')
    
    dt = datetime.datetime.now() + datetime.timedelta(seconds=32400)
    created_at = dt.strftime("%Y/%m/%d %H:%M:%S")
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "INSERT INTO articles (title, content, created_at, author) VALUES ('{}', '{}', '{}', '{}')".format(title, content, created_at, author)
    c.execute(sql)
    db.commit()
    
    return render_template('success.html')
    
    
@app.route('/articles/<int:article_id>/delete')
def delete(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "DELETE FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/articles')
    

@app.route('/articles/<int:article_id>/edit')
def edit(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    return render_template('edit.html', article=article)
    

@app.route('/articles/<int:article_id>/update')
def update(article_id):
    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = "UPDATE articles SET title='{}', content='{}', author='{}' WHERE ID = {}".format(title, content, author, article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/articles/{}'.format(article_id))