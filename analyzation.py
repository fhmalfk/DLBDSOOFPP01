'''
analysation.py provides the user with all functions to analyze and display habit information.
'''
#Import the connector class for establishing the database connection and the functions module to reuse functionalities
import connector
import functions

#Define ANSI escape codes to print red and green colored statements
red = "\033[31m"
green = "\033[92m"
reset = "\033[0m"

#Display the highest Highscore of all habits
def displayHighscoreAll():
    tempHigh = 0
    cursor = connector.mydb.cursor()
    cursor.execute("SELECT * FROM habits;")
    results = cursor.fetchall()
    #Figure out the highest Highscore through a comparsion loop
    for row in results:
         if (row[7]) > tempHigh:
                tempHigh = row[7]
                results = row
    #Store the column header values from the cursor.description 
    frienldyNames=[description[0] for description in cursor.description]
    print("\nThe current highscore is ") 
    #Print the highest Highscore
    print(tempHigh) 
    print("hold by:")
    #Print the column headers
    print(frienldyNames)
    #Print the whole row
    print(results)
    cursor.close()

#Display the highest highscore from a specific time period
def displayHighscorePeriod():
    #Print all periods including their id and amount of days
    print(functions.getPeriod())
    print("Enter durationDays attribute of the period from which the highscore shall be displayed: ")
    #Ensure the entered value is an integer value
    days = functions.getInteger()
    #Load all valid days from the period table
    enumPeriod=functions.getPeriodDays()
    #Check if the entered user value is a valid days value
    if days not in enumPeriod:
            print(red + "This period is not defined in the period table.\nExisting values: ")
            print(enumPeriod)
            print (reset)
    else:
        #Load the primary key value from the period table
        periodID = functions.getPeriodID(days)
        #Define a base value for comparsion
        tempHigh = 0
        cursor = connector.mydb.cursor()
        #Load all habit values from the defined period 
        cursor.execute("SELECT * FROM habits WHERE fk_period = %s", (periodID,))
        results = cursor.fetchall()
        #Compare all habits with the set period and store the highest Highscore
        for row in results:
            if (row[7]) > tempHigh:
                    tempHigh = row[7]
                    results = row
        #Load the column headers
        frienldyNames=[description[0] for description in cursor.description]
        #In case one of the habits of the period has a Highscore value above 0
        if tempHigh > 0:
            print("\nThe current highscore is ") 
            #Print the highest Highscore
            print(tempHigh) 
            print("hold by:")
            #Print the whole habit row
            print(frienldyNames)
            print(results)
        #In case no habit has a Highscore above 0
        else:
            #Load all habits of the the requested period
            cursor.execute("SELECT * FROM habits WHERE fk_period = %s", (periodID,))
            results = cursor.fetchall()
            print("No habit of the defined period has a Highscore above 0")
            print(frienldyNames)
            for row in results:
                print(row)
        #Close the cursor object
        cursor.close()
#Load all habits of a set period
def displayHabitsByPeriod():
    print(functions.getPeriod())
    print("Enter durationDays attribute of the period of which all habits shall be displayed: ")
    #Ensure the provided value is an integer value
    days = functions.getInteger()
    #Check that the days value is valid
    enumPeriod=functions.getPeriodDays()
    if days not in enumPeriod:
            print(red + "This period is not defined in the period table.\nExisting values: ")
            print(enumPeriod)
            print (reset)
    else:
        #Get the period primary key
        periodID = functions.getPeriodID(days)
        cursor = connector.mydb.cursor()
        #Load all habit values with the set period foreign key
        cursor.execute("SELECT * FROM habits WHERE fk_period = %s", (periodID,))
        results = cursor.fetchall()
        #Print all habits
        for row in results:
              print(row)
        #Close the cursor object
        cursor.close

#Display the current highscore of a specific habit
def displayHighscoreHabit():
    cursor = connector.mydb.cursor()
    cursor.execute("SELECT * FROM habits;")
    results = cursor.fetchall()
    #Display all habitIDs and names
    for row in results:
         print (row[0],row[2])
    print("Choose the habitID from which to display the Highscore: ")
    #Ensure the entered value is of the type integer
    habit=functions.getInteger()
    #Load the whole habit objects, based on the defined ID
    cursor.execute("SELECT * FROM habits WHERE id_habit = %s", (habit,))
    habit=cursor.fetchall()
    print("\nName, Highscore")
    #Print only the name and highscore of the habit
    print(habit[0][2], ",", habit[0][7], "\n")