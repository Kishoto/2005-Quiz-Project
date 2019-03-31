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

    Instance Variables:
        username: - student's unique userID
        selectTime - time the quiz was selected
        quizTup - a tuple conatining (createQuiz object, quiz object)
        foundQuiz - the quiz selected by student to be taken
        createdQuiz - the createQuiz object that made the quiz
        presentAttempt - holds information of quiz answered by student

    Public Methods:
        checkAccess() - verify if student has access to quiz
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
        self._username = username
        self._selectTime = datetime.datetime.now()
        self._foundQuiz = TakeQuiz.persistStorage.getQuiz(quizName)
##        self._quizTup = TakeQuiz.persistStorage.getQuiz(quizName)
##        self._foundQuiz = self._quizTup[1]
##        self._createdQuiz = self._quizTup[0]
        self._presentAttempt = QuizAttempt(username, self._foundQuiz)
        oldAttempt = TakeQuiz.resumeQuiz(username,quizName)
        if oldAttempt is not None:
            self._presentAttempt = oldAttempt


    def checkAccess(self):
        """
        Return true if student is listed as permitted to take Quiz,
        has not exceeded max attempts for quiz
        and quiz end date has not exceded.
        """
        exceededDate = False
        exceededAttempt = False
        permitted = False
        if self._username in self._foundQuiz.accessList:
            permitted = True
        
        if(self.numberOfAttempts() >= self._foundQuiz.getAttempts()):
           exceededAttempt = True

        if(self._selectTime > self._foundQuiz.getEndTime()):
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
        """Save student answer to a question in a response list."""
##        if isinstance(index,str) or isinstance(index,int):
##            raise TypeError
        self._presentAttempt.addResponse(index,answer)
        return self._presentAttempt

    def stopQuiz(self):
        """Saves current attempt for later completion; adds the incomplete quizAttempt to studentsQA dictionary."""
        quizName = self._foundQuiz.getQuizName()
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
                
    @classmethod
    def resumeQuiz(cls,name,quiz):
        """Return incomplete Quiz attempt."""
        if name in TakeQuiz.studentsQA:
            dictQuiz = TakeQuiz.studentsQA[name]
            if quiz in dictQuiz:
                attempts = dictQuiz[quiz]
                for attempt in attempts:
                    if attempt.getComplete() == False: #is incomplete:
                        return attempt                 #return incomplete attempt      
        

    def submitQuiz(self):
        """
        Set the QuizAttempt status to True when submit button is pressed
        and store quiz attempt in dictionary.
        """
        self._presentAttempt.completed()
        quizName = self._foundQuiz.getQuizName()
        
        #Check student already exist
        if self._username in TakeQuiz.studentsQA:
            dictQuiz = TakeQuiz.studentsQA[self._username]
            #Check if quiz name already exists
            if quizName in dictQuiz:
                quizAttempt = dictQuiz[quizName]
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
        """Gets the studentsQA stored in persist"""
        return TakeQuiz.persistStorage.getStudentQA()


def quizzesInStorage():
    """Returns a list of all quizzes that the student can choose from"""
    quizzes = storage.getQuiz()
    quizzNames = []
    for quiz in quizzes:
        quizzNames.append(quiz)
    return quizzNames

    
    

        
