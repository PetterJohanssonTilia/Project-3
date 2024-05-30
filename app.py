


def introduction(): #The first message that appears when you run the program
    print ("This is a madlibs game, You'll be asked to input words and your words will help shape the story")
    print("There's 3 storys to choose from.") 
    print ("Depending on which location you'll pick youll get a different story")
    choose_location() 

def choose_location(): #Pick between 3 locations for 3 different stories
    print("Where do you want your story to take place?")
    print("1. Forest")
    print("2. Desert")
    print("3. Ocean")
    choice = input("Enter the number of the story you want to play: ")
    # Add code to handle the user's choice and start the selected story




#Start
introduction()