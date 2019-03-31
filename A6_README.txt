NOTE: PLEASE SEE THE CHANGES.TXT FILE FOR NOTES ABOUT CHANGES MADE TO THE DELIVERABLES SINCE ASSIGNMENT 5

Testing Git 1.0

Grading Criteria:
1 - My team's sign off is a printed PDF of emails to Professor Ed Brown titled "Team Sign Off A6.pdf"
2 - My description and UML diagram are in the word document file "A6_Description.docx"  
3 - My use case is in the word document "A6_Use_Case.docx"
4 - I detail the clear connection between my module and its responsbilities in the word document file "A6_Description.docx"
5 - My module is stored in the "QuizResult.py" file and has the appopriate docstrings for the module and each of its functions.
6 - My interface and exports are clearly defined in the "QuizResult.py" file and the associated documentation. They're fully decoupled from all other parts of the project.
7 - The description of my module design is detailed in the word document file "A6_Description.docx"
8 - My instructions for running my module in full are detailed below.
9 - My unit tests are detailed in the "test_quiz_result.py" file and fit criteria A-E for this assignment.
10 - My function implementations are contained within my "QuizResult.py" module.
11 - My minimal flask front end is controlled primarily by the "cliff_app.py" file. The html files are stored in the "templates" folder.
12 - Deliverables 1-11 were resubmitted as instructed; both in updated form and as a zip file with the previous assignment files. 
13 - The implementation of the interface was completed.
14 - The unit tests were fully implemented.

-------------------

Below are instructions for testing the various parts of Assignment 6 for COMP 2005, created by Clifford Bowe, on the CS labnet machines. For the purposes of the test, please use the linux partition of the computer. Pull the files from my "assignment6" repo and place them in a folder named "cliff_a6"


VENV+FLASK TEST
---------------

1. Navigate to the cliff_a6 directory in the terminal
2. Run the command "python3 -m venv testenv"
3. Run the command "source testenv/bin/activate"
4. Run the command "pip install Flask"
5. Run the command "python cliff_app.py"
6. Navigate to the localhost:5000 address in a  web browser.
7. Click through the links to view the grades for separate quizzes, as described in the Use Case. 


UNIT TESTS
----------

1. Navigate to the cliff_a6 directory in the terminal
2. Run the command "python test_quiz_result.py"
3. Observe the results of the tests in standard python unittest format
