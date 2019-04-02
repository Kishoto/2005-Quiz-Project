from flask import Flask, render_template
app = Flask(__name__)
##from create_quiz import *
##from Take_Quiz import *
##
##quiz1 = CreateQuiz("Process Model", 3, datetime.datetime(2020,12,4,5), datetime.datetime(2020,5,6,7))
##quiz1._storeQuiz()
##activeQuiz = TakeQuiz("James","Process Model")
##quiz


@app.route('/')
def display_quizzes():
    return render_template('quizzes.html')

@app.route('/quiz1.html')
def display_quiz1():
    return render_template('quiz1.html')

@app.route('/done.html')
def display_done():
    return render_template('done.html')


if __name__ == '__main__':
    app.run(debug=True)
