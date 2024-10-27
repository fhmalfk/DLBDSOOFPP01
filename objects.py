'''
objects.py serves to provide two classes for the creation of objects. Namely habit and period objects. 
'''
#Import two datetime modules to calculate the next due time of new habits and load the current date
from datetime import datetime, timedelta

#Define a class to create new objects
class habits:
    #Define the requiere attributes and its default values
    def __init__(self, name, periodID, days=None, creationDate=None, nextTime=None, streakCounter=0, streakHighScore=0,successTrigger=False, habitID = None):
        self.name = name
        self.periodID = periodID
        #Define the creationDate automatically
        self.creationDate = creationDate if creationDate else datetime.now()
        #Calculate and store the next check time
        self.nextTime = nextTime if nextTime else self.creationDate + timedelta(days=days)
        self.streakCounter = streakCounter
        self.streakHighScore = streakHighScore
        self.successTrigger = successTrigger
        self.habitID = habitID
    #Define a display function for objects of the habit class to display all their attributes
    def display(self):
        print(f"Name: {self.name}")
        print(f"Creation Date: {self.creationDate}")
        print(f"Next Time: {self.nextTime}")
        print(f"PeriodID: {self.periodID}")
        print(f"Streak Counter: {self.streakCounter}")
        print(f"Streak High Score: {self.streakHighScore}")
        print(f"Success Trigger: {self.successTrigger}")
#Define a period class
class period:
    def __init__(self, durationDays):
        self.durationDays = durationDays
