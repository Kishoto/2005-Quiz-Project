

import unittest
import tempfile
import os.path


from Persist import Persist

class TestPersist(unittest.TestCase):



    def setUp(self):
        self.pdir = tempfile.TemporaryDirectory()
        self.dfname = os.path.join(self.pdir.name, 'testpersist.dat')
        self.persist = Persist(self.dfname)

    def tearDown(self):
        self.pdir.cleanup()

    def test_addAccount_true(self):
        self.persist.addInstructorAccount("wz1843","1234")
        account = self.persist.getInstructorAccount('wz1843','1234')
        self.assertEqual('1234',account,"not added")
        



    def test_addAccount_false(self):
        self.persist.addStudentAccount("cd1123", "abcd")
        account = self.persist.getInstructorAccount("cd1123", "abcd")
        self.assertNotEqual('abc', account, "not added")


    def test_getAccount_true(self):
        self.persist.addStudentAccount("bbb11", "aaa")
        account = self.persist.getStudentAccount("bbb11", "aaa")
        self.assertEqual('aaa', account, "not added")

    def test_getAccount_false(self):
        self.persist.addStudentAccount("bbb22", "aaaa")
        account = self.persist.getInstructorAccount('bbb222', "aaaa")
        self.assertNotEqual('aaaaa', account, "not get the account")


    def test_delete_true(self):
        self.persist.addStudentAccount("bbb33", "aaaaa")
        self.persist.delete("bbb33")
        print(self.persist.getStudentAccount("bbb33", "aaaaa"))



    def test_delete_false(self):
        self.persist.addStudentAccount("bbb33", "aaaaa")
        self.persist.delete("bbb333")
        print(self.persist.getStudentAccount("bbb33", "aaaaa"))

    def test_addQuiz_true(self):
        self.persist.addQuiz("Quiz1")
        quiz = self.persist.getQuiz("Quiz1")
        print(self.persist.getQuiz("Quiz1"))
    def test_addQuiz_false(self):
        self.persist.addQuiz("Quiz1")
        quiz = self.persist.getQuiz("Quiz1")
        self.assertNotEqual("['attempt3']",quiz,"not added quiz")

    def test_getQuiz_true(self):
        self.persist.addQuiz("Quiz2")
        quiz = self.persist.getQuiz("Quiz2")
        print(self.persist.getQuiz("Quiz2"))

    def test_getQuiz_false(self):
        self.persist.addQuiz("Quiz2")
        quiz = self.persist.getQuiz("Quiz")
        self.assertNotEqual("['attempt1']",quiz,"not get quiz successfully")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPersist('test_addAccount_true'))
    suite.addTest(TestPersist('test_addAccount_false'))
    suite.addTest(TestPersist('test_getAccount_true'))
    suite.addTest(TestPersist('test_getAccount_false'))
    suite.addTest(TestPersist('test_delete_true'))
    suite.addTest(TestPersist('test_delete_false'))
    suite.addTest(TestPersist('test_addQuiz_true'))
    suite.addTest(TestPersist('test_addQuiz_false'))
    suite.addTest(TestPersist('test_getQuiz_true'))
    suite.addTest(TestPersist('test_getQuiz_false'))

    # suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
