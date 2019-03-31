from CreateQuiz import CreateQuiz

from flask import Flask

app = Flask(__name__) 


clientpage = """
<!doctypehtml>
<html>
<h1>
<title>Quiz Setup</title>
Quiz Setup
</h1>
<body>
<div class=setup>
    <form>
        Quiz name: <input type=text size="15" name="quizname" value=""><br>
        <br>
        Number of attempts: <input type=text size=10 name=attemps value=""><br>
        <br>
        Start Time: <input type=date namestime"><br>
        <br>
        End Time: <input type=date name=etime><br>
        <br>
        <button type =button>Create Quiz</button>
    </form>
</body>
</html>
""" 
@app.route('/setupquiz')
def quizSetup():
    return clientpage

