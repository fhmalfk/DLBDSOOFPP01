'''
connector.py serves to create the database connection and will be used to create cursor objects within the established connection.
'''
#Importing the requiered mysql connector tools
import mysql.connector

#Create a connection object named mydb connecting to the defined database with the stored credentials
mydb = mysql.connector.connect( 
    host = "localhost",
    user = "Hausmann",
    password = "Test123",
    database = "habittrackerapp"
)