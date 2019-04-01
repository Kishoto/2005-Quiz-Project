import Persist


"""
CLASS:
     Login_
"""
class Login_:
    """
    Create the instructor account and student account ,also includes a login system

    Instsnce Variables:
        userType - type of the account includes instructor and student two types
        email - the key of the account which represents the identity
        password - user set it to log into the system

    Public Methods:
        createAccount() - create the new account
        userlogin() - user login method
    """


    def __init__(self, userType, email, password):
        """
        initialize the class and indicates all the parameters
        parameter:
            userType: type of user account: instructor or student
            email: user identity, also the key of the account dictionary
            password: value of the key(email)

        """
        self._store = Persist
        self._userType = userType
        self._email = email
        self._password = password


    def createAccount (self, userType, email, password):
        """
        create account method, which includes two usertype: student and instructor
        parameter:
            userType: type of user account: instructor or student
            email: user identity, also the key of the account dictionary
            password: value of the key(email)
        """
        if userType == "instructor":
            instructoraccount = {}
            if len(email) > 0 and len(password) > 0:
                instructoraccount[email] = password
                self._store.Persist.addInstructorAccount()

        elif userType == "student":
            studentaccount = {}
            if len(email) > 0 and len(password) > 0:
                studentaccount[email] = password
                self._store.Persist.addStudentAccount()

        else:
            print("Can't create account")


    def userlogin (self, email, password):
        """
        This method is login method includes password authentication, but it is not finished yet
        parameter:
            userType: type of user account: instructor or student
            email: user identity, also the key of the account dictionary
        """
        accounts = {}
        for p in accounts:
            """this sentence is the password authentication """
            if p.key != email:
                print("No such email exist")
            else:
                if accounts[email] == password:
                    pass
                else:
                    print("wrong password")

        return False

    def authentication(self, email, password):

        persist = Persist.Persist(True)
        user = persist.getStudentAccount(email, password)
        return user._email == email and user._password == password
