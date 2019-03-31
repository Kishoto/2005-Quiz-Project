
from datetime import date
from CreateQuiz import CreateQuiz
import unittest
import random

class TestCreateQuiz(unittest.TestCase):

    test_date = date(1997,1,19)
    quiz_questions = ("What is the 5th planet from the sun?",
                            "What is the process by which planets create food?",
                            "How many letters are in the English Alphabet?",
                            "In what year did Christopher Columbus discover America?",
                            "What is 2 + 2?",
                            "What colour is the sky?",
                            "What is the 11th Doctor's favourite food?")

    bad_questions = (5,999,68,42,8,25,test_date)
    
    def setUp(self):
        


        self.qname = "Test Quiz"
        self.numofattempts = 3
        self.stime = date.today()
        self.etime = date(2019,3,30)
        self.testCreate = CreateQuiz(self.qname,self.numofattempts,self.stime,self.etime)
        
        self.badname = 999
        self.invalattempts = 0
        self.badstime = 99
        self.badetime = "I solemnly swear that I am up to no good"
        self.badCreate = CreateQuiz(self.badname,self.invalattempts,self.badstime,self.badetime)
    
    def tearDown(self):
        self.testCreate = None
        self.badCreate = None

    def test_getQuizNamePass(self):
        self.assertTrue(isinstance(self.qname,str),"quiz name should be a string!")

    def test_badQuizName(self):
        badfoo = self.badCreate.getQuizName()
        self.assertFalse(isinstance(badfoo,str))

    def test_getStartTimePass(self):
        foo = self.testCreate.getStartTime()
        self.assertEqual(self.stime,foo,"dates do not match!")
        self.assertTrue(isinstance(foo,date),"datatype should be date!")

    def test_badStartTime(self):
        badfoo = self.badCreate.getStartTime()
        self.assertTrue(not isinstance(badfoo,date))

    def test_getQuestion(self):
        test_question = ""
        for i in range(len(self.quiz_questions)):
            if i == 2:
                question = self.quiz_questions[random.randrange(len(self.quiz_questions))]
                weight = random.randrange(1,3)
                test_question = question
                self.testCreate._addQuestion(question,weight)
            else:
                question = self.quiz_questions[random.randrange(len(self.quiz_questions))]
                weight = random.randrange(1,3)
                self.testCreate._addQuestion(question,weight)
    


        self.assertEqual(test_question,self.testCreate.getQuestion(3),"Index retrieved and question asked for did not match")

    def test_badQuestion(self):
        test_question = None
        for i in range(len(self.bad_questions)):
            if i == 2:
                bquestion = self.bad_questions[random.randrange(len(self.bad_questions))]
                weight = random.randrange(1,3)
                test_question = bquestion
                self.testCreate._addQuestion(bquestion,weight)
            else:
                question = self.bad_questions[random.randrange(len(self.bad_questions))]
                weight = random.randrange(1,3)
                self.testCreate._addQuestion(question,weight)

        self.assertEqual(test_question,self.testCreate.getQuestion(3),"Index retrieved and question asked did not match")
        self.assertFalse(isinstance(self.testCreate.getQuestion(3),str))

    

    def test_getQuestions(self):
        test_list = []
        for i in range(len(self.quiz_questions)):
            question = self.quiz_questions[random.randrange(len(self.quiz_questions))]
            weight = random.randrange(1,3)
            test_tuple = [question,weight]
            test_list.append(test_tuple)
            self.testCreate._addQuestion(question,weight)

        
        self.assertEqual(test_list,self.testCreate.getQuestions(),"Questions not being stored correctly, check usage of getQuestions")


    def test_badQuestions(self):
        test_list = []
        for i in range(len(self.bad_questions)):
            bquestion = self.bad_questions[random.randrange(len(self.bad_questions))]
            weight = random.randrange(1,3)
            test_tuple = [bquestion,weight]
            test_list.append(test_tuple)
            self.testCreate._addQuestion(bquestion,weight)


        self.assertEqual(test_list,self.testCreate.getQuestions(),"Questions are not being stored correctly, check usage of getQuestions or _addQuestion")
        self.assertFalse(isinstance(self.testCreate.getQuestions(),str))
        

    def test_getWeight(self):
        test_weight = 0
        for i in range(len(self.quiz_questions)):
            if i == 2:
                question = self.quiz_questions[random.randrange(len(self.quiz_questions))]
                weight = random.randrange(1,3)
                test_weight = weight
                self.testCreate._addQuestion(question,weight)
            else:
                question = self.quiz_questions[random.randrange(len(self.quiz_questions))]
                weight = random.randrange(1,3)
                self.testCreate._addQuestion(question,weight)

        self.assertEqual(test_weight,self.testCreate.getWeight(3),"Weight asked for does not match weight that should be stored in that index!")

    def test_badWeight(self):
        for i in range(len(self.quiz_questions)):
            bquestion = self.quiz_questions[random.randrange(len(self.quiz_questions))]
            weight = random.randrange(1,3)
            self.testCreate._addQuestion(bquestion,weight)
        
        self.assertTrue(isinstance(self.testCreate.getWeight(2),int))

if __name__ == '__main__':
    unittest.main(verbosity=2)