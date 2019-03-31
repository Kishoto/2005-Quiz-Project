
The package includes:
Scripts - contains all python files and test files
	create_quiz - creates a quiz and sends it to persist
	Persist - stores other components object to shelve

templates - jinja templates folder for flask

demoenv - virtual environment

TO RUN THE UNIT-TEST:
	$open the file test_take_quiz.py and press 'F5' to test the Take_Quiz module
	$open the file test_quiz_attempt.py and press 'F5' to test the Quiz_Attempt module
	
TO RUN THE FLASK APPLICATION:
    with flask installed the shell commands are:
	Open Terminal

	1. Activate virtual environment: source demoenv/bin/activate

	Scripts can now be run from virtual machine.
        $ export FLASK_APP=Scripts/routes.py
        $ flask run
