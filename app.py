


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
    choice = validate_input("Enter the number of the story you want to play: ", "number")
    # Add code to handle the user's choice and start the selected story
    
#Validates if its string or interger
def validate_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        if input_type == "number" and user_input.isdigit():
            return int(user_input)
        elif input_type == "letter" and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a valid", input_type + ".")


#Start
introduction()