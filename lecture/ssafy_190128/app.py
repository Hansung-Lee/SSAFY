from flask import Flask, render_template, request
import datetime
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/ask')
def ask():
    dt = datetime.datetime.now() + datetime.timedelta(seconds=32400)
    
    question = request.args.get('question')
    
    with open('question.csv', 'a') as f:
        wr = csv.writer(f)
        row_count=0
        with open('question.csv', 'r') as f2:
            reader = csv.reader(f2)
            row_count = sum(1 for row in reader)
        wr.writerow([row_count+1, question, dt.strftime("%Y/%m/%d %H:%M:%S")])
    
    return render_template('ask.html', question=question)
    
    
@app.route('/quest')
def quest():
    questions = []
    with open('question.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            questions.append(line)
            
    return render_template('quest.html', questions=reversed(questions))
