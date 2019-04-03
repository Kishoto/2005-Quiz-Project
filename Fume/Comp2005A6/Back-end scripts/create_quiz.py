from Persist import *

class CreateQuiz():
    
    def __init__(self,quiz_name,attempts,start_time,end_time):
        self.name = quiz_name
        self.attempts = attempts
        self.start_time = start_time
        self.end_time = end_time

        self.question_bank = []
        self.choices = []
        self.answer_key = []
        self.accessList = []

    
    def _setQuizName(self,name):
        """This function takes the name of the quiz
        as a string and sets that to the name of the quiz"""
        
        self.name = name

    def _addQuestion(self,question,weight):
        """Adds a question to a list of questions for a quiz
        
        Takes both a question as a string and weight
        as an integer
        that are placed into a list which is then placed into 
        a question bank"""

        qList = []
        qList.append(question)
        qList.append(weight)
        self.question_bank.append(qList)

    def _addChoices(self,*choice):
        """Adds choices to a list of choices a question will 
        provide during a quiz
        
        takes the choices that an instructor wants for a question
        as a string
        then adds it into a choice list"""

        self.choices.append(choice)

    def _addAnswerKey(self,*ans):
        """Adds the correct answers for a specific question 
        into an answer key list
        
        takes answers as a string and places it into
        the answer key list"""

        self.answer_key.append(ans)

    def getQuizName(self):
        """This function returns the name of the quiz"""
        return self.name
    
    def getQuestion(self,index):
        """This function returns a specific question name and weight

        This function takes an index as
        an integerprovided by the instructor
        and returns that question which is a string
        """
        question = self.question_bank[index]
        return question[0]
    
    def getQuestions(self):
        """This function will return all questions
        in the question as a List
        Each question is a list of two elements
        A question and that question's weight"""

        return self.question_bank

    def getChoice(self,index):
        """This function returns the choices for a specific question
        
        It will take an index an searh the choice list
        for the corresponding index and return it"""

        #return choices[index]

    def getChoices(self):
        """This function returns all of the choices
        for a quiz"""

        return self.choices

    def getAnswer(self,index):
        """This function returns a specific answer for a question

        It will take an index as a parameter and find the 
        corressponding index in the answer list and return it"""

        #return answer_key[index]

    def getAnswers(self):
        """This function returns all of the 
        answers for a quiz as a List"""
        
        return self.answer_key

    def getStartTime(self):
        """This function returns the start time"""
        return self.start_time

    def getEndTime(self):
        """This function returns the end time of a quiz"""
        return self.end_time
    

    def getAttempts(self):
        """This function returns the attempts
        that were inputted by the instructor
        as a string"""

        return self.attempts
    
    def getWeight(self,index):
        """This function returns the weight for a specific question
        It will take the index as integer and use that
        to find the specific question weight
        by getting that specific qList item
        and returning the second index"""

        weight = self.question_bank[index]
    
    def _removeQuestion(self,index):
        """This function will remove a question from the quiz and
        then store it in a shelf

        It will take an index as integer
        Using that index it will delte that specific
        index from the question bank list
        and then store the objects
        in the persist module"""
        
        del self.question_bank[index]

    def _editWeight(self,index,nweight):
        """This function will edit the weight of a question
        based on the question number entered
        by the instructor

        It will take the index as an integer
        and the new eight as either an integer/float/double 
        value and change the current weight for a question
        """

        weight = self.question_bank[index]
        weight[1] = nweight

        self.question_bank[index] = weight
        
        self.question_bank
        
        return

    def _giveAccess(self,name):
        """
        This function places a student's
        name into the quiz access list
        as a string which will 
        determine if they can access this specific quiz 
        """
        self.accessList.append(name)

    def _removeAccess(self,name):
        """This function allows the instructor
        to pass the name as a string
        and remove the access of that student"""

        try:
            for i in self.accessList:
                if name in self.accessList[i]:
                    del self.accessList[i]
                else:
                    next
        except ValueError:
            print("Name not in Access List!")

    def copyQuiz(self):
        """This function makes a deep copy
        of the quiz object and returns it
        which is only accessible by the instructor
        for that quiz in specific"""

        self.quizCopy = copy.deepcopy(q)

        return self.quizCopy

    def _storeQuiz(self):
        """Stores the quiz using the persist module
        
        This function uses the persist class to store the quiz
        and ensure it persists"""
        #Quiz.storage.addQuiz((self,self.q))
        storage.addQuiz(self)












