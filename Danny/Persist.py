import shelve
import datetime

class Persist:

    classList = ["James", "Dave", "Vlad", "Tommy", "Fred", "Danny", "Julie", "Divine", "Clifford", "Fume", "Danny", "Samad"]
    def __init__(self):
        self._store = shelve.open("file.txt", writeback= True)
        self._store["Quiz"] = {}
        self._store["studentAttempt"] = {}
        self._store["gradedAttempts"] = {}
        self._store["instructor"] = {}
        self._store["student"] = {}
        
    def addInstructorAccount(self,userID,password):
        """add a created instructor account to the shelve"""
        instructDict = self._store["instructor"]
        instructDict[userID] = password
        self._store["instructor"] = instructDict

    def addStudentAccount(self, userID,password):
        """add a created student account to the shelve"""
        studentDict = self._store["student"]
        studentDict[userID] = password
        self._store["student"] = studentDict

    def getInstructorAccount(self):
        """return a dictionary of all the accounts"""
        instructorAccount = self._store["instructor"]
        return instructorAccount

    def getStudentAccount(self):
        """return a dictionary of all the accounts"""
        studentAccount = self._store["student"]
        return studentAccount


    def addQuiz(self, quiz_tup):
        """add the instructor's quiz to the shelve"""

        """Quiz = { quiz:[attempt1, attemp2] }"""
        Quiz = self._store["Quiz"]
        Quiz[quiz_tup.getQuizName()] = quiz_tup
        self._store["Quiz"] = Quiz

    def getQuiz(self, quizName=None):
        """get a particular quiz or get all the quiz"""
        Quiz = self._store["Quiz"]
        if quizName == None:
            return Quiz
        if quizName in Quiz:
            return Quiz[quizName]
        else:
            raise Exception("The quiz",quizName,"is not in the storage")

    def addAllStudentQA(self, quizAttemptDict):
        """add all students' quiz attempts to shelve"""
        """quizAttempt = { email: { quiz:[attempt] } }"""
        quizAttempt = self._store["studentAttempt"]
        quizAttempt = quizAttemptDict
        self._store["studentAttempt"] = quizAttempt

    def getStudentQA(self):
        """ get the student's quiz attempt from the shelve"""
        quizAttempt = self._store["studentAttempt"]
        return quizAttempt
    
    def addQuizResult(self, gradedQuiz_dict):
        """add students quizResult to shelve """
        gradedQuiz = self._store["gradedAttempts"]
        gradedQuiz = gradedQuiz_dict
        self._store["gradedAttempts"] = gradedQuiz

    def getQuizResult(self):
        """get students quizResult from shelve """
        gradedQuiz = self._store["gradedAttempts"]
        return gradedQuiz
    
    def close(self):
        self._store.sync()
        self._store.close()

storage = Persist()



