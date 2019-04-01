from flask import Flask,render_template, request, flash, url_for
from QuizResult import *

app = Flask(__name__)

app.secret_key = 'secret'

obj = QuizResult()

quizname = ''

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('start_page.html')

@app.route("/temp_grades")
def home():
        
    return render_template('temp_grades.html', title='Quiz List')

@app.route("/ins_class_part",methods=['GET', 'POST'])
def class_part():
    quizname = request.form.get('quizname')
    c = obj.ins_class_part(quizname)
    d = {'grade': c}
    
    return render_template('ins_class_part.html', title='Class Participation',call = d,name = quizname)


@app.route("/ins_class_hist",methods=['GET', 'POST'])
def class_hist():
    quizname = request.form.get('quizname')
    c = obj.ins_class_hist(quizname)
    d = [{'first': c}]
    
    return render_template('ins_class_hist.html', title='Class Histogram',call = d,name = quizname)



@app.route("/quiz1_grades")
def quiz1():

    c = obj.ins_class_avg('Quiz1')
    d = {'grade': c}
        
    return render_template('quiz1_grades.html', call = d,title='Quiz 1 Grades')

@app.route("/quiz2_grades")
def quiz2():
        
    call = obj.ins_class_avg('quizname')
    d = {'grade': call}
        
    return render_template('quiz2_grades.html', call = d,title='Quiz 1 Grades')


@app.route("/quiz3_grades")
def quiz3():
    
    call = obj.ins_class_avg('quizname')
    d = {'grade': call}
        
    return render_template('quiz3_grades.html', call = d,title='Quiz 1 Grades')

#if __name__ == '__main__':
app.run(debug = True)


