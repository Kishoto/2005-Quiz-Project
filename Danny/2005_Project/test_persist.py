

import unittest
import tempfile
import os.path
import Persist

from Persist import Persist

class TestPersist(unittest.TestCase):



    def setUp(self):
        self.pdir = tempfile.TemporaryDirectory()
        self.persist = Persist("test.txt")
    def tearDown(self):
        self.pdir.cleanup()

    def test_addAccount_true(self):
        self.persist.addInstructorAccount("wz1843","1234")
        account = self.persist.getInstructorAccount()
        self.assertEqual('1234', account["wz1843"],"not added")
        



    def test_addAccount_false(self):
        self.persist.addStudentAccount("cd1123", "abcd")
        self.persist.addInstructorAccount("qw1212","qwer")
        account = self.persist.getInstructorAccount()
        self.assertEqual('abcd', account["qw1212"], "not added")


    def test_getAccount_true(self):
        self.persist.addStudentAccount("bbb11", "aaa")
        account = self.persist.getStudentAccount()
        self.assertEqual({'bbb11':'aaa'}, account,"not get the account")

    def test_getAccount_false(self):
        self.persist.addStudentAccount("bbb22", "aaaa")
        account = self.persist.getStudentAccount()
        self.assertEqual({'bbb22':'aaaa'}, account, "not get the account")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPersist('test_addAccount_true'))
    suite.addTest(TestPersist('test_addAccount_false'))
    suite.addTest(TestPersist('test_getAccount_true'))
    suite.addTest(TestPersist('test_getAccount_false'))

    # suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
