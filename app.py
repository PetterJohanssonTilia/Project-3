


def introduction(): #The first message that appears when you run the program
    print ("This is a madlibs game, You'll be asked to input words and your words will help shape the story")
    print("There's 3 storys to choose from.") 
    print ("Depending on which location you'll pick you'll get a different story")


def display_location(): #Display 3 locations, user input what location they want
    global choice
    print("Where do you want your story to take place?")
    print("1. Forest")
    print("2. Desert")
    print("3. Ocean")
    choice = validate_input("Enter the number for the story you want to play: ", "number")
    locations = {1: "Forest", 2: "Desert", 3: "Ocean"}
    print(f"You chose {locations[choice]}")

def choose_location(choice): #call the story chosen by user input
    if choice == 1:
        story_forest()
    elif choice == 2:
        story_desert()
    elif choice == 3:
        story_ocean()
    else:
        print("Invalid choice. Please select a number between 1 and 3.")    


def user_inputs(word_list):
    inputs = {}
    for word, prompt in word_list.items():
        user_input = validate_input(prompt, "letter")
        inputs[word] = user_input
    return inputs

#Gives colors to the users input
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

word_list = { #The different types of words the player inputs with the prompts to tell the player what to input
    'person': f"Enter a {colorize("person's name", 'red')}:",
    'title': f"Enter a {colorize("title", 'blue')} for the person:",
    'object': f"Enter the name of a {colorize("mysterious object", 'yellow')}:",
    'adjective': f"Enter an {colorize("adjective", 'magenta')}:",
    'creature': f"Enter the name of a {colorize("creature", 'cyan')}:",
    'country': f"Enter the name of a {colorize("country", 'green')}: "
}

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



#================ The 3 main stories ================#
def story_forest():
    inputs = user_inputs(word_list)

    print(f"In a distant forest, a {colorize(inputs['title'], 'blue')} named {colorize(inputs['person'], 'red')} found a mysterious {colorize(inputs['object'], 'yellow')}.")
    print(f"It granted them incredible {colorize(inputs['adjective'], 'magenta')} powers and transported them to a magical woodland.")
    print(f"There, they met a {colorize(inputs['creature'], 'cyan')} in need. With bravery, {colorize(inputs['person'], 'red')} helped the {colorize(inputs['creature'], 'cyan')}")
    print(f"and became a hero of {colorize("country", 'green')}.")
    

def story_desert():
    inputs = user_inputs(word_list)

    print(f" In a distant desert, a {colorize(inputs['title'], 'blue')} named {colorize(inputs['person'], 'red')} found a mysterious {colorize(inputs['object'], 'yellow')}.")
    print(f"It granted them incredible {colorize(inputs['adjective'], 'magenta')} powers and transported them to a magical oasis.")
    print(f"There, they met a {colorize(inputs['creature'], 'cyan')} in need. With bravery, {colorize(inputs['person'], 'red')} helped the {colorize(inputs['creature'], 'cyan')}")
    print(f"and became a hero of {colorize("country", 'green')}.")
    

def story_ocean():
    inputs = user_inputs(word_list)

    print(f"In a distant ocean, a {colorize(inputs['title'], 'blue')} named {colorize(inputs['person'], 'red')} found a mysterious {colorize(inputs['object'], 'yellow')}.")
    print(f"It granted them incredible {colorize(inputs['adjective'], 'magenta')} powers and transported them to a magical underwater city.")
    print(f"There, they met a {colorize(inputs['creature'], 'cyan')} in need. With bravery, {colorize(inputs['person'], 'red')} helped the {colorize(inputs['creature'], 'cyan')}")
    print(f"and became a hero of {colorize("country", 'green')}.")

#Start
introduction()
display_location()
choose_location(choice)
#user_inputs()

