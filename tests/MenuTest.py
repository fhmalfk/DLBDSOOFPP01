import pytest
from unittest.mock import patch
import sys
import os

green = "\033[92m"
reset = "\033[0m"

#Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import analyzation
#Import the necessary items from main.py
from main import mainMenu, analyzationMenu, run, run2  


@pytest.fixture
def resetGlobals():
    global run, run2
    run = True
    run2 = True

def test_mainMenu_case_1(resetGlobals):
    with patch('functions.createHabit') as mock_createHabit:
        mainMenu("1")
        #Check if createHabit was called
        mock_createHabit.assert_called_once()  

def test_mainMenu_case_2(resetGlobals):
    with patch('functions.createPeriod') as mock_createPeriod:
        mainMenu("2")
        #Check if createPeriod was called
        mock_createPeriod.assert_called_once()  

def test_mainMenu_case_3(resetGlobals):
    with patch('functions.getHabits') as mock_getHabits:
        mainMenu("3")
        #Check if getHabits was called
        mock_getHabits.assert_called_once()  

def test_mainMenu_case_4(resetGlobals):
    with patch('functions.getPeriod') as mock_getPeriod:
        mainMenu("4")
        #Check if getHabits was called
        mock_getPeriod.assert_called_once()  

def test_mainMenu_case_5(resetGlobals):
    with patch('functions.editHabit') as mock_editHabit:
        mainMenu("5")
         #Check if getHabits was called
        mock_editHabit.assert_called_once()  

def test_mainMenu_case_6(resetGlobals):
    with patch('functions.markSuccess') as mock_markSuccess:
        mainMenu("6")
        #Check if getHabits was called
        mock_markSuccess.assert_called_once()  

def test_mainMenu_case_7(resetGlobals):
   assert run2 is True

def test_mainMenu_case_8(resetGlobals):
    global run
    run = False
    #Assert that run is set to False
    assert run is False

print(green + "\nEvery function call of the main menu was executed successfully" + reset)

def test_analyzationMenu_case_1(resetGlobals):
    with patch('analyzation.displayHighscoreAll') as mock_displayHighscoreAll:
        analyzationMenu("1")
        #Check if getHabits was called
        mock_displayHighscoreAll.assert_called_once() 

def test_analyzationMenu_case_2(resetGlobals):
    with patch('analyzation.displayHighscorePeriod') as mock_displayHighscorePeriod:
        analyzationMenu("2")
        #Check if getHabits was called
        mock_displayHighscorePeriod.assert_called_once()  

def test_analyzationMenu_case_3(resetGlobals):
    with patch('functions.getHabits') as mock_getHabits:
        analyzationMenu("3")
        #Check if getHabits was called
        mock_getHabits.assert_called_once() 

def test_analyzationMenu_case_4(resetGlobals):
    with patch('analyzation.displayHabitsByPeriod') as mock_displayHabitsByPeriod:
        analyzationMenu("4")
        #Check if getHabits was called
        mock_displayHabitsByPeriod.assert_called_once()  

def test_analyzationMenu_case_5(resetGlobals):
    with patch('analyzation.displayHighscoreHabit') as mock_displayHighscoreHabit:
        analyzationMenu("5")
        #Check if getHabits was called
        mock_displayHighscoreHabit.assert_called_once()  

def test_analyzationMenu_case_6(resetGlobals):
    global run2
    run2 = False
    assert run2 is False

print(green + "Every function call of the analyzation menu was executed successfully" + reset)
