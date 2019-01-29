from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

class Quest(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/')
def index():
    questions = Quest.query.all()
    return render_template('index.html', questions=reversed(questions))
 
    
@app.route('/ask')
def ask():
    dt = datetime.datetime.now() + datetime.timedelta(seconds=32400)
    nowtime = dt.strftime("%Y/%m/%d %H:%M:%S")
    question = request.args.get('question')
    
    # ORM을 통해 DB에 데이터를 저장하는 방법
    quest = Quest(content=question, time=nowtime)
    db.session.add(quest)
    db.session.commit()
    
    return redirect('/')
    
    
@app.route('/delete/<int:id>')
def delete(id):
    d_quest = Quest.query.get(id)
    # d_quest = Quest.query.filter_by(Quest.id=id)
    db.session.delete(d_quest)
    db.session.commit()
    
    return redirect('/')


@app.route('/quest')
def quest():
    
    # DB에 저장된 모든 질문들을 불러온다.
    questions = Quest.query.all()
    
    return render_template('quest.html', questions=reversed(questions))


    
# import csv

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/ask')
# def ask():
#     dt = datetime.datetime.now() + datetime.timedelta(seconds=32400)
    
#     question = request.args.get('question')
    
#     with open('question.csv', 'a') as f:
#         wr = csv.writer(f)
#         row_count=0
#         with open('question.csv', 'r') as f2:
#             reader = csv.reader(f2)
#             row_count = sum(1 for row in reader)
#         wr.writerow([row_count+1, question, dt.strftime("%Y/%m/%d %H:%M:%S")])
    
#     return render_template('ask.html', question=question)
    
    
# @app.route('/quest')
# def quest():
#     questions = []
#     with open('question.csv', 'r') as f:
#         reader = csv.reader(f)
#         for line in reader:
#             questions.append(line)
            
#     return render_template('quest.html', questions=reversed(questions))
