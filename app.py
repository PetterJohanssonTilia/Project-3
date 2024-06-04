
#================ Main Functions ================#

def introduction(): 
    """
    The first message that appears when you run the program
    """
    print ("==================")
    print (
        """This is a madlibs game, You'll be asked to input words 
        and your words will help shape the story"""
        )
    print("There's 3 storys to choose from.") 
    print ("Depending on which location you'll pick you'll get a different story")

def endmessage(): 
    """
    The last message before you quit/restart
    """
    global choicerestart
    print ("==================")
    print("Do you wish to play again?")
    print("1. Yes")
    print("2. No")
    choicerestart = validate_input(
        "Do you want to play again?", "number", [1, 2]
    )
    restart = {1: "Yes", 2: "No"}
    #Tell the user choice what they've picked
    print(f"You chose {restart[choicerestart]}") 
    
    #Return true or false if the player wants to play again or not
    if choicerestart == 2: 
        print("Thanks for playing! Bye!")
        return False
    elif choicerestart == 1:
        print("Let's play again!")
        return True


def display_location():
    """
    Display 3 locations, user input what location they want
    """
    global choice
    print("Where do you want your story to take place?")
    print("1. Forest")
    print("2. Desert")
    print("3. Ocean")
    #Validates its a number between 1-3
    locations = {1: "Forest", 2: "Desert", 3: "Ocean"}
    choice = validate_input(
        "Enter the number for the story you want to see:", "number", [1, 2, 3]
    ) 
    #Tell the user what location they've picked
    print(f"You chose {locations[choice]}") 
    print ("==================")


def display_goodevil(): 
    """
    Display 2 options, the previous user inputs(choice) fills the words this time
    """
    global choicegoodevil
    print("Do you wish for the main character to turn good or evil?")
    print("1. Good")
    print("2. Evil")
    #Validates its a number between 1-2
    choicegoodevil = validate_input(
        "Enter the number for the story you want to see: ", "number", [1, 2]
    ) 
    goodevil = {1: "Good", 2: "Evil"}
    #Tell the user what path they've picked
    print(f"You chose {goodevil[choicegoodevil]}")
    print ("==================") 

def choose_location(choice): 
    """
    call the location-story chosen by user input
    """
    if choice == 1:
        story_forest()
    elif choice == 2:
        story_desert()
    elif choice == 3:
        story_ocean()
    else:
        print("Invalid choice. Please select a number between 1 and 3.")    

def choose_goodevil(choicegoodevil):
    """
    call the good/evil-story chosen by user input
    """
    if choicegoodevil == 1:
        #Uses the previous inputs in the next story
        story_good(inputs) 
    elif choicegoodevil == 2:
        #Uses the previous inputs in the next story
        story_evil(inputs) 
    else:
        print("Invalid choice. Please select a number between 1 and 2.")    


def user_inputs(word_list): 
    """
    Request users to input words
    """
    global inputs
    #the dictionary that stores the inputs
    inputs = {} 
    for word, prompt in word_list.items():
        #Validates that it's letters
        user_input = validate_input(prompt, "letter") 
        inputs[word] = user_input
    return inputs

#Dictionary of colors to use on the input words
def colorize(text, color): 
    colors = { 
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'default': '\033[0m'
    }
    return colors.get(color, '') + text + colors['default']

#Dictionary of descriptions of the words the player needs to input
word_list = { 
    'person': f"Enter a {colorize("person's name", 'red')}:",
    'title': f"Enter a {colorize("title", 'blue')} for the person:",
    'object': f"Enter the name of a {colorize("mysterious object", 'yellow')}:",
    'adjective': f"Enter an {colorize("adjective", 'magenta')}:",
    'creature': f"Enter the name of a {colorize("creature", 'cyan')}:",
    'country': f"Enter the name of a {colorize("country", 'green')}:"
}

def validate_input(prompt, input_type, choices=None): 
    """
    Validates if its string or the correct intergers 
    """
    while True:
        user_input = input(prompt)
        #Checks if it's a number
        if input_type == "number" and user_input.isdigit():
            #User input is now an integer
            user_input = int(user_input) 
            #Error - The user chose a number but it's not in the choices
            if choices is not None and user_input not in choices: 
                print("Invalid input. Please enter a valid choice.")
            else:
                #Returns the now integer input
                return user_input 
        #Checks if it's a letter
        elif input_type == "letter" and user_input.isalpha(): 
            #Return a string
            return user_input 
        else:
            #Error - invalid input message
            print("Invalid input. Please enter a valid", input_type + ".") 



#================ The 3 location stories ================#
def story_forest():
    inputs = user_inputs(word_list)
    print(
        f"==================\n"
        f"In a distant forest, a {colorize(inputs['title'], 'blue')}\n"
        f"named {colorize(inputs['person'], 'red')}\n" 
        f"found a mysterious {colorize(inputs['object'], 'yellow')}.\n"
        f"It granted them incredible {colorize(inputs['adjective'], 'magenta')}\n"
        f"powers and transported them to a magical woodland.\n"
        f"There, they met a {colorize(inputs['creature'],'cyan')}\n"
        f"in need. With bravery, {colorize(inputs['person'],'red')}\n"
        f"helped the {colorize(inputs['creature'], 'cyan')}\n"
        f"and became a hero of {colorize(inputs['country'], 'green')}.\n"
    )

    

def story_desert():
    inputs = user_inputs(word_list)
    print(
        f"==================\n"
        f"In a distant desert, a {colorize(inputs['title'], 'blue')}\n"
        f"named {colorize(inputs['person'], 'red')}\n"
        f"found a mysterious {colorize(inputs['object'], 'yellow')}.\n"
        f"It granted them incredible {colorize(inputs['adjective'], 'magenta')}\n"
        f"powers and transported them to a magical oasis.\n"
        f"There, they met a {colorize(inputs['creature'], 'cyan')}\n"
        f"in need. With bravery, {colorize(inputs['person'], 'red')}\n"
        f"helped the {colorize(inputs['creature'], 'cyan')}\n"
        f"and became a hero of {colorize(inputs['country'], 'green')}.\n"
    )
    

def story_ocean():
    inputs = user_inputs(word_list)
    print(
        f"==================\n"
        f"In a distant ocean, a {colorize(inputs['title'], 'blue')}\n"
        f"named {colorize(inputs['person'], 'red')}\n"
        f"found a mysterious {colorize(inputs['object'], 'yellow')}.\n"
        f"It granted them incredible {colorize(inputs['adjective'], 'magenta')}\n"
        f"powers and transported them to a magical underwater city.\n"
        f"There, they met a {colorize(inputs['creature'], 'cyan')} in need.\n"
        f"With bravery, {colorize(inputs['person'], 'red')}\n"
        f"helped the {colorize(inputs['creature'], 'cyan')}\n"
        f"and became a hero of {colorize(inputs['country'], 'green')}.\n"
        )

#================ The 2 good/evil stories ================#
def story_good(inputs):
    print(
        f"==================\n"
        f"a {colorize(inputs['title'], 'blue')} named {colorize(inputs['person'], 'red')}\n"
        f"stumbled upon a wondrous {colorize(inputs['object'], 'yellow')}.\n"
        f"It bestowed upon them noble and {colorize(inputs['adjective'], 'magenta')}\n"
        f"powers and transported them to an enchanting underwater utopia.\n"
        f"There, they encountered a {colorize(inputs['creature'], 'cyan')} in distress.\n"
        f"With courage and compassion, {colorize(inputs['person'], 'red')}\n"
        f"aided the {colorize(inputs['creature'], 'cyan')}\n" 
        f" and restored harmony to the underwater realm.\n"
        )

def story_evil(inputs):
    print(
        f"==================\n"
        f"{colorize(inputs['title'], 'blue')} known as {colorize(inputs['person'], 'red')}\n"
        f"stumbled upon a malevolent {colorize(inputs['object'], 'yellow')}.\n"
        f"It bestowed upon them dark and {colorize(inputs['adjective'], 'magenta')}\n"
        f"powers and whisked them away to a cursed underwater fortress.\n"
        f"There, they encountered a {colorize(inputs['creature'], 'cyan')} in distress.\n"
        f"{colorize(inputs['person'], 'red')}\n"
        f"exploited the situation for their own gain, using the {colorize(inputs['creature'], 'cyan')}\n"
        f"to further their wicked agenda.\n"
        )

#================ Start of script ================
while True:
    introduction() #Introduction text
    display_location() #Displays the location choices
    choose_location(choice) #Calls the chosen locations story
    display_goodevil() #Displays the good and evil choices
    choose_goodevil(choicegoodevil) #Calls the chosen good/evil story
    if not endmessage():  #calls the endmessage and checks for true/false
        break

