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
        createAccount() - create the new account
        userlogin() - user login method
    """

    loginStorage = storage
    def __init__(self, userType, userID, password):
        """
        initialize the class and indicates all the parameters
        parameter:
            userType: type of user account: instructor or student
            email: user identity, also the key of the account dictionary
            password: value of the key(email)

        """
        #self._store = Persist()
        self._userType = userType
        self._userID = userID
        self._password = password

    def authentication(self,password):
        if len(password) < 8:
            return False


    def createAccount (self, userType, userID, password):
        """
        create account method, which includes two usertype: student and instructor
        parameter:
            userType: type of user account: instructor or student
            email: user identity, also the key of the account dictionary
            password: value of the key(email)
        """
        
        if authentication(password):
            
            if userType == "instructor":
                instructorAccount = {}
                if len(userID) > 0:
                    instructorAccount[userID] = password
                    Login.loginStorage.addInstructorAccount()

            elif userType == "student":
                studentAccount = {}
                if len(userID) > 0:
                    studentAccount[userID] = password
                    Login.loginStorage.addStudentAccount()
            #print("Account has been created")
            return True

        else:
            #print("Password must be 8 characters long")
            return False


    def userlogin (self, userKey, password):
        """
        This method is login method includes password authentication, but it is not finished yet
        parameter:
            userType: type of user account: instructor or student
            userID: user identity, also the key of the account dictionary
        """
        studentAccount = Login.loginStorage.getStudentAccount()
        instructorAccount = Login.loginStorage.getInstructorAccount()

        for userID in studentAccount:
            if userID == userKey:
                if studentAccount[userID] == password:
                    return True

        for userID in InstructorAccount:
            if userID == userKey:
                if InstructorAccount[userID] == password:
                    return True
                
        return False

    
        
