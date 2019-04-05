from flask import Flask,render_template, request, flash, url_for
from QuizResult import *

app = Flask(__name__)

app.secret_key = 'secret'

obj = QuizResult()
obj.add_quiz_attempts()
obj.get_grades()

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

@app.route("/ins_class_attempts",methods=['GET', 'POST'])
def class_attempts():
    quizname = request.form.get('quizname')
    c = obj.ins_class_attempts(quizname)
    if len(c) < 1:
        d = ['a','b']
    else:
        d = [{'first': c}]
    
    return render_template('ins_class_attempts.html', title='Class Attempts',call = d,name = quizname)

@app.route("/ins_student_grades",methods=['GET', 'POST'])
def student_grades():
    stuname = request.form.get('stuname')
    c = obj.ins_student_grades(stuname)

    if len(c) < 1:
        d = ['a','b']
    else:
        d = [{'first': c}]

    return render_template('ins_student_grades.html', title='Student Grades',call = d,name = stuname)


@app.route("/stu_quiz_grades",methods=['GET', 'POST'])
def grade_summaries():
    stuname = request.form.get('stuname')
    c = obj.stu_quiz_grades(stuname)

    if len(c) < 1:
        d = ['a','b']
    else:
        d = [{'first': c}]

    return render_template('stu_quiz_grades.html', title='Student Grades',call = d,name = stuname)

@app.route("/stu_quiz_detailed",methods=['GET', 'POST'])
def detail_summaries():
    stuname = request.form.get('stuname')
    quizname = request.form.get('quizname')
    
    c = obj.stu_quiz_detailed(stuname,quizname)

    if len(c) < 1:
        d = ['a','b']
    else:
        d = [{'first': c}]

    return render_template('stu_quiz_detailed.html', title='Student Grades',call = d,name = stuname)





##@app.route("/quiz1_grades")
##def quiz1():
##
##    c = obj.ins_class_avg('Quiz1')
##    d = {'grade': c}
##        
##    return render_template('quiz1_grades.html', call = d,title='Quiz 1 Grades')
##
##@app.route("/quiz2_grades")
##def quiz2():
##        
##    call = obj.ins_class_avg('quizname')
##    d = {'grade': call}
##        
##    return render_template('quiz2_grades.html', call = d,title='Quiz 1 Grades')
##
##
##@app.route("/quiz3_grades")
##def quiz3():
##    
##    call = obj.ins_class_avg('quizname')
##    d = {'grade': call}
##        
##    return render_template('quiz3_grades.html', call = d,title='Quiz 1 Grades')

if __name__ == '__main__':
    app.run(debug = True)


