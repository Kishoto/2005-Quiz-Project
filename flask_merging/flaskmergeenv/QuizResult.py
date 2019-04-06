from random import *
from Quiz_Attempt import *
from Persist import *

"""
CLASS:
    QuizResult
"""

class QuizResult:

    """
    Allow student to take a quiz and store their attempts

    Class Variable:
        input_dict - (dictionary) The QA data that's stored in Persist by the TakeQuiz module
        Key: username
        Value: dictionary(Key: quizName,
                          Value: List[] of quizAttempt objects)


        _quiz_dict - (dictionary) The reformatted quiz data from the QA data
        Key: quizname
        Value: List[] of data(username (str), list of questions (list), list of choices (list of lists), list of responses (lists),
               list of correct answers (list), list of question weights (list)


        _quiz_graded - (dictionary) The reformatted quiz data from the _quiz_dict; it's identical in format
                                    but grades are added to the end of each entry data
        Key: quizname
        Value: List[] of data(username (str), list of questions (list), list of choices (list of lists), list of responses (lists),
               list of correct answers (list), list of question weights (list), grade (float)
                          

    
        sample_quiz_dict - A holder for sample data for demonstrative purposes (NOT PART OF FINAL MODULE)
        attempt1 - A holder for sample data for demonstrative purposes (NOT PART OF FINAL MODULE)
        attempt2 -  holder for sample data for demonstrative purposes (NOT PART OF FINAL MODULE)

    Public Methods:
        add_quiz_attempts() - adds the QA information to the _quiz_dict member  variable
        get_grades() - returns the graded quiz data
        grade() - Grades the given quiz data
        ins_class_part() - Calculates the class participation of a given quiz
        ins_class_hist() - Calculates the class histogram of a given quiz
        ins_class_attempts() - Calculates the number of attempts each student took on a given quiz
        ins_student_grades() - Calculates the grade summary of a given student
        stu_quiz_grades() - Calculates the grade summary of a given student
        stu_quiz_detailed() - Calculates the detailed grade summary of a given quiz for a given student
        
    """

    #Note: The data below was used for demonstrative purposes, as was the Quiz Attempt
    #module. The persist interactions are present but have been commented out with a triple pound
    #sign to indicate where they occur. 
    attempt1 = QuizAttempt(1)
    attempt2 = QuizAttempt(2)
    
    ###sample_quiz_dict = {'Fume' : { 'Quiz1': [attempt1, attempt2], 'Quiz2': [attempt1]}, 'Vlad' : { 'Quiz1': [attempt1, attempt2], 'Quiz2': [attempt1]}}


    QR_PER = storage
    QR_PER.addAllStudentQA({'Fume' : { 'Quiz1': [attempt1, attempt2], 'Quiz2': [attempt1]}, 'Vlad' : { 'Quiz1': [attempt1, attempt2], 'Quiz2': [attempt1]}})

    sample_quiz_dict = storage.getStudentQA()



    ## This dictionary will hold all of the quiz attempts and their relevant information as a dictionary where the keys
    ##are the quiz names and the values are lists containing [course, studentemail, list of questions, list of lists of choices, list
    ##of responses and list of correct answers. There will be a list for each attempt.
    input_dict = {}
    _quiz_dict = {}

    ##This dictionary will look like the previous; the only difference will be that the values of its list will have an additional
    ##value at the end; the grade as a floating point number. 
    _quiz_graded = {}

    def __init__(self):
        """This initializes the quiz result object.
        Params: None

        Returns: None 

        """
        

            

    def add_quiz_attempts(self):
        """This iterates over the quiz attempts dictionary and adds the information to the quiz result object's dictionary.
        Params: None

        Returns: A list of strings; formatted to show the number of attempts all student have made. 


        """
        self.input_dict = self.QR_PER.getStudentQA()
        ###self.input_dict = self.sample_quiz_dict  ##Sample data of the format we'd be pulling from Persist
        for stuname, quizinfo in self.input_dict.items():
            for quizname, attempt in quizinfo.items():
                for i in range(len(attempt)):
                    if quizname not in self._quiz_dict:
                        self._quiz_dict[quizname] = [[ stuname, attempt[i]._quizQuestions, attempt[i]._quizChoices, attempt[i]._response, attempt[i]._quizAnswers, attempt[i]._quizweights]]
                    else:
                        self._quiz_dict[quizname].append([stuname, attempt[i]._quizQuestions, attempt[i]._quizChoices, attempt[i]._response, attempt[i]._quizAnswers, attempt[i]._quizweights])
                       

    def get_grades(self):
        """This function returns the dictionary member variable that will contain all of our graded quiz attempts
        Params: None


        Returns: The dictionary member variable that will contain all of the graded quiz attempts.


        """
        self.grade()
        return self._quiz_graded



        
    def grade(self):
        """This function will grade the quiz attempts and then store the highest scored attempt, along with all of its information, in the dictionary member variable.
        Params: None
        
        Returns: None      

        """
        for name_of_quiz, attempt_lists in self._quiz_dict.items():
            for att in attempt_lists:
                corr = float(0)
                w = sum(att[5])
                for i in range(len(att[1])):
                    if att[3][i] == att[4][i]:
                        corr = corr + (1.0*att[5][i])
                grade = round((corr/float(w))*100,2)


                temp = att
                temp2 = []
                for i in range(len(temp)):
                    temp2.append(temp[i])
                temp2.append(grade)
                
                if name_of_quiz not in self._quiz_graded:
                    self._quiz_graded[name_of_quiz] = [temp2]
                else:
                    self._quiz_graded[name_of_quiz].append(temp2)
        
        
    

    def ins_class_part(self,quizname):
        """This function will calculate the class participation and return it as a string.

        Params:
        quizname - Name of the given quiz

        Returns: A float representing the class participation of the classs on a given quiz. 

        """

        
        size = float(len(self.QR_PER.classList))
        ###size = float(2)  #A temp variable to work with the sample data. 
        part = float(0)
        stunames = {}

        for name_of_quiz, attempt_lists in self._quiz_dict.items():
            for att in attempt_lists:
                if name_of_quiz == quizname and att[0] not in stunames:
                    stunames[att[0]] = ''
                    part = part+1
        part = part*100
        out = part/size
        return float(round(out,2))

    def ins_class_avg(self,quizname):
        """This function will calculate the class average of a quiz and return it as a float.

        Params:
        quizname - Name of the given quiz

        Returns: A float value representing the class average on the given quiz. 


        """
        stunames = {}
        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            for att in attempt_lists:
                if att[0] not in stunames:
                    stunames[att[0]] = att[6]
                else:
                    if stunames[att[0]] < att[6]:
                        stunames[att[0]] = att[6]

        count = len(stunames)
        total = float(0)

        for grade in stunames.values():
            total = total + grade

        return round(total/count,2)
            

    def ins_class_hist(self,quizname):
        """This function will return the grade distribution histogram as a dictionary with increments as keys and number of students as values.

        Params:
        quizname - Name of the given quiz

        Returns: A dictionary with strings representing grade increments as keys and
                the number of students that scored in that interval as integer values. 


        """
        stunames = {}
        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            if name_of_quiz == quizname:
                for att in attempt_lists:
                    if att[0] not in stunames:
                        stunames[att[0]] = att[6]
                    else:
                        if stunames[att[0]] < att[6]:
                            stunames[att[0]] = att[6]
                        

        temp = {'zero':0,'one': 0,'two': 0,'three': 0,'four': 0,'five': 0,'six': 0,'seven': 0,'eight': 0,'nine': 0}

        for grade in stunames.values():
            if grade >= 0 and grade < 10:
                temp['zero'] = temp['zero']+1
            if grade >= 10 and grade < 20:
                temp['one'] = temp['one']+1
            if grade >= 20 and grade < 30:
                temp['two'] = temp['two']+1
            if grade >= 30 and grade < 40:
                temp['three'] = temp['three']+1
            if grade >= 40 and grade < 50:
                temp['four'] = temp['four']+1
            if grade >= 50 and grade < 60:
                temp['five'] = temp['five']+1
            if grade >= 60 and grade < 70:
                temp['six'] = temp['six']+1
            if grade >= 70 and grade < 80:
                temp['seven'] = temp['seven']+1
            if grade >= 80 and grade < 90:
                temp['eight'] = temp['eight']+1
            if grade >= 90 and grade < 101:
                temp['nine'] = temp['nine']+1

        return temp
            
    def ins_class_attempts(self,quizname):
        """This function will return the number of attempts by students on a given quiz as a list.

        Params:
        quizname - Name of the given quiz

        Returns: A list of strings; formatted to show the number of attempts all student have made. 


        """

        stunames = {}
        out_list = []
        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            if name_of_quiz == quizname:
                for att in attempt_lists:
                    if att[0] not in stunames:
                        stunames[att[0]] = 0
                    else:
                        stunames[att[0]] = stunames[att[0]]+1

        for names, atts in stunames.items():
            out_list.append(names +" - " + str(atts))
        return out_list

    def ins_student_grades(self,studentname):
        """This function will return a list of strings containing the grades of a given student on all of their quizzes.

        Params:
        quizname - Name of the given student

        Returns: A list of strings; formatted to show the student's grade on all their quizzes. 


        """
        stunames = {}
        out_list = []

        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            for att in attempt_lists:
                if att[0] not in stunames:
                    stunames[att[0]] = [[name_of_quiz,att[6]]]
                else:
                    stunames[att[0]].append([name_of_quiz,att[6]])

        namehold = ''
        temp = 1
        if studentname in stunames:
            for i in range(len(stunames[studentname])):
                if namehold != '':
                    if stunames[studentname][i][0] == namehold:
                        temp = temp + 1
                    else:
                        temp = 1            
                out_list.append(stunames[studentname][i][0]+ " = Attempt " + str(temp) + " - " + str(stunames[studentname][i][1]))
                namehold = stunames[studentname][i][0]
        return out_list

    def stu_quiz_grades(self,studentname):
        """This function will return a list of strings containing the summary of the student's grades by quiz.

        Params:
        studentname - Name of the given student

        Returns: A list of strings; formatted to show a summary of the student's grades. 


        """
        stunames = {}
        out_list = []

        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            for att in attempt_lists:
                if att[0] not in stunames:
                    stunames[att[0]] = [[name_of_quiz,att[6]]]
                else:
                    stunames[att[0]].append([name_of_quiz,att[6]])

        namehold = ''
        temp = 1

        if studentname in stunames:
            for i in range(len(stunames[studentname])):
                if namehold != '':
                    if stunames[studentname][i][0] == namehold:
                        temp = temp + 1
                    else:
                        temp = 1            
                out_list.append(stunames[studentname][i][0]+ " = Attempt " + str(temp) + " - " + str(stunames[studentname][i][1]))
                namehold = stunames[studentname][i][0]
        return out_list

    def stu_quiz_detailed(self,studentname,quizname):
        """This function will return a string with the breakdown of a given quiz by a given student.


        Params:
        studentname - Name of the given student 
        quizname - Name of the given quiz

        Returns: A list of strings; formatted to show the given student's grades on a given quiz. 


        """

        stunames = {}
        out_list = []


        for name_of_quiz, attempt_lists in self._quiz_graded.items():
            for att in attempt_lists:
                if att[0] not in stunames:
                    stunames[att[0]] = [[name_of_quiz,att[6]]]
                else:
                    stunames[att[0]].append([name_of_quiz,att[6]])

        namehold = ''
        temp = 1
        if studentname in stunames:
            for i in range(len(stunames[studentname])):
                if quizname == stunames[studentname][i][0]:
                    if namehold != '':
                        if stunames[studentname][i][0] == namehold:
                            temp = temp + 1
                        else:
                            temp = 1            
                    out_list.append(stunames[studentname][i][0]+ " = Attempt " + str(temp) + " - " + str(stunames[studentname][i][1]))
                    namehold = stunames[studentname][i][0]
        return out_list

        
test = QuizResult()
test.add_quiz_attempts()
test.get_grades()
print(test.ins_class_hist('Quiz1'))
        
