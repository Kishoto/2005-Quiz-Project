import unittest
import datetime

from create_quiz import CreateQuiz
from Quiz_Attempt import QuizAttempt

class TestQuizAttempt(unittest.TestCase):
    
    def setUp(self):
        start_time = datetime.datetime(2019,3,21,12)
        end_time = datetime.datetime(2019,3,28,12)
        
        self.quiz1 = CreateQuiz("Process Model",3,start_time, end_time)
        self.quiz1._addQuestion("Which best describes Project management", 1)
        self.quiz1._addQuestion("Stephens methods for managing the software process are:", 1)
        
        self.q1_attempt = QuizAttempt("Fume",self.quiz1)
    
    def test_addResponse(self):
        data = "Stevens"
        index_number = 0
        
        self.q1_attempt.addResponse(index_number,data)
        
        self.assertEqual(self.q1_attempt.getResponse()[index_number],"Stevens", msg="Did not add response to the right index" )

    def test_addResponse_error(self):
        pass

    def test_getResponse(self):
        self.assertEqual(type(self.q1_attempt.getResponse()),type([]))

    def test_getComplete(self):
        self.assertEqual(type(self.q1_attempt.getComplete()),bool)

    def test_completed(self):
        self.q1_attempt.completed()
        self.assertTrue(self.q1_attempt.getComplete())

if __name__ == '__main__':
    unittest.main(verbosity=2)

    
        
                         
