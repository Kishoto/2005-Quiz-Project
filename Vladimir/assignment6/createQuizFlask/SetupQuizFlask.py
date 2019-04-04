from CreateQuiz import *
from datetime import *
from flask import Flask,render_template,request,flash,url_for

app = Flask(__name__) 
quizobj = None

@app.route('/',methods=['GET','POST'])
def launchPage():
    return render_template('setup_quiz.html')

@app.route('/restrictaccess',methods=['GET','POST'])
def instanceQuiz():
    quizname = request.form.get('quizName')
    attempts = request.form.get('attempts')
    stime = request.form.get('stime')
    etime = request.form.get('etime')
    quizobj = CreateQuiz(quizname,attempts,stime,etime)
    
    return render_template('restrict_access.html')

@app.route('/ra',methods=['GET','POST'])
def giveAccess():
     

@app.route('/addQuestion', methods=['GET','POST'])
def creationPage():
    return render_template('QuestionCreation.html')

if __name__ == '__main__':
    app.run(debug=True)