from Persist import *
from Quiz_Attempt import QuizAttempt

"""
CLASS:
    TakeQuiz
"""
class TakeQuiz:
    """
    Allow student to take a quiz and store their attempts

    Class Variable:
        persistStorage - persist object
        studentsQA - (dictionary)Each student quiz attempt for a quiz
        Key: username
        Value: dictionary(Key: quizName,
                          Value: List[] of quizAttempt objects)

    Class Methods:
        resumeQuiz(name, quiz) - returns an incomplete quiz attempt if found.
        store_studentsQA() - calls persist method to store studentsQA dictionary in shelve
        get_studentsQA - get stored studentsQA dictionary from persist
        

    Instance Variables:
        username: - student's unique userID
        selectTime - time the quiz was selected
        quizTup - a tuple conatining (createQuiz object, quiz object)
        foundQuiz - the quiz selected by student to be taken
        createdQuiz - the createQuiz object that made the quiz
        presentAttempt - holds information of quiz answered by student
        formerAttempt - indicates True or False if the student is continuing from his last attempt

    Public Methods:
        checkAccess() - verify if student has access to quiz
        getFoundQuiz() - returns the quiz object that the sudent is currently taking
        getQuizContent() - return the quiz content(quizName,question, and choices)
        saveAnswer() - saves student answer to a question
        stopQuiz() - stop and save incomplete quiz attempt for later completion 
        submitQuiz() - submit quiz attempt
        store_studentsQA() - store all the students quiz attempts for each quiz
        numberOfAttempts() - check students number of attempt on a quiz
        
    """
    persistStorage = storage
    studentsQA = {}
    
    
    def __init__(self,username,quizName):
        """
        Initialise instance variables, get the quiz from storage

        Params:
            username -  person taken the quiz
            quizName - Name of the quiz selected
        """
        print(username)
        self._username = username
        self._selectTime = datetime.datetime.now()
        self._foundQuiz = TakeQuiz.persistStorage.getQuiz(quizName)
        self._presentAttempt = QuizAttempt(username, self._foundQuiz)
        oldAttempt = TakeQuiz.resumeQuiz(username,quizName)
        self.formerAttempt = False
        if oldAttempt is not None:
            self._presentAttempt = oldAttempt
            self.formerAttempt = True

    def checkAccess(self):
        """
        Return true if student is listed as permitted to take Quiz,
        has not exceeded max attempts for quiz
        and quiz end date has not exceded.
        """
        print(0)
        print("Username")
        print(self._username)
        print("Access List")
        print(self._foundQuiz.accessList)
        print(" Current Attempt Number")
        print(self.numberOfAttempts())
        print(" Get Attempts")
        print(self._foundQuiz.getAttempts())
        print("Select (Start?) Time")
        print(self._selectTime)
        print("End Time")
        print(self._foundQuiz.getEndTime())
        exceededDate = False
        exceededAttempt = False
        permitted = False
        if self._username in self._foundQuiz.accessList:
            print(1)
            permitted = True
        
        if(self.numberOfAttempts() >= self._foundQuiz.getAttempts() and TakeQuiz.studentsQA[self._username][self._foundQuiz.getQuizName()][-1].getComplete() == True):
            print(2)
            exceededAttempt = True

        if(self._selectTime > self._foundQuiz.getEndTime()):
            print(3)
            exceededDate = True

        if(exceededDate == False and  exceededAttempt == False and permitted):
            return True
        else:
           return False

    def getQuizContent(self):
        """Return the contents of the quiz."""
        name = self._foundQuiz.getQuizName()
        questions = self._foundQuiz.getQuestions()
        choices = self._foundQuiz.getChoices()
        return (name,questions,choices)


    def saveAnswer(self,index, answer):
        """
        Save student answer to a question in a response list.

        Params:
            index - the index where the answer should stored
            answer - the answer student selected in question

        """
        self._presentAttempt.addResponse(index,answer)
        return self._presentAttempt

    def stopQuiz(self):
        """Saves current attempt for later completion; adds the incomplete quizAttempt to studentsQA dictionary."""
        #Ensures the attempt about to be placed is set to incomplete
        self._presentAttempt._complete = False
        
        quizName = self._foundQuiz.getQuizName()
        #If he already has an incomplete quiz do not store
        if self._username in TakeQuiz.studentsQA and quizName in TakeQuiz.studentsQA[self._username]:
            for attempt in TakeQuiz.studentsQA[self._username][quizName]:
                if attempt.getComplete() == False:
                    return
        if self._username in TakeQuiz.studentsQA:
            dictQuiz = TakeQuiz.studentsQA[self._username]
            if quizName in dictQuiz:
                attempts = dictQuiz[quizName]
                attempts.append(self._presentAttempt)
                dictQuiz[quizName] = attempts
            else:
                attempts = []
                attempts.append(self._presentAttempt)
                dictQuiz[quizName] = attempts
        else:
            quizAttempt = []
            quizAttempt.append(self._presentAttempt)
            
            dictQuiz = {}
            dictQuiz[quizName] = quizAttempt
            
            TakeQuiz.studentsQA[self._username] = dictQuiz
        TakeQuiz.store_studentsQA()
                
    @classmethod
    def resumeQuiz(cls,name,quiz):
        """
        Return incomplete Quiz attempt.

        Params:
            name - name of the student
            quiz - name of thae quiz he wants to take
        """
        if name in TakeQuiz.studentsQA:
            dictQuiz = TakeQuiz.studentsQA[name]
            if quiz in dictQuiz:
                attempts = dictQuiz[quiz]
                for attempt in attempts:
                    if attempt.getComplete() == False:#is incomplete:
                        #TakeQuiz.formerAttempt = True
                        return attempt                 #return incomplete attempt      
        

    def submitQuiz(self):
        """
        Set the QuizAttempt status to True when submit button is pressed
        and store quiz attempt in dictionary.
        """
        quizName = self._foundQuiz.getQuizName()
        self._presentAttempt.completed()
        
        #Check student already exist
        if self._username in TakeQuiz.studentsQA:
            dictQuiz = TakeQuiz.studentsQA[self._username]
            #Check if quiz name already exists
            if quizName in dictQuiz:
                #Get all attempts for that quiz
                quizAttempt = dictQuiz[quizName]
                
                if self.formerAttempt == False:
                    quizAttempt.append(self._presentAttempt)
                    dictQuiz[quizName] = quizAttempt
            else:
                quizAttempt = []
                quizAttempt.append(self._presentAttempt)
                dictQuiz[quizName] = quizAttempt
 
            TakeQuiz.studentsQA[self._username] = dictQuiz
        else:
            quizAttempt = []
            quizAttempt.append(self._presentAttempt)
            
            dictQuiz = {}
            dictQuiz[quizName] = quizAttempt
            
            TakeQuiz.studentsQA[self._username] = dictQuiz

        TakeQuiz.store_studentsQA()
        return self._presentAttempt
        
        
    def numberOfAttempts(self):
        """Return the number of attempts the user has on a particular quiz."""
        if self._username not in TakeQuiz.studentsQA:
            return 0
        if self._foundQuiz.getQuizName() not in TakeQuiz.studentsQA[self._username]:
            return 0

        attempts = TakeQuiz.studentsQA[self._username][self._foundQuiz.getQuizName()]
        return len(attempts)
    
    @classmethod
    def store_studentsQA(cls):
        """Store/Persist studentsQA."""
        TakeQuiz.persistStorage.addAllStudentQA(TakeQuiz.studentsQA)
        
    @classmethod
    def get_studentsQA(cls):
        """Gets the studentsQA stored in persist and returns it"""
        return TakeQuiz.persistStorage.getStudentQA()

    def getFoundQuiz(self):
        """Return the current quiz being taken"""
        return self._foundQuiz

        
