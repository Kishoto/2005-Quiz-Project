from Persist import *
from datetime import *
import copy

class CreateQuiz():
    """This module allows an instructor to create a quiz
    such as set the name of the quiz, set the number of
    attempts, the start and end times of the quiz.

    This module also allows the instructor to restrict 
    and give access to students for a quiz
    add and remove questions and add choices and 
    answers to a quiz
    
    Params:
    quiz_name - the name of the quiz 
    attempts - the number of attempts alloted for the quiz
    start_time - the start time for the quiz in datetime 
    end_time - the end time for the quiz in datetime
    
    Returns:
    None"""

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
        as a string and sets that to the name of the quiz
        
        Params:
        name - Quiz name for the given quiz, is a string
        
        Returns:
        None"""
        
        self.name = name

    def _setAttempts(self,attempts):
        """This function takes the number of attempts
        requested and then converts it into an integer

        Params:
        attempts-the number of attmepts for a quiz

        Returns:
        None"""

        self.attempts = attempts
    
    def _setStartTime(self,stime):
        """This function sets the start time
        for the quiz

        Params:
        stime - the time the instructor wants to start the quiz

        Returns:
        None
        """

        self.start_time = stime

    def _setEndTime(self,etime):
        """This functions sets the end time
        for the quiz

        Params:
        etime - the time the instructor wants to end the quiz

        Returns:
        None"""

        self.end_time = etime

    def _addQuestion(self,question,weight):
        """Adds a question to a list of questions for a quiz
        
        Takes both a question as a string and weight
        as an integer
        that are placed into a list which is then placed into 
        a question bank
        
        Params:
        question - The question for a quiz, stored as a string
        weight - The weight for a given question, given as a string,stored 
        as a float variable
        
        Returns:
        None """

        qList = []
        qList.append(question)
        qList.append(float(weight))
        self.question_bank.append(qList)

    def _addChoices(self,*choice):
        """Adds choices to a list of choices a question will 
        provide during a quiz
        
        takes the choices that an instructor wants for a question
        as a string
        then adds it into a choice list
        
        Params:
        choice- stores a choice for a quiz question as a string
        
        Returns:
        None"""

        self.choices.append(choice)

    def _addAnswerKey(self,*ans):
        """Adds the correct answers for a specific question 
        into an answer key list
        
        takes answers as a string and places it into
        the answer key list
        
        Params:
        *ans - the answer or answers that wants to be entered
        
        Returns:
        None"""

        self.answer_key.append(ans)

    def getQuizName(self):
        """This function returns the name of the quiz
        
        Params:
        None
        
        Returns:
        The quiz name that is stored
        """
        return self.name
    
    def getQuestion(self,index):
        """This function returns a specific question name and weight

        This function takes an index as
        an integerprovided by the instructor
        and returns that question which is a string
       
       Params:
       index - the question index the instructor is looking for,
       stored as a string, converted to int
       
       Returns:
       None  """
        question = self.question_bank[int(index)-1]
        return question[0]
    
    def getQuestions(self):
        """This function will return all questions
        in the question as a List
        Each question is a list of two elements
        A question and that question's weight
        
        Params:
        None

        Returns:
        question_bank - the list of questions and weights stored"""

        return self.question_bank

    def getChoice(self,index):
        """This function returns the choices for a specific question
        
        It will take an index an searh the choice list
        for the corresponding index and return it
        
        Params:
        index - stores an index of a choice the instructor wants as a string,
        which is then converted to an int value
        
        Returns:
        Choice/Choices the instructor wanted"""

        return self.choices[int(index)]

    def getChoices(self):
        """This function returns all of the choices
        for a quiz
        
        Params:
        None

        Returns:
        The entire list of choices for a quiz"""

        return self.choices

    def getAnswer(self,index):
        """This function returns a specific answer for a question

        It will take an index as a parameter and find the 
        corressponding index in the answer list and return it
        
        Params:
        index - the index of an answer the instructor wants
        
        Returns:
        answer_key[int(index)] -the specific answer the instructor wants"""

        return self.answer_key[int(index)]

    def getAnswers(self):
        """This function returns all of the 
        answers for a quiz as a List
        
        Params:
        None

        Returns:
        The answer list for the entire quiz
        """        
        
        return self.answer_key

    def getStartTime(self):
        """This function returns the start time
        
        Params:
        None
        
        Returns:
        The start time for a quiz"""
        return self.start_time

    def getEndTime(self):
        """This function returns the end time of a quiz
        
        Params:
        None
        
        Returns:
        The end time for a quiz"""
        return self.end_time
    

    def getAttempts(self):
        """This function returns the attempts
        that were inputted by the instructor
        as a string
        
        Params:
        None
        
        Returns:
        The number of attempts alloted for a quiz"""

        return self.attempts
    
    def getWeight(self,index):
        """This function returns the weight for a specific question
        It will take the index as integer and use that
        to find the specific question weight
        by getting that specific qList item
        and returning the second index
        
        Params:
        index - the index of the question that is requested
        
        Returns:
        Returns the second element in the question list which contains the weight"""

        weight = self.question_bank[index-1]
        
        return weight[1]

   #Editing functionality is not available at this time in flask 
    #def _removeQuestion(self,index):
        #"""This function will remove a question from the quiz and
        #then store it in a shelf

        #It will take an index as integer
        #Using that index it will delte that specific
        #index from the question bank list
        #and then store the objects
        #in the persist module"""
        
        #del self.question_bank[index-1]

    #Editing functionality is not available at this time in flask
    #def _editWeight(self,index,nweight):
       # """This function will edit the weight of a question
        #based on the question number entered
        #by the instructor

        #It will take the index as an integer
        #and the new eight as either an integer/float/double 
        #value and change the current weight for a question
        #"""

        #weight = self.question_bank[index-1]
        #weight[1] = nweight

        #self.question_bank[index] = weight
        
        #self.question_bank
        
        #return

    def _giveAccess(self,name):
        """
        This function places a student's
        name into the quiz access list
        as a string which will 
        determine if they can access this specific quiz 
        
        Params:
        name - the name of the student that can access the quiz
        
        Returns:
        None"""

        self.accessList.append(name)


    def checkAccess(self):
        """
        This function returns the 
        access list for a quiz
        
        Params:
        None
        
        Returns:
        Returns the list of students that this quiz is accessible for"""

        return self.accessList
    
    #Commented this code out, might implement it later into the flask
    #def _removeAccess(self,name):
       # """This function allows the instructor
        #to pass the name as a string
        #and remove the access of that student"""

        #try:
            #for i in self.accessList:
                #if name in self.accessList[i]:
               #     del self.accessList[i]
                #else:
                   # next
        #except ValueError:
           # print("Name not in Access List!")

    def _storeQuiz(self):
        """Stores the quiz using the persist module
        
        This function uses the persist class to store the quiz
        and ensure it persists
        
        Params:
        None
        
        Returns:
        None"""

        storage.addQuiz(self)