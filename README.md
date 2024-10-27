Install Python 3.13 and pip.
For these steps please consolidate the linux, mac or windows manuals of python.
https://docs.python.org/3/whatsnew/3.13.html
######################################################################################
Install mysql and import the database habittrackerapp.sql
The Mysql Database was set to autoincrement the primaryKeys of all tables and ensure the uniqueness of them.

Setup the username and password and ensure read and write access to the imported tables: 

Username:Hausmann
Password:Test123
###################################################################################
Next install the mysql-connector-python with pip and the pytest, pytest-mock package:
for example: 
cd C:\Users\admin\AppData\Local\Programs\Python\Python313\Scripts
pip install mysql-connector-python pytest pytest-mock 

Add the pytest path to your system environment variables

Store all .py files from the GitHub Repository in one folder. 
For example: C:\Downloads\Habittracker

Store all the Test*.py files in a children repository of this folder. 
For example C:\Downloads\Habittracker\test
#####################################################################################
The testsuite is split up in multiple testcases.

To test the main and analyzation menu call: "pytest MenuTest.py -s" from the test directory over the cli. 

To test all functions from the function.py file call: "pytest TestFunctions.py -s" from the test directory over cli. Ensure that the database connection is possible and that the
database is filled with the provided data. Some test cases are relying on the provided testdata. 

To test the analyzation functions please call "pytest analyzationTest.py -s" from the test directory over the cli.

To test the scheduler please call "pytest schedulerTest.py -s" from the test directory over the cli.
######################################################################################
To run and interact with the application open the CMD/CLI and call the main.py file. 
For example: C:\Downloads\Habittracker\main.py

The application is controlled over a simple menu. The cli will request an input from the user:
1=Create new habit
2=Create new period
3=Display all habits
4=Display all periods
5=Edit an existing habit. In the following menu users can enter 1 to change the period of an existing habit or 2 to delete a habit.
6=Mark a habit as executed
7=Load the analyzation menu. In this menu users have the chance to analyze their habits. 
	1=Display top Highscore of all habits 
	2=Display top Highscore of a specific period 
	3=Display all habits
	4=Display all habits with a specific period
	5=Return the highscore of a specific habit
	6=Turn back to the main menu
8=Close the application

The menu from here on should be self explainatory. As a last example, if the user wants to see the highscore of a specific habit, he would press 7 to enter the analyzation menu
from there he would load option 5 to enter the corresponding dialog. Here he would enter the habitID from which he wants the highscore to be displayed. Afterwards he can close the
analyzation menu by pressing the 6 and get back to the main menu.
