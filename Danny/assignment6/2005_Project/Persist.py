import shelve

class Persist:
    """
    Set up a database to store data which the modules return and provide the format of dictionary for modules.

    Methods:
        addInstructorAccount() - add a created instructor account to the shelve
        addStudentAccount() - add a created student account to the shelve
        getInstructorAccount() -  return a dictionary of the instructor account
        getStudentAccount() - return a dictionary of the student account
        delete() - delete a created account from shelve
        addQuiz() - add the instructor's quiz to the shelve
        getQuiz() - get a particular quiz or get all the quiz

    """


    def __init__(self, fileName):
        self._fileName = fileName
        self._store = shelve.open(fileName, writeback= True)
        self._store["instructor"] = {}
        self._store["student"] = {}
        self._store["Quiz"] = {}




    def addInstructorAccount(self, email, password):
        """
        add a created instructor account to the shelve
        parameter:
            email - key of the account in a dict
            password - value of the key(email)
        """
        account = self._store["instructor"]
        account[email] = password

        temp = []
        temp.append(email)
        self._store[email] = temp

    def addStudentAccount(self, email, password):
        """
        add a created student account to the shelve
        parameter:
            email - key of the account in a dict
            password - value of the key(email)
        """
        account = self._store["student"]
        account[email] = password

        temp = []
        temp.append(email)
        self._store[email] = temp

    def getInstructorAccount(self, email,password):
        """
        return a dictionary of the instructor account
        parameter:
            email - key of the account in a dict
            password - value of the key(email)
        """
        account = self._store["instructor"]
        account[email] = password
        if email not in account:
            print("invalid email, please try again")
        else:
            return account[email]

    def getStudentAccount(self, email,password):
        """return a dictionary of the student account"""
        account = self._store["student"]
        account[email] = password
        if email not in account:
            print("invalid email, please try again")
        else:
            return account[email]


    def delete(self, email):
        """
        delete a created account from shelve
        """

        account1 = self._store["instructor"]
        account2 = self._store["student"]
        if email not in account1 or account2:
            print("invalid email, please try again")
        else:
            if email in account1:
                del account1[email]
            elif email in account2:
                del account2[email]


    def addQuiz(self, quiz):
        """
        add the instructor's quiz to the shelve
        parameter: quiz
        format:
            Quiz = { quiz:[attempt1, attemp2] }
        """

        Quiz = self._store["Quiz"]
        attempt = []
        Quiz[quiz] = attempt
        temp = []
        temp.append(quiz)
        self._store[quiz] = temp

    def getQuiz(self, quiz=None):
        """
        get a particular quiz or get all the quiz
        """

        Quiz = self._store["Quiz"]
        if quiz not in Quiz:
            print("This quiz is not exist")
        else:
            return Quiz[quiz]


    def addQuizResult(self, email=None,quiz=None):
        """
        add students' quiz result to the shelve, results gonna include the quiz name and scores
        parameter: email, quiz
        format:
            quizResult = { email:{ quiz:[result] }}"""

        quizResult = self._store["Quiz"]
        result = []
        quizResult[email][quiz] = result

        if email not in self._store["Account"]:
            print("The student is not exist")

        else:
            temp = []
            temp.append(email)
            self._store[email] = temp


    def addAllStudentQA(self, email=None, quiz=None):
        """
        add all students' quiz attempts to shelve
        parameter: email, quiz
        format:
            quizAttempt = { email: { quiz:[attempt] } }
            """
        quizAttempt = self._store["Quiz"]
        attempt = ['attempt1', 'attempt2']
        quizAttempt[email][quiz] = attempt

        if email not in self._store["Account"]:
            print("The student is not exist")

        else:
            temp = []
            temp.append(email)
            self._store[email] = temp


    def getStudentQA(self, email=None, quiz=None):
        """
        get the student's quiz attempt from the shelve
        parameter: email, quiz
        """
        quizAttempt = self._store["Quiz"]
        if email not in quizAttempt:
            print("The student is not exist")
        else:
            return quizAttempt[email][quiz]


    def removeQuizResult(self, email=None, quiz=None):
        """
        remove the student's quiz result from the shelve
        parameter: email, quiz
        """

        quizResult = self._store["Quiz"]
        if email not in self._store["Account"]:
            print("The student is not exist")
        if quiz not in quizResult:
            print("No such quiz exist")
        else:
            del quizResult[quiz]

    def close(self):
        self._store.sync()
        self._store.close()


class Newuser:
    def __init__(self, email, usertype, password):
        self.email = email
        self.usertype = usertype
        self.password = password

#help(Persist)


