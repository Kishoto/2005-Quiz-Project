import shelve
import datetime

class Persist:

    classList = ["James", "Dave", "Vlad", "Tommy", "Fred", "Danny", "Julie", "Divine", "Clifford", "Fume", "Danny", "Samad"]
    def __init__(self, filename):
        self._store = shelve.open(filename, writeback= True)
        self._store["Quiz"] = {}
        self._store["studentAttempt"] = {}
        self._store["gradedAttempts"] = {}
        self._store["instructor"] = {}
        self._store["student"] = {}
        
    def addInstructorAccount(self,userID, password):
        """add a created instructor account to the shelve
            parameter:
                userID: the username that the instructor set as the key of the dict
                password: the password that the instructor set as the value of the key

            :return: None
        """
        instructDict = self._store["instructor"]
        instructDict[userID] = password
        self._store["instructor"] = instructDict

    def addStudentAccount(self, userID, password):
        """add a created student account to the shelve
            parameter:
                userID: the username that the student set as the key of the dict
                password: the password that the student set as the value of the key

            :return: None

        """
        studentDict = self._store["student"]
        studentDict[userID] = password
        self._store["student"] = studentDict

    def getInstructorAccount(self):
        """The method that return a dictionary of all the accounts
            :parameter: None
            :return: The instructor account that be invoked

        """
        instructorAccount = self._store["instructor"]
        return instructorAccount

    def getStudentAccount(self):
        """The method that return a dictionary of all the accounts
            :parameter: None
            :return: The student account that be invoked
        """
        studentAccount = self._store["student"]
        return studentAccount


    def addQuiz(self, quiz_tup):
        """add the instructor's quiz to the shelve
            :parameter:
                quiz_tup: set up a new quiz
            :return: None
        """

        Quiz = self._store["Quiz"]
        Quiz[quiz_tup.getQuizName()] = quiz_tup
        self._store["Quiz"] = Quiz

    def getQuiz(self, quizName=None):
        """The method that get a particular quiz or get all the quiz
            :parameter:
                quizName: The name of the quiz
            :return: Quiz that be invoked
        """
        Quiz = self._store["Quiz"]
        if quizName == None:
            return Quiz
        if quizName in Quiz:
            return Quiz[quizName]
        else:
            raise Exception("The quiz",quizName,"is not in the storage")

    def addAllStudentQA(self, quizAttemptDict):
        """add all students' quiz attempts to shelve
            :parameter:
                quizAttemptDict: The dictionary which stores the attempt times that the quiz be taken.
            :return: None
        """

        quizAttempt = self._store["studentAttempt"]
        quizAttempt = quizAttemptDict
        self._store["studentAttempt"] = quizAttempt

    def getStudentQA(self):
        """ The method that get the student's quiz attempt from the shelve
            :parameter: None
            :return: quizAttempt , the attempt times
        """
        quizAttempt = self._store["studentAttempt"]
        return quizAttempt
    
    def addQuizResult(self, gradedQuiz_dict):
        """add students quizResult to shelve
            :parameter: gradeQuiz_dict: the dictionary that stores the quiz grades
            :return: None
        """
        gradedQuiz = self._store["gradedAttempts"]
        gradedQuiz = gradedQuiz_dict
        self._store["gradedAttempts"] = gradedQuiz

    def getQuizResult(self):
        """The method that get students quizResult from shelve
            :parameter: None
            :return: gradeQuiz: which is the grade of the exact quiz attempt
        """
        gradedQuiz = self._store["gradedAttempts"]
        return gradedQuiz
    
    def close(self):
        self._store.sync()
        self._store.close()

storage = Persist("file.txt")



