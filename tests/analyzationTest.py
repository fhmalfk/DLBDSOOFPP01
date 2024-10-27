import sys
import os

green = "\033[92m"
reset = "\033[0m"

#Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analyzation import displayHighscoreAll, displayHabitsByPeriod, displayHighscoreHabit, displayHighscorePeriod
import connector

def testDisplayHighscoreAll(capsys):
    displayHighscoreAll()
    testCursor = connector.mydb.cursor()
    testCursor.execute("Update habits SET streakHighscore = 2 WHERE id_habit = 5")
    connector.mydb.commit()
    #Capture the standard output
    capturedOutput = capsys.readouterr()
    #Strip and split the single String at \n new line characters into a list of lines
    outputLines = capturedOutput.out.strip().split("\n")
    #Check the firt line for the column descriptions. The current highscore is 12
    assert outputLines[1] == "12"  
    #Change the Highscore of another habit to 15 and reload the function
    testCursor.execute("Update habits SET streakHighscore = 15 WHERE id_habit = 5")
    connector.mydb.commit()
    displayHighscoreAll()
    capturedOutput2 = capsys.readouterr()
    outputLines2 = capturedOutput2.out.strip().split("\n")
    #Check if the new displayed highscore equals 15
    print(outputLines2[1])
    #Reset the highscore of id 5 to 2
    testCursor.execute("Update habits SET streakHighscore = 2 WHERE id_habit = 5")
    connector.mydb.commit()
    print(green + "\ndisplayHighscoreAll() tested successfully" + reset)

def testDisplayHabitsByPeriod(capsys, monkeypatch):
    #Define the later simulated correct user input 
    values = iter(["17", "1"])
    monkeypatch.setattr('builtins.input', lambda: next(values))
    displayHabitsByPeriod()
    capturedOutput = capsys.readouterr()
    #Ensure the function throws an error, if a non integer value was provided
    assert "This period is not defined in the period table" in capturedOutput.out 
    displayHabitsByPeriod()
    capturedOutput2 = capsys.readouterr()
    outputLines = capturedOutput2.out.strip().split("\n")
    #Ensure the habits 10k Schritte and Kochen are loaded when all habits with the period 1 are displayed
    assert "10K Schritte" in outputLines[7]
    assert "Kochen" in outputLines[8]
    print(green + "\ngetPeriod() tested successfully" + reset)

def testDisplayHighscoreHabit(capsys, monkeypatch):
    #define the future values to simulate user input
    values = iter(["1", "4"])
    monkeypatch.setattr('builtins.input', lambda: next(values))
    #call the function
    displayHighscoreHabit()
    #Capture std output
    capturedOutput = capsys.readouterr()
    #Split the output lines at the \n new line character
    outputLines = capturedOutput.out.strip().split("\n")
    #Ensure the Highscore of 12 for habitID 1 is displayed
    assert "10K Schritte , 12" == outputLines[9]
    displayHighscoreHabit()
    capturedOutput = capsys.readouterr()
    outputLines = capturedOutput.out.strip().split("\n")
    #Ensure the Highscore of 7 for habitID 4 is displayed
    assert "100 Seiten lesen , 7" == outputLines[9]
    print(green + "\ngetPeriod() tested successfully" + reset)

def testDisplayHighscorePeriod(capsys, monkeypatch):
    #Define the later simulated correct user input 
    values = iter(["1", "20"])
    monkeypatch.setattr('builtins.input', lambda: next(values))
    displayHighscorePeriod()
    capturedOutput = capsys.readouterr()
    outputLines = capturedOutput.out.strip().split("\n")
    #Ensure the highscore of 12 was loaded for habits with the PeriodID 1
    assert "12" == outputLines[9]
    displayHighscorePeriod()
    capturedOutput2 = capsys.readouterr()
    outputLines2 = capturedOutput2.out.strip().split("\n")
    #Ensure that the right feedback is presented, if a non existent period time was defined
    assert "This period is not defined in the period table" in outputLines2[7]
    print(green + "\nDisplayHighscorePeriod() tested successfully" + reset)
