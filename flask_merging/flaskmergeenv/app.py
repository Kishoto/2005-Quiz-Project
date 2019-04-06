
from flask import Flask, render_template, request, flash, redirect, url_for
from login import *
from datetime import datetime
from CreateQuiz import *
from Take_Quiz import *
from QuizResult import *

import os
ansList = []
studentAccount = Login.loginStorage.getStudentAccount()
instructorAccount = Login.loginStorage.getInstructorAccount()


app = Flask(__name__)
app.secret_key = os.urandom(24)

obj = QuizResult()
obj.add_quiz_attempts()
obj.get_grades()

quizname = ''

@app.route('/', methods=['GET', 'POST'])
def base():
    """Get the base page, which include 'instructor' and 'student'.
    Instructor click 'instructor' to register and log in. Student click 'student' to register and log in."""
    if request.method == 'GET':
        return render_template('base.html')


@app.route('/instructor/', methods=['GET', 'POST'])
def instructor():
    """Instructor page, which include 'Register' and 'Login'
    if the instructor has no account, click 'Register' to transfer to the register page.
    if the instructor has an account, click 'Login' to transfer to the login page"""
    if request.method == 'GET':
        return render_template('instructor.html')


@app.route('/student/', methods=['GET', 'POST'])
def student():
    """Student page, which include 'Register' and 'Login'
    if the student has no account, click 'Register' to transfer to the register page.
    if the student has an account, click 'Login' to transfer to the login page"""
    if request.method == 'GET':
        return render_template('student.html')


@app.route('/instructor_Register/', methods=['GET', 'POST'])
def insRegister():
    """Instructor register page, after register store the data into Persist: {'instructor'}
     """

    if request.method == 'GET':
        return render_template('instructor_regist_form.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        # Login.loginStorage.addInstructorAccount(username, password)

        if username is not None and password == confirm:
            Login.loginStorage.addInstructorAccount(username, password)
            return redirect(url_for('instructor_login'))
            
        return render_template('instructor_regist_form.html', message = 'Invalid username or password')

@app.route('/student_Register/', methods=['GET', 'POST'])
def stuRegister():
    """student register page, after register store the data into Persist: {'student'} """
    if request.method =='GET':
        return render_template('student_regist_form.html')
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        # Login.loginStorage.addStudentAccount(username,password)

        if username is not None and password == confirm:
            Login.loginStorage.addStudentAccount(username,password)
            return redirect(url_for('stu_login'))

        return render_template('student_regist_form.html', message = 'Invalid username or password')


@app.route('/student_login/', methods=['GET', 'POST'])
def stu_login():
    """Studnt log in page, which get the data from the persist to check whether the student can log in successfully or not"""

    if request.method == 'GET':
        return render_template('student_login.html')

    if request.method == 'POST':

        global glob_user
        username = request.form.get('username')
        glob_user = username
        password = request.form.get('password')


        if not all([username,password]):
            flash('imcomplete')

        for user in studentAccount:
            # the situation that username exist in the persist and the password should also be in the persist and conform to what user set.
            if username == user and password == studentAccount[user]:
                return redirect(url_for('quiz'))
            # the situation that the username is not in the persist
            elif username != user:
                return render_template('student_login.html', message = 'Account is not exist, Please register first')
            # the situation that the password is not what user set
            elif password != studentAccount[user]:
                return render_template('student_login.html', message = 'Input the wrong password')
        else:
            return render_template('student_login.html', message = 'Account is not exist, Please register first')

@app.route('/instruct_login/', methods=['GET', 'POST'])
def instructor_login():
    """Instructor log in page, which get the data from the persist to check whether the instructor can log in successfully or not"""

    if request.method == 'GET':

        return render_template('instructor_login.html')

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username,password]):
            flash('imcomplete')
                                                                                                                  
        for instruct_user in instructorAccount:
            # the situation that username exist in the persist and the password should also be in the persist and conform to what user set.
            if username == instruct_user and password == instructorAccount[instruct_user]:
                return redirect(url_for('createQuiz'))
            # the situation that the username is not in the persist
            elif username != instruct_user:
                return render_template('instructor_login.html', message = 'Account is not exist, Please register first')
            # the situation that the password is not what user set
            elif password != instructorAccount[instruct_user]:
                return render_template('instructor_login.html', message = 'Input the wrong password')
        else:
            return render_template('instructor_login.html', message = 'Account is not exist, Please register first')

#Create Quiz
@app.route('/createquiz')
def createQuiz():
    return render_template('setup_quiz.html')

@app.route('/restrictaccess',methods=['GET','POST'])
def instanceQuiz():
    global quizObj
    quizname = request.form.get('quizName')
    attempts = request.form.get('attempts')
    stime = request.form.get('stime')
    etime = request.form.get('etime')
    startTime = datetime.datetime.strptime(stime,'%Y-%m-%d')
    endTime = datetime.datetime.strptime(etime,'%Y-%m-%d')

    quizObj = CreateQuiz(quizname,int(attempts),startTime,endTime)

    return render_template('restrict_access.html')

@app.route('/ra',methods=['GET','POST'])
def giveAccess():
    quizObj._giveAccess(request.form.get('studentName'))
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

    quizObj._addQuestion(question,weight)
    quizObj._addChoices(choiceList)
    quizObj._addAnswerKey(ansList)

    return render_template('QuestionCreation.html')

@app.route('/newquiz',methods=['GET','POST'])
def newQuiz():
    quizObj._storeQuiz()
    return render_template('setup_quiz.html')

#Take Quiz
@app.route('/takequiz')
def quiz():
    quizes = TakeQuiz.persistStorage.getQuiz()
    quizNames = []
    for quiz in quizes:
        quizNames.append(quiz)

    return render_template('quizzes.html', quizNames=quizNames)

@app.route('/quiz.html',methods=['GET','POST'])
def display_quiz():
    #Check to see if there is a present incomplete quiz by this student.
    global activeQuiz
    global studentName
    studentName = glob_user
    global quizName
    quizName = request.form.get('quiz')
    activeQuiz = TakeQuiz(studentName,quizName)
    quizContent = activeQuiz.getQuizContent()

    #Setting the attempt display number
    global attemptNum
    if activeQuiz.numberOfAttempts() == 0:
        attemptNum = 1
    elif activeQuiz.numberOfAttempts() == activeQuiz.getFoundQuiz().getAttempts():
        attemptNum = activeQuiz.numberOfAttempts()
    elif activeQuiz.numberOfAttempts() > 0 and TakeQuiz.studentsQA[studentName][quizName][-1].getComplete() == True:
        attemptNum = activeQuiz.numberOfAttempts() + 1
        
    #For Debugging
    newAttempt = activeQuiz._presentAttempt
    #
    
    incompleteQuiz = TakeQuiz.resumeQuiz(studentName,quizName)
    oldResponse = []
    if incompleteQuiz is not None:
        oldResponse = incompleteQuiz.getResponse()
    return render_template('quiz.html', newAttempt=newAttempt,permission=activeQuiz.checkAccess(), attemptNum=attemptNum, oldResponse=oldResponse, name=quizContent[0], questions=quizContent[1], choiceList=quizContent[2])



#Receives a post request from quiz.html: Saves all inputs received from the submission 
@app.route('/done.html', methods=['GET', 'POST'])
def display_done():
    finished = False
    if request.method == 'POST':
        for i in range(len(activeQuiz.getFoundQuiz().getQuestions())):
            choiceName = "choice"+str(i+1)
            answer = request.form.get(choiceName)
            savedAttempt = activeQuiz.saveAnswer(i,answer)
        action = request.form.get('button')
        if action == 'Submit':
            activeQuiz.submitQuiz()
            finished = True
        elif action == 'Stop':
            activeQuiz.stopQuiz()
        jAttempts = TakeQuiz.studentsQA[studentName][quizName]
        return render_template('done.html', jAttempts=jAttempts, finished=finished)

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




if __name__ == '__main__':
    app.run(debug=True)
