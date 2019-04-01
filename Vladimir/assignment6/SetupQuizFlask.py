from CreateQuiz import CreateQuiz

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__) 

@app.route('/editquiz')
def edit():
    return render_template('QuestionCreation.html')

clientpage = """
<!doctypehtml>
<html>
<h1>
<title>Quiz Setup</title>
Quiz Setup
</h1>
<body>
<div class=setup>
    <form action="http://127.0.0.1:5500/editquiz">
        Quiz name: <input type=text size="15" name="quizname" value=''><br>
        <br>
        Number of attempts: <input type=text size=10 name=attemps value=''><br>
        <br>
        Start Time: <input type="date" name="stime" value=''><br>
        <br>
        End Time: <input type="date" name="etime" value=''><br>
        <br>
        <input type="submit" value="Create Quiz">
    </form>
</body>
</html>
""" 
@app.route('/setupquiz')
def quizSetup():
    return clientpage
