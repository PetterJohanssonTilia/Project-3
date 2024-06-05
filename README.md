<h1>Madlibs Python</h1>
This is a Python portfolio-project. <br>
The application is designed to be a branching type of madlibs game. The application offers a clear and simple game with simple visuals to keep the player well informed and engaged.<br><br>

## Table of Contents

1.  <details open>

      <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)

2.  <details open>
      <summary><a href="#features">Features</a></summary>
      
       <summary><a href="#data-model">Data Model</a></summary>
      <summary><a href="#colors">Colors</a></summary>
      <summary><a href="#validation">Validation</a></summary>
      <summary><a href="#feauture-ideas">Feauture Ideas</a></summary>

3.  <details open>
      <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)

    </details>

4.  <details open>
      <summary><a href="#testing">Testing</a></summary>
      <ul>
      <li><details>
      <summary><a href="#methods">Methods</a></summary>
      
      - [Validation](#validation)
      - [General Testing](#general-testing)
      - [Mobile Testing](#mobile-testing)
      - [Desktop Testing](#desktop-testing)
      </details></li>
      <li><details>
      <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
    </details>

5.  <details open>
      <summary><a href="#deployment">Deployment</a></summary>
      <ul>
      <li><details>
      <summary><a href="#local-deployment">Local Deployment</a></summary>
      
      - [Local Preparation](#local-preparation)
      - [Local Instructions](#local-instructions)
      </details></li>
      <li><details>
      <summary><a href="#github-deployment">Github Deployment</a></summary>
      
      - [Github Preparation](#github-preparation)
      - [Github Instructions](#github-instructions)
      </details></li>
      </ul>
    </details>

6.  <details open>
      <summary><a href="#credit-and-contact">Credit and Contact</a></summary>
      
      - [Content](#content)
      - [Contact](#contact)
    </details>

---

# UX

## Goals

### Visitor Goals

The target audience for Madlibs Pythonare:

- People who want to play a madlibs game.
- People who want to see branching stories.
- People who want create their own story.

User goals are:

- Getting a clear understanding of the game.
- Allow for users to shape their own story
- Be able to replay the game with a new story

Madlib Python fills these needs by:

- Clearly stating how the game is played
- Showing each branch of the story clearly
- Showing confirmation of each decision the player makes
- Displaying in colors what words the user has input to influence the story
- Allowing the user to easily replay the game again

### User Stories

1. As a user interested in making my own stories I want to be able to influence the outcome
2. As a user I'd like to see many different stories
3. I'd like for the game to not be confusing

---

# Features

## Flow-chart

picture of flowchart

### Data Model

The user inputs data in a dictionary called inputs
The game later accesses those inputs to fill out the chosen story

The game uses a dictionary called colorise to store colors and
use them to color the users input words

The game uses a dictionary called word_list to describe to the player
what type of words they should be entering

### Validation

The game uses the function validate_input to check if its a letter, or a number, and if the number entered is in the list of choices being given

### Branches

The game offers 3 different branches at the start

-forest
-desert
-ocean

It then offers 2 more branches of

-good
-evil

### introduction

A brief introduction on what the game is about and explaining
how the users inputs changes the story and how there will be
different branches

### end-message

a message in the end asking if the player wants to play again or quit the game

---

# Feature-Ideas

The introduction and end messages is to give the player a clear understanding of the game with as few words as possible

The Idea of the branching stories is to give the game more replayability

The user inputs are colorised to clearly show the player what their attribution to the story was

The validation helps to stop player confusion and from breaking the game

# Technologies Used

## Languages

- [Python]
  - Interactivity and styling.

## Platforms

- [Heroku](https://heroku.com/)
  - Deployment of the application(Terminal)
- [Github](https://github.com/)
  - Storing code remotely and deployment.
- [Gitpod](https://gitpod.io/)
  - IDE for project development.

## Other Tools

- [chat.gpt](https://chat.openai.com/)
  - Create the stories

---

# Testing

### Validation

CI linter, in case you don't have link: https://pep8ci.herokuapp.com/,

### General Testing

- Each time a feature was added, all the functions were tested to see if there was an impact.
- The site application was sent to friends for feedback and testing.
- .gitignore file has been included to prevent system file commits.

### Manual Testing

table enter number letter

- Testing done through playing the game

### Mobile Testing

- I tested the application personally on my Android device, going through the entire process
- The application was sent to friends and relatives for them to follow the same process. They have tested on their devices, including iOS.

### Desktop Testing

- the majority of testing occurred on vscode.
- The site was tested by friends and relatives on numerous desktop devices.

### Testing User Stories

|     |                                         User story                                         |                                                                                                                                                             Answer to user story |
| --- | :----------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| 1   | "As a user interested in making my own stories I want to be able to influence the outcome" |                                                                                    The game features inputs from the players and show each word they played has written in color |
| 2   |                     "As a user I'd like to see many different stories"                     | The game contains 3 locations each with their own story and later 2 more outcomes of becoming good or evil. These are clearly explained at the start and when the choices appear |
| 3   |                        "I'd like for the game to not be confusing"                         |                 The game features good explinations but also validation, if the user inputs the wrong letters/numbers/choices the game states what was typed wrongly by the user |

## Bugs

### Known Bugs

- No known bugs

### Fixed Bugs

- [Choose_goodevil](https://github.com/PetterJohanssonTilia/Project-3/issues/1)
  After choosing good or evil the terminal still asks you to input the madlib words again. This was fixed with the linked commit to use the previous input words stored in inputs
- [Validating if integer but not if it's the wrong integer](https://github.com/PetterJohanssonTilia/Project-3/issues/2) The validation works to see if its a number you enter but if you enter a number outside of the choices it breaks the game. This was fixed with the commit linked

---

# Deployment

## Local Deployment

### Local Preparation

**Requirements:**
-A terminal of your choice, vscodee being recommended

### Local Instructions

1. Download a copy of the project repository [here](https://github.com/PetterJohanssonTilia/Project-3/archive/refs/heads/main.zip) and extract the zip file
2. Open the run.py file in your terminal
3. Enjoy the aplication!

## Heroku Deployment

### Heroku Instructions

1. Log in to your Heroku account.
   navigate to [madlibs-python](https://madlibs-python-b03353853cb1.herokuapp.com/).
2. Enjoy the application!

## Credits and Contact

### Content

All the stories was generated by chatgpt

### Contact

Please feel free to contact me at `fake.email@hotmail.com`
