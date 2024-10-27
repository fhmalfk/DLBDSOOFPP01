'''
main.py serves as the main menu of the habit tracker application and loads all the neccesary modules. 
'''
#Import all requiered modules
import functions
import analyzation
import scheduler

#These boolean variables control the while loops of both menus, the main menu and analyzation menu
run = True
run2 = True

#Defines the main menu
menu="""Press the corresponding option to execute:\n
1)Create new habit
2)Create new period
3)Display all habits 
4)Display all periods 
5)Edit existing habit 
6)Mark habit as executed 
7)Load analyzation module
8)Close application\n""" 

#Defines the analyzation menu
menu2='''Press the corresponding option to execute:\n
1)Display top highscore of all habits
2)Display top highscore of specific period
3)Display all habits
4)Display all habits with a specific period
5)Return the highscore of a specific habit
6)Turn back to main menu'''

#Build a switch case menu to let the user switch between his choices
def mainMenu(choice):
        '''
        User input gets aligned with the switch case structure.
        User enters 1
        case 1 gets executed
        '''
        #Load both global variables in the local scope
        global run
        global run2
        match choice:
            case "1":
                functions.createHabit()
                #In case the newly created habit has a shorter period as the currently scheduled next execution of the nextExecution function.
                scheduler.nextExecution()
            case "2":
                functions.createPeriod()
            case "3":
                functions.getHabits()
            case "4":
                functions.getPeriod()
            case "5":
                functions.editHabit()
            case "6":
                functions.markSuccess()
            case "7":
                #Reset run2 again to true, so the menu can be reopend during a session, if it was closed before by the user
                run2 = True
                while run2 == True:
                 print(menu2)
                 choice2 = input("Option: ")
                 analyzationMenu(choice2)
            case "8":
                #set run to false and this end the while loop
                run = False
                print("Good by!")
            case _:
                #is a wildcard case for every not defined case
                print("Invaild choice")

def analyzationMenu(choice2):
        '''
        User input gets aligned with the switch case structure.
        User enters 1
        case 1 gets executed
        '''
        global run2
        match choice2:
            case "1":
                analyzation.displayHighscoreAll()
            case "2":
                analyzation.displayHighscorePeriod()
            case "3":
                functions.getHabits()
            case "4":
                analyzation.displayHabitsByPeriod()
            case "5":
                analyzation.displayHighscoreHabit()
            case "6":
                run2 = False
            case _:
                    print("Invaild choice")

#Call the nextExecution function to check all habit states and schedule its next run to the needed time to save ressources
scheduler.nextExecution()

if __name__ == "__main__":
    #print the main menu
    while run == True:
        print(menu)
        choice = input("Option: ")
        mainMenu(choice)
