'''
functions.py provides the other modules with neccessary functions to get integers, get periodIDs, habits, etc.
'''
import connector
import objects

#Define ANSI escape codes to print red colored statements
red = "\033[31m"
green = "\033[92m"
reset = "\033[0m"

#Load all day values from the period table
def getPeriodDays(): 
    #inovke a cursor object
                 cursor = connector.mydb.cursor()
                 #prepare and execute the SQL command
                 cursor.execute("SELECT durationDays FROM period;")
                 #store the retrived tuples 
                 results = cursor.fetchall()
                 #prepare a list object to store all valid periods
                 enumPeriod = [] 
                 for elements in results:
                      #Clean the retrived tuples from leading and trailing brackets
                      element = elements[0]
                      #extend the list with every retrived value from the table
                      enumPeriod.extend([element])
                 cursor.close()
                 #Is utilized later to check if the entered day value of the user is valid
                 return enumPeriod

#Load all periods and their id
def getPeriod(): 
                 #inovke a cursor object
                 cursor = connector.mydb.cursor()
                 #prepare and execute the SQL command
                 cursor.execute("SELECT * FROM period;")
                 #store the retrived tuples 
                 results = cursor.fetchall()
                 #store the column names
                 frienldyNames=[description[0] for description in cursor.description]
                 print(frienldyNames)
                 for row in results:
                         print(row)
                 #print (enumPeriod)
                 cursor.close()

#Ensure that the entered value by the user is an integer object
def getInteger():
                while True:    
                    #Get user input
                    inputInteger = input()
                    try:
                        #Try to convert the string value in an integer object
                        newDuration = int(inputInteger)
                        #If the operation was successful, return the int object
                        return newDuration
                    except ValueError:
                        #In case the conversion was not possible, display an error message
                        print(red + "Wrong input, no integer. Try again: " + reset)

#Get the corresponding id from the provided days value
def getPeriodID(days):
                cursor = connector.mydb.cursor()
                cursor.execute("SELECT id_period FROM period WHERE durationDays = %s", (days,))
                periodID = cursor.fetchall()
                cleanPeriod = [] 
                for elements in periodID:
                    #Clean the retrived tuples from leading and trailing brackets
                    element = elements[0]
                    #extend the list with every retrived value from the table
                    cleanPeriod.extend([element])
                cursor.close()
                return cleanPeriod[0]

#Load all values from the habits table
def getHabits():
                 cursor = connector.mydb.cursor()
                 cursor.execute("SELECT * FROM habits;")
                 results = cursor.fetchall()
                 frienldyNames=[description[0] for description in cursor.description]
                 print(frienldyNames)
                 for row in results:
                      print (row)
                 print()
                 cursor.close()
                
#Create a new habit
def createHabit():
                #Store all valid period days
                enumPeriod=getPeriodDays()
                print("Enter habit period in days: ")
                #get an integer value from the user defining the day value of the habit object
                days = getInteger()
                #Check if the days value is invalid
                if days not in enumPeriod:
                     print(red + "This period is not defined in the period table.\nExisting values: ")
                     print(enumPeriod)
                     print (reset)
                else:
                    #Get the foreign key value to reference the period row
                    periodID = getPeriodID(days)
                    print("Enter habit name: ")
                    name = input()
                    #Create an empty dictionary object to store all habit values 
                    habits = {}
                    #call the habits class and initialize the creation of an object and store it in the dictionary under $name, pass following attributes to the class
                    habits[name] = objects.habits(name, periodID, days)
                    #call the .dispaly function of the object stored in the dictionary
                    print(habits[name].display())
                    try:
                         #Try to write the object attributes in the database
                         cursor = connector.mydb.cursor()
                         sql = "INSERT INTO `habits`(`fk_period`, `name`, `success`, `createdAt`, `nextTime`, `streakCounter`, `streakHighscore`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                         values = (
                            habits[name].periodID,
                            habits[name].name, 
                            habits[name].successTrigger, 
                            habits[name].creationDate, 
                            habits[name].nextTime, 
                            habits[name].streakCounter,
                            habits[name].streakHighScore,   
                         )
                         cursor.execute(sql,values)
                         connector.mydb.commit()
                         cursor.close() 
                         #Inform user about successful habit creation
                         print(green + "Habit created successful\n" + reset)
                    except connector.mysql.connector.Error as err:
                         print(f"Error: {err}")

def createPeriod():
                 #Call function to return a list of all period day values
                 enumPeriod=getPeriodDays()
                 #call function to store int value in newDuration while typechecking the input data
                 print("Enter new integer value for days: ")
                 newDuration = getInteger()  
                 cursor = connector.mydb.cursor()  
                 #Check if the days value is already existing
                 if newDuration not in enumPeriod:
                    try:
                         cursor.execute("INSERT INTO period (durationDays) VALUES (%s)", (newDuration,))
                         connector.mydb.commit()
                         cursor.close() 
                         print(green + "New Period was created successful!\n" + reset)
                    except connector.mysql.connector.Error as err:
                         print(f"Error: {err}")
                 else:
                    #Display to the user that the days value is already existing and display all already defined days values
                    print(red + "Duration already exisits, please choose a different value.\nExisting values: ")
                    print(enumPeriod)
                    print (reset)

#Enable users to delete habits or change the period
def editHabit():
        print("Press 1 to change the period of a habit, press 2 to delete a habit:")
        #Get the user choice
        choice = int(input())
        #If the provided value was not 1 or 2, print an error message
        if choice not in (1, 2):
                print(red + "Entered invalid choice, only 1 or 2 are accepted!" + reset)
        #If user chose to change the period
        elif choice == 1:
            cursor = connector.mydb.cursor()
            #Print all habits and their column names
            cursor.execute("SELECT * FROM habits;")
            results = cursor.fetchall()
            frienldyNames=[description[0] for description in cursor.description]
            print(frienldyNames)
            for row in results:
                print(row)
            #Get the habit id of the habit to change
            print("The period of which habit shall be edited? Enter the habitID?")
            habitId=int(input())
            cursor.execute("SELECT id_habit FROM habits")
            habitIDs = cursor.fetchall()
            cleanHabitIDs = [] 
            for elements in habitIDs:
                #Clean the retrived tuples from leading and trailing brackets
                element = elements[0]
                #extend the list with every retrived value from the table
                cleanHabitIDs.extend([element])
            #Ensure that the habit id exists
            if habitId in cleanHabitIDs:
                print("Which period shall be applied? Enter the days: ")
                enumPeriod=getPeriodDays()
                print(enumPeriod)
                periodDays=int(input())
                #Ensure the provided period value exists
                if periodDays in enumPeriod:
                        try:
                            cursor = connector.mydb.cursor()
                            #Load the periodID value through the chosen days value
                            cursor.execute("SELECT id_period FROM period where durationDays = %s", (periodDays,))
                            #Extract single value from only row which was retrived from the table, since we only expect one periodID to be returned, lists are not accepted as arguments for the planned cursor.execute. 
                            results = cursor.fetchone()
                            id_period = results [0]
                            #Reference the periodID value as a foreign key in the habits row
                            cursor.execute("Update habits SET fk_period = %s WHERE id_habit = %s", (id_period, habitId,))
                            connector.mydb.commit()
                            cursor.close() 
                            print(green + "Period of habit changed successful" + reset)
                        except connector.mysql.connector.Error as err:
                            print(f"Error: {err}")
                else:
                    print(red + "Period is not defined so far. Please enter a valid already defined timespan\n" + reset)
            else:
                   print(red + "HabitID doenst exist!" + reset)
        #If the user chose to delete a habit
        else:        
            cursor = connector.mydb.cursor()
            #Display all habit
            cursor.execute("SELECT * FROM habits;")
            results = cursor.fetchall()
            frienldyNames=[description[0] for description in cursor.description]
            print(frienldyNames)
            for row in results:
                print(row)
            print("Enter habitID to delete habit:")
            id=input()
            try:
                #Try to delete the provided habit based on the id
                cursor.execute("Delete from habits WHERE id_habit = %s", (id,))
                connector.mydb.commit()
                cursor.close() 
                print(green + "Habit was deleted successful" + reset + "\n")
            #In case an error occours or an invalid habitID value was provided, display an error message
            except connector.mysql.connector.Error as err:
                print(f"Error: {err}")

#mark a habit as succeded
def markSuccess():
        cursor = connector.mydb.cursor()
        print("Which habit shall be marked as successful? Please enter the habitID")
        #Print all habits and their ids
        getHabits()
        #Let the user pick the id
        habitId=int(input())
        cursor.execute("SELECT id_habit FROM habits")
        habitIDs = cursor.fetchall()
        cleanHabitIDs = [] 
        for elements in habitIDs:
            #Clean the retrived tuples from leading and trailing brackets
            element = elements[0]
            #extend the list with every retrived value from the table
            cleanHabitIDs.extend([element])
        #Check if the provided ID exists
        if habitId in cleanHabitIDs:
                try:
                    #Set the boolean success to 1
                    cursor.execute("Update habits SET success = 1 WHERE id_habit = %s", (habitId,))
                    connector.mydb.commit()
                    cursor.close() 
                    print(green + "Habit was marked as succeded" + reset + "\n")
                except connector.mysql.connector.Error as err:
                    print(f"Error: {err}")
        else:
               print(red + "Entered invalid value!" + reset)