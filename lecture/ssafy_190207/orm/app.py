from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


"""
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
    );
"""
db.init_app(app)
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return "제목: {}, 내용: {}".format(self.title, self.content)
    
db.create_all()

@app.route('/')
def index():
    """
    DB에 저장된 모든 글을 보여준다.
    """
    articles = Article.query.all()
    
    return render_template('index.html', articles=articles)


@app.route('/create')
def create():
    """
    DB에 입력받은 제목과 내용을 저장한다.
    """
    form_title = request.args.get('title')
    form_content = request.args.get('content')
    
    # ORM을 사용하여 새로운 Article 객체를 만들어 DB에 저장
    a = Article(title=form_title, content=form_content)
    db.session.add(a)
    db.session.commit()
    
    return redirect('/')
    
    
@app.route('/delete/<int:article_id>')
def delete(article_id):
    """
    article_id에 저장된 id 값을 가진 레코드를 지운다.
    """
    a = Article.query.filter_by(id=article_id).first()
    db.session.delete(a)
    db.session.commit()
    return redirect('/')
    

@app.route('/edit/<int:article_id>')
def edit(article_id):
    """
    글을 편집 할 수 있는 페이지를 보여준다.
    """
    a = Article.query.filter_by(id=article_id).first()
    
    return render_template('edit.html', article=a)
    

@app.route('/update/<int:article_id>')
def update(article_id):
    """
    article_id에 저장된 id 값을 가진 레코드를 수정한다.
    """
    title = request.args.get('title')
    content = request.args.get('content')
    
    a = Article.query.filter_by(id=article_id).first()
    a.title = title
    a.content = content
    db.session.commit()
    
    return redirect('/')