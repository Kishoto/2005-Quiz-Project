from CreateQuiz import *
from datetime import *
from flask import Flask,render_template,request,flash,url_for

app = Flask(__name__) 

#These are abritrary values to initialize the object
quizobj = CreateQuiz("PlaceHolderName","2","2019,3,30","2019,3,32")

#Initializes ansList so it can be used when the instructor
#Adds more than one answer
ansList = []
@app.route('/',methods=['GET','POST'])
def launchPage():
    return render_template('setup_quiz.html')

@app.route('/restrictaccess',methods=['GET','POST'])
def instanceQuiz():
    quizname = request.form.get('quizName')
    attempts = request.form.get('attempts')
    stime = request.form.get('stime')
    etime = request.form.get('etime')
    quizobj._setQuizName(quizname)
    quizobj._setAttempts(attempts)
    quizobj._setStartTime(stime)
    quizobj._setEndTime(etime)

    return render_template('restrict_access.html')

@app.route('/ra',methods=['GET','POST'])
def giveAccess():
    quizobj._giveAccess(request.form.get('studentName'))
    return render_template('restrict_access.html')

@app.route('/addQuestion', methods=['GET','POST'])
def creationPage():
    return render_template('QuestionCreation.html')

@app.route('/addAnswer',methods=['GET','POST'])
def addAnswer():
    swap1 = request.form.get('question')
    swap2 = request.form.get('weight')
    answer = request.form.get('answer')
    ansList.append(answer)
    return render_template('QuestionCreation.html',
    question=swap1,weight=swap2)

@app.route('/newQuestion',methods=['GET','POST'])
def newQuestion():
    question = request.form.get('question')
    weight = request.form.get('weight')
    choices = request.form.get('choices')
    choiceList = choices.split(",")

    quizobj._addQuestion(question,weight)
    quizobj._addChoices(choiceList)
    quizobj._addAnswerKey(ansList)

    return render_template('QuestionCreation.html')

@app.route('/newquiz',methods=['GET','POST'])
def newQuiz():
    quizobj._storeQuiz()
    return render_template('setup_quiz.html')


if __name__ == '__main__':
    app.run(debug=True)