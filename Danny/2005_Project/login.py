import Persist

"""
CLASS:
     Login_
"""
class Login:
    """
    Create the instructor account and student account ,also includes a login system

    Instsnce Variables:
        userType - type of the account includes instructor and student two types
        userID - the key of the account which represents the identity
        password - user set it to log into the system

    Public Methods:
        authentication() - authenticate the password is valid or not
        createAccount() - create the new account
        userlogin() - user login method
    """

    loginStorage = Persist.storage
    def __init__(self, userType, userID, password):
        """
        initialize the class and indicates all the parameters
        parameter:
            userType: type of user account: instructor or student
            userID: user identity, also the key of the account dictionary
            password: value of the key(email)

        """

        self._userType = userType
        self._userID = userID
        self._password = password


    def authentication(self,password):
        """
        authenticate the account to see whether the password is valid or not
        :param password: the password which the user input and set
        :return: true if the password length is longer than 8 and return false if the length is less than 8
        """
        if len(password) < 8:
            return False


    def createAccount (self, userType, userID, password):
        """
        create account method, which includes two usertype: student and instructor
        parameter:
            userType: type of user account: instructor or student
            userID: user identity, also the key of the account dictionary
            password: value of the key(email)

        :return: true if the account is been created successfully
        """
        

            
        if userType == "instructor":
            if len(userID) > 0:
                Login.loginStorage.addInstructorAccount(userID,password)

        elif userType == "student":
            if len(userID) > 0:
                Login.loginStorage.addStudentAccount(userID, password)
            return True



    def userlogin (self, userKey, password):
        """
        This method is login method to check whether the userID is in persist or not and check whether the password
        is equal to what the user set
        :parameter:
            userKey: The username which get from the persist
            password: The password which also get from the persist
        :return:
            return true if the user login successfully and return false if does not.
        """
        studentAccount = Login.loginStorage.getStudentAccount()
        instructorAccount = Login.loginStorage.getInstructorAccount()

        for userID in studentAccount:
            if userID == userKey:
                if studentAccount[userID] == password:
                    return True

        for userID in instructorAccount:
            if userID == userKey:
                if instructorAccount[userID] == password:
                    return True
                
        return False
    
        
