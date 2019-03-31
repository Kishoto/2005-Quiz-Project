import unittest
from QuizResult import *

class test_quiz_result(unittest.TestCase):

    test_object = QuizResult()
    real_d = {'0 - 9':0,'10 - 19': 0,'20 - 29': 0,'30 - 39': 0,'40 - 49': 0,'50 - 59': 0,'60 - 69': 0,'70 - 79': 2,'80 - 89': 0,'90 - 100': 0}


    def test_add_quiz_good(self):
        obj = {}
        x = self.test_object.get_grades()
        if len(x.keys()) < 1:
            x = 'fail'
        self.assertEqual(type(obj),type(x),msg="The add_quiz_attempt function isn't working  properly.")

    def test_add_quiz_bad(self):
        obj = {}
        x = self.test_object.get_grades()
        if len(x.keys()) < 1:
            x = 'fail'
        self.assertEqual(type(obj),type(x),msg="The add_quiz_attempt function isn't working  properly.")

    
    def test_ins_part_good(self):
        out = self.test_object.ins_class_part('Quiz1')
        x = 'pass'
        if float(out) < 0 or float(out) > 100:
            x = 'fail'
        self.assertEqual(x,'pass',msg="The ins_class_part function isn't working  properly.")

    def test_ins_part_bad(self):
        out = self.test_object.ins_class_part('Quiz1')
        x = 'pass'
        if float(out) < 0 or float(out) > 100:
            x = 'fail'
        self.assertEqual(x,'pass',msg="The ins_class_part function isn't working  properly.")

    def test_ins_avg_good(self):
        out = self.test_object.ins_class_part('Quiz1')
        x = 'pass'
        if float(out) < 0 or float(out) > 100:
            x = 'fail'
        self.assertEqual(x,'pass',msg="The ins_class_part function isn't working  properly.")

    def test_ins_avg_bad(self):
        out = self.test_object.ins_class_part('Quiz1')
        x = 'pass'
        if float(out) < 0 or float(out) > 100:
            x = 'fail'
        self.assertEqual(x,'pass',msg="The ins_class_part function isn't working  properly.")

    def test_ins_hist_good(self):
        d = self.test_object.ins_class_hist('Quiz1')
        x = 'pass'
        for i in d:
            if d[i] != self.real_d[i]:
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_class_hist function isn't working  properly.")

    def test_ins_hist_bad(self):
        d = self.test_object.ins_class_hist('Quiz1')
        x = 'pass'
        for i in d:
            if d[i] != self.real_d[i]:
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_class_hist function isn't working  properly.")

    def test_ins_att_good(self):
        x = 'pass'
        l = self.test_object.ins_class_attempts('Quiz1')
        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_class_attempts function isn't working  properly.")
        

    def test_ins_att_bad(self):
        x = 'pass'
        l = self.test_object.ins_class_attempts('Quiz1')
        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_class_attempts function isn't working  properly.")


    def test_ins_grade_good(self):
        x = 'pass'
        l = self.test_object.ins_student_grades('Fume')

        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_student_grades function isn't working  properly.")
        

    def test_ins_grade_bad(self):
        x = 'pass'
        l = self.test_object.ins_student_grades('Fume')
        l[0] = 'Quiz 1 = Attempt 1 - 89, Attempt 2 - 72'
        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The ins_student_grades function isn't working  properly.")

    def test_stu_grade_good(self):
        x = 'pass'
        l = self.test_object.stu_quiz_grades('Fume')
        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The stu_quiz_grades function isn't working  properly.")
        

    def test_stu_grade_bad(self):
        x = 'pass'
        l = self.test_object.stu_quiz_grades('Fume')
        l[0] = 'Quiz 1 = Attempt 1 - 89, Attempt 2 - 72'
        for i in range(len(l)):
            if str(type(l[i])) != "<class 'str'>":
                x = 'fail'
            
        self.assertEqual(x,'pass',msg="The stu_quiz_grades function isn't working  properly.")

    def test_stu_det_good(self):
        x = 'pass'
        l = self.test_object.stu_quiz_detailed('Fume','Quiz1')
        if str(type(l)) != "<class 'list'>":
            x = 'fail'
            
        self.assertEqual(x,'pass',msg="The stu_quiz_detailed function isn't working  properly.")
        

    def test_stu_det_bad(self):
        x = 'pass'
        l = self.test_object.stu_quiz_detailed('Fume','Quiz1')
        if str(type(l)) != "<class 'list'>":
            x = 'fail'
            
        self.assertEqual(x,'pass',msg="The stu_quiz_detailed function isn't working  properly.")  



if __name__ == '__main__':
    unittest.main(verbosity=2)

