'''
Scheduler.py serves to schedule the next execution cycle to check the state of habits which have crossed their defined cycle.
Additionally the function nextExecution() ensures that the next check will occour in the future and will clean up all check times which are set in the past.
'''

#Import the connector class to establish a connection with the DB
import connector
#Import the datetime class to load the current time and calculate time differences that account for month and year shifts
from datetime import datetime, timedelta
#Import the time module to define a sleep time for a thread
import time
#Import threading to run a background task
import threading

#Serves to save ressources to execute the check and update cycle only when the deadline of a habit has been reached
def schedule(seconds):
    def planner():
            #Sleep till the nextTime date is reached
            time.sleep(seconds)
            #Execute the check and update cycle
            nextExecution()
    #Create a thread
    threading.Thread(target=planner, daemon=True).start()

def nextExecution():
    #create a cursor object and load the habitID and nextTime attribute from the habit table.
    cursor = connector.mydb.cursor()
    cursor.execute("SELECT id_habit, nextTime FROM habits;")
    #Fetch the read data from the cursor object
    results = cursor.fetchall()
    now = datetime.now()
    #store a value in the nextDate object that always will be bigger than the stored nextTime attribute of the habit objects. 
    nextDate = now.replace(year = now.year + 1)
    #Compare the nextTime attribute of the habits between each other and safe the smallest value, additionally store the corresponding haibtID attribute
    for row in results:
        if row[1] < nextDate:
            nextDate = row[1]
            id = row[0]
    #Calculate the difference between now and the smallest nextTime value
    deltaTime = nextDate - now
    #Load all neccessary values from the habit corresponding to the stored id
    cursor.execute("SELECT success, streakCounter, streakHighscore, fk_period FROM habits WHERE id_habit = %s", (id,))
    results=cursor.fetchone()
    #Store the successState to check if the habit was fulfilled
    successState=results[0]
    #Store the streakCounter to enhance it by one, if the habit was fulfilled
    streakCounter=results[1]
    #Store the the streakHighscore to enhance it by one, if the habit was fulfilled
    streakHighscore=results[2]
    #Load the periodID to calculate the nextExecution time of the habit accordingly 
    fkPeriod=results[3]
    #Load the period days amount, based on the foreign key
    cursor.execute("SELECT durationDays FROM period WHERE id_period = %s", (fkPeriod,))
    results=cursor.fetchone()
    days=results[0]
    #Calculate the nextTime attribute of the habit based on the current time and its planned period
    nextDate = now + timedelta(days=days)
    #Try to execute sql statement, in case of failure, display mysql-Error message
    try:
        #Write the habit data into the history table
        cursor.execute(
            "INSERT INTO history (fk_habits, date, success) VALUES (%s, %s, %s)",
            (id, now, successState)
        )
        connector.mydb.commit()
    except connector.mysql.connector.Error as err:
                         print(f"Error: {err}")
    #If the time difference between the nextTime attribute and the current time is negativ, execute the functions immediately
    if deltaTime <= timedelta(0):
        #Check if the habit was marked as fulfilled
        if successState == 1:
           #Enhance the streakCounter by 1, if yes
           streakCounter += 1
           #If the the current streakCounter is higher than the highscore, replace the highscore count
           if streakCounter > streakHighscore:
               streakHighscore = streakCounter
           #Reset the successState to 0 
           successState = 0
           try:
                #Update the habit object with the new values
                cursor.execute("UPDATE habits SET success = %s, streakCounter = %s, streakHighscore = %s, nextTime = %s WHERE id_habit = %s", (successState, streakCounter, streakHighscore, nextDate, id,))
                connector.mydb.commit()
                #Close the cursor object
                cursor.close
           except connector.mysql.connector.Error as err:
                         print(f"Error: {err}")
           #Commit the sql command to the database
           #Execute the nextExecution function recursive till the timedifference between now and the nextTime value is positive
           nextExecution()
        #Execute if the successState equals 0, meaning the habit was not fulfilled
        else:
            try:
                #Reset streakCounter, set nextTime value for evaluated habit
                cursor.execute("UPDATE habits SET streakCounter = 0, nextTime = %s WHERE id_habit = %s", (nextDate, id,))
                connector.mydb.commit() 
                #Close the cursor object
                cursor.close
            except connector.mysql.connector.Error as err:
                         print(f"Error: {err}")
            #Execute the nextExecution function recursive till the timedifference between now and the nextTime value is positive
            nextExecution()
    #Execute if the timedifference between nextTime and now is positive
    else:
        #Transform the the timedifference in seconds
        seconds = deltaTime.seconds
        schedule(seconds)


