"""
CLASS:
    QuizAttempt
"""


class QuizAttempt:
    """
    Holds Attempt information of a an already taken quiz

    Instance Variables:
        quizName - name of quiz
        quizQuestions - list of questions
        quizChoices - list of lists: list of choices for each question
        quizAnswers - list of correct answers to question
        response - student answers for this attempt
        complete - status of the attempt

    Public Methods:
        addResponse(number, answer) - add student's answer to a question
        getResponse() - get student answers
        completed()- marks this attempt as completed
        getComplete() - check status of the attempt
        
    """
    
    def __init__(self,num):
        """Initialise instance variables."""
##        self._quizName = quiz.getName()
##        self._quizQuestions = quiz.getQuestions()
##        self._quizChoices = quiz.getQuizChoices()
##        self._quizAnswers = quiz.getCorrectAnswers()
##
##        self._response = [None] * len(self._quizAnswers)

        self._quizname = 'Quiz'+str(num)
        self._quizQuestions = ['1. How much is a kg?','2. How much is a gram?']
        self._quizChoices = [['A. 3', 'B. 6', 'C. 10'],['A. 10', 'B. 20', 'C. 30']]
        self._quizAnswers =  ['A','C']
        self._response = ['A','B']
        self._quizweights = [num+4,num+1]
        self._complete = True





    def addResponse(self, number, answer):
        """
        Record the answers of the student for this quiz attempt

        Params:
            number - Number of the question
            answer - students' response from the multiple choice

        """
        self._response[number] = answer
            

    def getResponse(self):
        """Return student response for this particular quiz attempt."""
        return self._response

    def completed(self):
        """Set status of complete to True for this attempt."""
        self._complete = True

    def getComplete(self):
        """Return True or False to verify complete status of this attempt."""
        return self._complete

    
