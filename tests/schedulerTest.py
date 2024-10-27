import sys
import os
import threading
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
import pytest

green = "\033[92m"
reset = "\033[0m"

#Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scheduler import schedule, nextExecution
import connector

def testSchedule():
        wait = 1
        #Count active Threads
        currentThreads=threading.active_count()
        schedule(wait)
        #Check if a new thread was created
        assert threading.active_count() > currentThreads
        print(green + "\nschedule() was tested succesful" + reset)

def testNextExecution():
    #Create a cursor object
    cursor = connector.mydb.cursor()
    now = datetime.now()
    #Prepare and enter the testdata
    cursor.execute("""
    INSERT INTO habits (id_habit, fk_period, name, success, createdAt, nextTime, streakCounter, streakHighscore)
    VALUES (100, 1, 'Test', 1, %s, %s, 1, 1)
    """, (now - timedelta(days=2), now - timedelta(minutes=10)))
    connector.mydb.commit()

    #Call the function to test
    nextExecution()

    #Insert the test data to the table
    cursor.execute("SELECT success, streakCounter, streakHighscore, nextTime FROM habits WHERE id_habit = 100")
    habit = cursor.fetchone()

    #Check that the habit was created
    assert habit is not None
    #Ensure the success state is reset to 0
    assert habit[0] == 0
    #Ensure the streakCounter was increased by 1
    assert habit[1] == 2
    #Ensure the Highscore counter was incremented by 1
    assert habit[2] == 2
    #Assert the nextExecution time was scheduled for the future
    assert habit[3] > datetime.now()

    #Ensure an entry in the history table was created
    cursor.execute("SELECT date FROM history WHERE fk_habits = 100")
    period = cursor.fetchone()
    #Check that the history entry was created
    assert period is not None

    #Delete foreing key usages
    cursor.execute("DELETE FROM history WHERE fk_habits = 100")
    #Delete the test habit
    cursor.execute("DELETE FROM habits WHERE id_habit = 100")
    cursor.close
    connector.mydb.commit()

print(green + "\nnextExecution() was tested succesful" + reset)
