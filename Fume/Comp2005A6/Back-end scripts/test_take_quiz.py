import unittest

import datetime
from create_quiz import CreateQuiz
from Take_Quiz import *
    
class TestTakeQuiz(unittest.TestCase):

    def setUp(self):
        self.q1 = CreateQuiz("Process Model",3,datetime.datetime(2020,12,4,5),datetime.datetime(2020,5,6,7))
        self.q1._addQuestion("What is compsci",1)
        self.q1._addChoices("good","bad", "nice")
        self.q1._addAnswerKey("nice")
        self.q1._giveAccess("James")
        self.q1._storeQuiz()
        
        self.activeQuiz = TakeQuiz("James","Process Model")
        self.activeQuiz2 = TakeQuiz("Dave","Process Model")

    def test_checkAccessNo(self):
        self.assertEqual(self.activeQuiz2.checkAccess(), False)

    def test_checkAccessYes(self):
        self.assertEqual(self.activeQuiz.checkAccess(), True)

    def test_getQuizContent(self):
        self.assertEqual(self.activeQuiz.getQuizContent(),("Process Model",self.q1.getQuestions(),self.q1.getChoices()))

    def test_saveAnswer(self):
        attempt = self.activeQuiz.saveAnswer(0,"nice")
        self.assertEqual(attempt.getResponse()[0],"nice")

##    def test_saveAnswerFail1(self):
##        with self.assertRaises(TypeError):
##            self.activeQuiz.saveAnswer(0,9)
##    def test_saveAnswerFail2(self):
##        with self.assertRaises(TypeError):
##            self.activeQuiz.saveAnswer("0","9")

    def test_stopQuiz(self):
        self.activeQuiz.saveAnswer(0,"bad")
        self.activeQuiz.stopQuiz()
        attempts = TakeQuiz.studentsQA["James"]["Process Model"]
        incompleteAttempt = False
        for attempt in attempts:
            if attempt.getComplete() == False:
                incompleteAttempt = True
        self.assertTrue(incompleteAttempt)

    def test_resumeQuiz(self):
        attempt1 = self.activeQuiz.saveAnswer(0,"good")
        self.activeQuiz.stopQuiz()
        attempt2 = self.activeQuiz.resumeQuiz("James","Process Model")
        self.assertEqual(attempt1,attempt2)

    def test_submitQuiz(self):
        attempt_num = len(TakeQuiz.studentsQA["James"]["Process Model"])
        self.activeQuiz.saveAnswer(0,"bad")
        self.activeQuiz.submitQuiz()
        attempt_num2 = len(TakeQuiz.studentsQA["James"]["Process Model"])
        self.assertEqual(attempt_num+1,attempt_num2)
        
    def test_numberOfAttempts(self):
        self.assertEqual(self.activeQuiz.numberOfAttempts(), 0)

    def test_numberOfAttemptsSubmitted(self):
        self.activeQuiz.submitQuiz()
        self.activeQuiz3 = TakeQuiz("James","Process Model")
        self.activeQuiz3.submitQuiz()
        self.assertEqual(self.activeQuiz3.numberOfAttempts(), 2)

    def test_store_studentsQA(self):
        james_attempt1 = self.activeQuiz.submitQuiz()
        studentAttemptDict = TakeQuiz.get_studentsQA()
        james_attempt_list = studentAttemptDict["James"]["Process Model"]
        found = False
        for attempt in james_attempt_list:
            if attempt == james_attempt1:
                found = True
        self.assertTrue(found)
                
if __name__ == '__main__':
    unittest.main(verbosity=2)
