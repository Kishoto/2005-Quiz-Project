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
        
##    def addInstructorAccount(self, email, password):
##        """add a created instructor account to the shelve"""
##        account = self._store["instructor"]
##        account[email] = password
##
##        temp = []
##        temp.append(email)
##        self._store[email] = temp
##
##    def addStudentAccount(self, email, password):
##        """add a created student account to the shelve"""
##        account = self._store["student"]
##        account[email] = password
##
##        temp = []
##        temp.append(email)
##        self._store[email] = temp
##
##    def getInstructorAccount(self, email,password):
##        """return a dictionary of all the accounts"""
##        account = self._store["instructor"]
##        account[email] = password
##        if email not in account:
##            print("invalid email, please try again")
##        else:
##            return account[email]
##
##    def getStudentAccount(self, email,password):
##        """return a dictionary of all the accounts"""
##        account = self._store["student"]
##        account[email] = password
##        if email not in account:
##            print("invalid email, please try again")
##        else:
##            return account[email]
##
##
##    def delete(self, email):
##        """delete a created account from shelve"""
##        account1 = self._store["instructor"]
##        account2 = self._store["student"]
##        if email not in account1 or account2:
##            print("invalid email, please try again")
##        else:
##            if email in account1:
##                del account1[email]
##            elif email in account2:
##                del account2[email]


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



