import random
import sys

shoppingList = []
funds = int(0)
area = str("")
inf_peop = 0
event = str("")
time = 300

#tracks which area you have visited
visA1 = int(0) #area 1
visA2 = int(0) #area 2
visA3 = int(0) #area 3
visA4 = int(0) #area 4
visA5 = int(0) #area 5
visA6 = int(0) #area 6


def spaces(number):
    for i in range(0, number):
        print("\n")
        

def decrementTime():
    time -= 1


def infection(inf_peop):
    print("Infection is everywhere")
    if(inf_peop < 5):
        infection = random.randint(0, 256)

    elif(inf_peop < 9 and inf_peop >= 5):
        infection = random.randint(0, 200)

    else:
        infection = random.randint(0, 150)

    
    if(infection == 0):
        print("You are infected")
        gameOver()

    else:
        print("You are still healthy")

        
    
def gameOver():
    print("Your adventure ends here.")
    sys.exit(0)
        

def mainHub():
    while(True):
        print("You are in the main hub of the mall")
        spaces(1)
        print("Choose where do you wish to go: ")
        '''
        insert choices of area here
        don't forget to check visit variables
        '''


        #Triggered after finishing an area
        #some random events happen
        #some item are gone in other areas

        

def area1():
    global visA1, choice
    choice = 0
    print("Insert story text here")
    print("Blah blah blah")
    print("Looking at the directory, there are x number of peoples here")
    people = 5
    infection(people) #checks infection

    print("Direction A, choice 1")
    print("Direction B, choice 2")

    #some events happen that take away more time
    #repeat how many times
    #don't forget to decrement time after each command
    #you found the stuffs
    print("You found all the stuffs you need.")
    print("Time to go to the other areas.")
    visA1 = 1
    return
    
    
    


def area2():
    global visA2, choice
    choice = 0

    if(visit == 0):
        spaces(2)
        print("Story text 1")
        spaces(6)
        print("Story text 2")


def area3():


def area4():


def area5():


def area6():
    

infection()
        
