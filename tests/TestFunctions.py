import sys
import os

green = "\033[92m"
reset = "\033[0m"

#Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import getPeriodDays, getPeriod, getInteger, getPeriodID, getHabits, createHabit, createPeriod, markSuccess
import connector

def test_getPeriodDays():
        #Call the function under test
        result = getPeriodDays()
        #Ensure the day values are returned correctly
        assert 7 in result  
        assert 1 in result
        assert 14 in result
        print(green + "\n\ngetPeriodDays() tested successfully" + reset)

def test_getPeriod(capsys):
    getPeriod()
    #Capture the standard output
    capturedOutput = capsys.readouterr()
    #Strip and split the single String at \n new line characters into a list of lines
    outputLines = capturedOutput.out.strip().split("\n")
    #Check the firt line for the column descriptions
    assert outputLines[0] == "['id_period', 'durationDays']"  
    #Check the row data
    assert outputLines[1] == "(1, 1)"
    assert outputLines[2] == "(2, 7)"
    assert outputLines[3] == "(3, 14)"
    assert outputLines[4] == "(4, 2)"
    print(green + "\ngetPeriod() tested successfully" + reset)

def test_getInteger(monkeypatch, capsys):
    #Store simulated user entry values
    values = iter(["abc", "10"])
    #Insert stated values for input requests of the application
    monkeypatch.setattr('builtins.input', lambda: next(values))
    #Store the return value
    result = getInteger()
    #ensure the return value for 10 is 10
    assert result == 10
    #Capture the standard output
    capturedOutput = capsys.readouterr()
    #Ensure the function throws an error, if a non integer value was provided
    assert "Wrong input, no integer" in capturedOutput.out
    print(green + "\ngetInteger() tested successfully" + reset)

def test_getPeriodID():
     #Store the return value 
     result=getPeriodID(7)
     #Assert the returned ID is 2, standing for 7 days
     assert result == 2
     print(green + "\ngetPeriodID() tested successfully" + reset)

def test_getHabits(capsys):
     #Execute function
     getHabits()
     #Capture the standard output
     capturedOutput = capsys.readouterr() 
     #Strip and split the single String at \n new line characters into a list of lines
     outputLines = capturedOutput.out.strip().split("\n")
     assert outputLines[0] == "['id_habit', 'fk_period', 'name', 'success', 'createdAt', 'nextTime', 'streakCounter', 'streakHighscore']"
     #assert output_lines[1] == "(1, 1, '10K Schritte', 0, datetime.datetime(2024, 9, 25, 16, 9, 31), datetime.datetime(2024, 10, 23, 16, 9, 31), 0, 12)"
     assert "1, 1, '10K Schritte'" in outputLines[1]
     print(green + "\ngetHabits() tested successfully" + reset)

def test_createHabit(monkeypatch, capsys):
    # Mock user input for the habit name and the days
    values = iter(["1", "Test"])
    monkeypatch.setattr('builtins.input', lambda: next(values))
    # Run the createHabit function
    createHabit()
    # Capture the output during the function call
    capturedOutput = capsys.readouterr()
    # Check if the habit was successfully created in the database
    testCursor = connector.mydb.cursor()
    testCursor.execute("SELECT * FROM habits WHERE name = %s", ("Test",))
    # Fetch the created habit
    habit = testCursor.fetchone()  
    #Assert that data was retrived
    assert habit is not None  
    #Ensure the habit was created
    assert habit[2] == "Test"  
    #Assert the operation was conducted successful 
    assert "Habit created successful" in capturedOutput.out
    #Clean up
    testCursor.execute("DELETE FROM habits WHERE name = %s", ("Test",))
    connector.mydb.commit()
    testCursor.close()
    print(green + "\ncreateHabit() tested successfully" + reset)

def test_createPeriod(monkeypatch, capsys):
    #Define the later simulated correct user input 
    monkeypatch.setattr('builtins.input', lambda: "100")
    #Call the function
    createPeriod()
    # Capture the output during the function call
    capturedOutput = capsys.readouterr()
    # Check if the habit was successfully created in the database
    testCursor = connector.mydb.cursor()
    testCursor.execute("SELECT * FROM period WHERE durationDays = 100")
    # Fetch the created period
    period = testCursor.fetchone()
    #Assert that data was retrived
    assert period is not None  
    #Assert the operation was conducted successful 
    assert "New Period was created successful!" in capturedOutput.out
    #Clean up
    testCursor.execute("DELETE FROM period WHERE durationDays = 100")
    connector.mydb.commit()
    testCursor.close()

    #Define the later simulated doubled user input 
    monkeypatch.setattr('builtins.input', lambda: "1")
    #Call the function
    createPeriod()
    # Capture the output during the function call
    capturedOutput = capsys.readouterr()
    #Assert the operation was conducted successful 
    assert "Duration already exisits, please choose a different value" in capturedOutput.out
    print(green + "\ncreatePeriod() tested successfully" + reset)

def test_markSuccess(monkeypatch, capsys):
    #Define the later simulated correct user input 
    monkeypatch.setattr('builtins.input', lambda: "6")
    # Check the current state of the habitID 6
    testCursor = connector.mydb.cursor()
    testCursor.execute("SELECT * FROM habits WHERE id_habit = 6")
    result = testCursor.fetchone()
    #Ensure the success is set to 0
    if result[3] == 1:
         testCursor.execute("Update habits SET success = 0 WHERE id_habit")
         connector.mydb.commit()
         testCursor.execute("SELECT * FROM habits WHERE id_habit = 6")
         result = testCursor.fetchone()
    #Assert it
    assert result[3] == 0
    #Call the function markSuccess for habitID 6
    markSuccess()
    #Reload the habit 6
    testCursor.execute("SELECT * FROM habits WHERE id_habit = 6")
    result = testCursor.fetchone()
    #Assert it is set to success now
    assert result[3] == 1
    #Reset the value to 0
    testCursor.execute("Update habits SET success = 0 WHERE id_habit")
    connector.mydb.commit()
    testCursor.close()
    #To keep the cli empty when conducting the test
    captured = capsys.readouterr()
    print(green + "\nmarkSuccess() tested successfully" + reset)
    
