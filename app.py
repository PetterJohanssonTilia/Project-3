


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


word_list = { #The different types of words the player inputs
    'person': "Enter a person's name: ",
    'title': "Enter a title for the person: ",
    'object': "Enter the name of a mysterious object: ",
    'adjective': "Enter an adjective: ",
    'creature': "Enter the name of a creature: ",
    'country': "Enter the name of a country: "
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


    print(f"In a distant forest, a {inputs['title']} named {inputs['person']} found a mysterious {inputs['object']}.")
    print(f"It granted them incredible {inputs['adjective']} powers and transported them to a magical woodland.")
    print(f"There, they met a {inputs['creature']} in need. With bravery, {inputs['person']} helped the {inputs['creature']}")
    print(f"and became a hero of {inputs['country']}.")
    

def story_desert():
    inputs = user_inputs(word_list)

    print(f" In a distant desert, a {inputs['title']} named {inputs['person']} found a mysterious {inputs['object']}.")
    print(f"It granted them incredible {inputs['adjective']} powers and transported them to a magical oasis.")
    print(f"There, they met a {inputs['creature']} in need. With bravery, {inputs['person']} helped the {inputs['creature']}")
    print(f"and became a hero of {inputs['country']}.")
    

def story_ocean():
    inputs = user_inputs(word_list)

    print(f"In a distant ocean, a {inputs['title']} named {inputs['person']} found a mysterious {inputs['object']}.")
    print(f"It granted them incredible {inputs['adjective']} powers and transported them to a magical underwater city.")
    print(f"There, they met a {inputs['creature']} in need. With bravery, {inputs['person']} helped the {inputs['creature']}")
    print(f"and became a hero of {inputs['country']}.")

#Start
introduction()
display_location()
choose_location(choice)
#user_inputs()

