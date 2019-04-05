import sys
sys.path.append('C:/Users/omafu/OneDrive/Documents/GitHub/2005-Quiz-Project/Fume/Comp2005A6/Back-end scripts')
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)


from create_quiz import *
from Take_Quiz import *

#Adding a quiz
quiz1 = CreateQuiz("Process Model", 3, datetime.datetime(2020,12,4,5), datetime.datetime(2020,5,6,7))
quiz1._addQuestion("Unit-test in python was inspired from what programming language?",1)
quiz1._addChoices("Java","C-Sharp","Ruby","JavaScript")
quiz1._addAnswerKey("Java")

quiz1._addQuestion("Which of the following is not a keyword in python?",1)
quiz1._addChoices("self","in","is","barf")
quiz1._addAnswerKey("barf")

quiz1._addQuestion("The name of the model mention in  lecture note 1?",1)
quiz1._addChoices("Water-Fall","Fast-paced","Constructive","Tree")
quiz1._addAnswerKey("Water-Fall")

quiz1._giveAccess("James")
quiz1._storeQuiz()


#Check persist to get the available quizzes
quizes = TakeQuiz.persistStorage.getQuiz()
quizNames = []
for quiz in quizes:
    quizNames.append(quiz)

#Call this when student selects a quiz
activeQuiz = TakeQuiz("James","Process Model")
quizContent = activeQuiz.getQuizContent()

@app.route('/')
def display_quizzes():
    return render_template('quizzes.html', quizNames=quizNames)

@app.route('/quiz.html')
def display_quiz():
    #Check to see if there is a present incomplete quiz by this student.
    activeQuiz = TakeQuiz("James","Process Model")
    incompleteQuiz = TakeQuiz.resumeQuiz("James","Process Model")
    oldResponse = []
    if incompleteQuiz is not None:
        oldResponse = incompleteQuiz.getResponse()
    return render_template('quiz.html', permission=activeQuiz.checkAccess(), oldResponse=oldResponse, name=quizContent[0], questions=quizContent[1], choiceList=quizContent[2])

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
            #activeQuiz._presentAttempt
        jAttempts = TakeQuiz.studentsQA["James"]["Process Model"]
        return render_template('done.html', jAttempts=jAttempts, finished=finished)


if __name__ == '__main__':
    app.run(debug=True)
