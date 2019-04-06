
from flask import Flask, render_template, request, flash, redirect, url_for, session
from login import *
import os

studentAccount = Login.loginStorage.getStudentAccount()
instructorAccount = Login.loginStorage.getInstructorAccount()


app = Flask(__name__)
app.secret_key = os.urandom(24)


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
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['confirm'] = request.form['confirm']


        if session['username'] is not None and session['password'] == session['confirm']:
            Login.loginStorage.addInstructorAccount(session['username'], session['password'])
            return redirect(url_for('instructor_login'))
            
        return render_template('instructor_regist_form.html', message = 'Invalid username or password')

@app.route('/student_Register/', methods=['GET', 'POST'])
def stuRegister():
    """student register page, after register store the data into Persist: {'student'} """
    if request.method =='GET':
        return render_template('student_regist_form.html')
    if request.method =='POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['confirm'] = request.form['confirm']


        if session['username'] is not None and session['password'] == session['confirm']:
            Login.loginStorage.addStudentAccount(session['username'], session['password'])
            return redirect(url_for('stu_login'))

        return render_template('student_regist_form.html', message = 'Invalid username or password')


@app.route('/student_login/', methods=['GET', 'POST'])
def stu_login():
    """Studnt log in page, which get the data from the persist to check whether the student can log in successfully or not"""

    if request.method == 'GET':
        return render_template('student_login.html')

    if request.method == 'POST':


        session['username'] = request.form['username']
        session['password'] = request.form['password']


        if not all([session['username'], session['password']]):
            flash('imcomplete')

        for user in studentAccount:
            # the situation that username exist in the persist and the password should also be in the persist and conform to what user set.
            if session['username'] == user and session['password'] == studentAccount[user]:
                return redirect(url_for('quiz'))
            # the situation that the username is not in the persist
            elif session['username'] != user:
                return render_template('student_login.html', message = 'Account is not exist, Please register first')
            # the situation that the password is not what user set
            elif session['password'] != studentAccount[user]:
                return render_template('student_login.html', message = 'Input the wrong password')
        else:
            return render_template('student_login.html', message = 'Account is not exist, Please register first')

@app.route('/instruct_login/', methods=['GET', 'POST'])
def instructor_login():
    """Instructor log in page, which get the data from the persist to check whether the instructor can log in successfully or not"""

    if request.method == 'GET':

        return render_template('instructor_login.html')

    if request.method == 'POST':

        session['username'] = request.form['username']
        session['password'] = request.form['password']

        if not all([session['username'],session['password']]):
            flash('imcomplete')
                                                                                                                  
        for instruct_user in instructorAccount:
            # the situation that username exist in the persist and the password should also be in the persist and conform to what user set.
            if session['username'] == instruct_user and session['password'] == instructorAccount[instruct_user]:
                return redirect(url_for('createQuiz'))
            # the situation that the username is not in the persist
            elif session['username'] != instruct_user:
                return render_template('instructor_login.html', message = 'Account is not exist, Please register first')
            # the situation that the password is not what user set
            elif session['password'] != instructorAccount[instruct_user]:
                return render_template('instructor_login.html', message = 'Input the wrong password')
        else:
            return render_template('instructor_login.html', message = 'Account is not exist, Please register first')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('base'))

@app.route('/takequiz')
def quiz():
    return render_template('quizzes.html')

@app.route('/createquiz')
def createQuiz():
    return render_template('create_quiz.html')


