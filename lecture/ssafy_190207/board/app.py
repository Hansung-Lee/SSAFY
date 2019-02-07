from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    db = sqlite3.connect('board.db')
    c = db.cursor()
    sql = "SELECT * FROM articles"
    c.execute(sql)
    data = c.fetchall()
    return render_template('index.html', data=data)
    
    
@app.route('/create')
def create():
    """
    index 페이지에서 보낸 정보를 받아, DB에 저장
    """
    
    # 유저가 요청을 보낸 정보가 담겨있음
    title = request.args.get('Title')
    content = request.args.get('Content')
    
    # sqlite3를 활용하여 제목과 내용을 DB에 저장한다.
    db = sqlite3.connect('board.db')  # (sqlite:///) 생략 가능
    # 1. 커서를 생성
    c = db.cursor()
    
    # 2. SQL 실행
    sql = "INSERT INTO articles (title, content) VALUES ('{}', '{}')".format(title, content)
    c.execute(sql)
    
    # 3. commit
    db.commit()
    
    return redirect('/')
    
    
@app.route('/delete/<int:article_id>')
def delete(article_id):
    """
    article_id에 저장된 id 값을 가진 레코드를 지운다.
    """
    db = sqlite3.connect('board.db')
    c = db.cursor()
    sql = "DELETE FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/')
    

@app.route('/edit/<int:article_id>')
def edit(article_id):
    """
    글을 편집 할 수 있는 페이지를 보여준다.
    """
    # 1. 편집하고자 하는 글을 불러온다.
    # 2. form에 불러온 글을 넣는다.
    
    db = sqlite3.connect('board.db')
    c = db.cursor()
    sql = "SELECT * FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    return render_template('edit.html', article=article)
    

@app.route('/update/<int:article_id>')
def update(article_id):
    """
    article_id에 저장된 id 값을 가진 레코드를 수정한다.
    """
    
    title = request.args.get('Title')
    content = request.args.get('Content')
    
    db = sqlite3.connect('board.db')
    c = db.cursor()
    sql = "UPDATE articles SET title='{}', content='{}' WHERE ID = {}".format(title, content, article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/')