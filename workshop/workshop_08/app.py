from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dictionary')
def dictionary():
    fruits = {'apple': '사과', 'banana':'바나나'}
    input_fruit = request.args.get('input_fruit')
    result = fruits.get(input_fruit, False)
    
    if result:
        msg = "{}은(는) {}!".format(input_fruit, result)
    else:
        msg = "{}은(는) 나만의 단어장에 없는 단어입니다.".format(input_fruit)
        
    return render_template('dictionary.html', msg=msg)