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
        getComplete() - check status of the attempt
        completed()- marks this attempt as completed
        
    """
    
    def __init__(self, username, quiz):
        """Initialise instance variables."""
        self._username = username
        self._quizName = quiz.getQuizName()
        self._quizQuestions = quiz.getQuestions()
        self._quizChoices = quiz.getChoices()
        self._quizAnswers = quiz.getAnswers()
        self._questionWeight = [None] * len(self._quizQuestions)

        for i in range(len(self._quizQuestions)):
            self._questionWeight = quiz.getWeight(i)

        self._response = [None] * len(self._quizQuestions)
        self._complete = False

    def addResponse(self, number, answer):
        """
        Record the answers of the student for this quiz attempt

        Params:
            number - Index number of the question
            answer - students' response from the multiple choice
        """
        self._response[number] = answer
            
    def getResponse(self):
        """Return student response for this particular quiz attempt."""
        return self._response
    
    def getComplete(self):
        """Return True or False to verify complete status of this attempt."""
        return self._complete

    def completed(self):
        """Set status of complete to True for this attempt."""
        self._complete = True

    

    
