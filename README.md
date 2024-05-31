<h1>Madlibs Python</h1>
This is a python portfolio-project. <br>
The application is designed to be a game of Madlibs with a branching story.<br>

## Table of Contents

1. <details open>
     
   <summary><a href="#goals">Goals</a></summary>

   - [Visitor Goals](#visitor-goals)
   - [Business Goals](#business-goals)
   - [User Stories](#user-stories)
   </details>

2. <details open>

   <summary><a href="#visual-design">Visual Design<a></summary>

   - [Colors](#colors)

   </details>

3. <details open>
     <summary><a href="#features">Features</a></summary>

   - [Flow chart](#flow-chart)
   - [Branching story](#branching-story)
   - [Input words](#input-words)

4. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

   - [Languages](#languages)
   - [Platforms](#platforms)
   - [Other Tools](#other-tools)

   </details>

5. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <details><summary><a href="#methods">Methods</a></summary>
    
    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details>
      
    <details><summary><a href="#bugs">Bugs</a></summary>
    
    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details>
   </details>

6. <details open>
     <summary><a href="#deployment">Deployment</a></summary>
     <details>
     <summary><a href="#local-deployment">Local Deployment</a></summary>
     
     - [Local Preparation](#local-preparation)
     - [Local Instructions](#local-instructions)
     </details><details>
     <summary><a href="#github-deployment">Github Deployment</a></summary>
     
     - [Github Preparation](#github-preparation)
     - [Github Instructions](#github-instructions)
     </details>
   </details>

7. <details open>
     <summary><a href="#credit-and-contact">Credit and Contact</a></summary>
     
     - [Content](#content)
     - [Contact](#contact)
   </details>

---

# UX

## Goals

### Visitor Goals

The target audience for Madlib Python are:

- People who want to play a game where their choices matters.
- People who want to see how creative they can be.

User goals are:

- Getting an interactive story
- Feeling that they can influence the story
- Freedom to write what they want

Madlibs Python fills these needs by:

- Clearly explaining how the game works
- Explaining what branching stories the user can choose from
- Explaining when the user can input their own words
- Clear error messages if the user gives the wrong input
- Coloring the users inputs to show the user what they've contributed to the story

### User Stories

1. As a user interested in creating a funny story
2. As a user I'd like to see many different stories and outcomes
3. I'd like to clearly know what I can't and what I can write

# Visual Design

## Colors

The colors used all have their corresponding word they're connected to
This increases the readabilty and makes it easier to spot what you as the user
has contributed

# Features

## Functions

### Introduction

hello

### Display branches

hello

### Choices

hello

### Inputs

hello

### Validation

hello

# Feature-Ideas

###

### Player feedback

The Idea is the give the player simple instructions, and simple feedback when they've made an incorrect input

visual feedback comes from the colors of the words from the player

# Technologies Used

## Languages

- [Python]
  - Functions and display.

## Platforms

- [Github](https://github.com/)
  - Storing code remotely and deployment.
- [Gitpod](https://gitpod.io/)
  - IDE for project development.

## Other Tools

- [Chatgpt](https://chat.openai.com/)
  - To create the stories.

---

# Testing

## Methods

### Validation

HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/).

<img src="assets/readme/validator/wc3validator1.png" alt="wc3 validator">

|        |                                index.html                                 |                                                                game.html |
| ------ | :-----------------------------------------------------------------------: | -----------------------------------------------------------------------: |
|        | <img src="assets/readme/validator/html5index1.jpg" alt="html5 validator"> | <img src="assets/readme/validator/html5game1.jpg" alt="html5 validator"> |
| Alerts |                              Trailing slash                               |                                                           Trailing slash |

"Trailing slash on void elements has no effect and interacts badly with unquoted attribute values." This is from the prettier extension to make the code more readable but it has no effect on the code

HTML has been validated with [Wave.webaim HTML5 Validator](https://wave.webaim.org/).
<img src="assets/readme/validator/wavevalidator1.png" alt="wave validator">

|        |                                  index.html                                  |                                                                   game.html |
| ------ | :--------------------------------------------------------------------------: | --------------------------------------------------------------------------: |
|        | <img src="assets/readme/validator/webaimindex1.jpg" alt="webaim validation"> | <img src="assets/readme/validator/webaimgame1.jpg" alt="webaim validation"> |
| Alerts |                                     None                                     |                                       A paragraph is used instead of header |

Website speed optimisation has been checked with [PageSpeed Insights](https://pagespeed.web.dev/).

<img src="assets/readme/validator/pagespeedinsights1.png" alt="page speed insight">

|                    |                                    index.html                                    |                                                                       game.html |
| ------------------ | :------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
|                    | <img src="assets/readme/validator/pagespeedindex1.jpg" alt="page speed insight"> | <img src="assets/readme/validator/pagespeedgame1.jpg" alt="page speed insight"> |
| Performance issues |                                       none                                       |                                                                            none |

Javascript has been checked with [JShint](https://jshint.com/).

<img src="assets/readme/validator/jshint1.jpg" alt="Jshint">

|          |                        |     |
| -------- | :--------------------: | --: |
| Warnings | Const and Let warnings |     |
| Errors   |          None          |     |

When using JSHint to check my JavaScript code, it doesn't recognize the const/let keywords, which is part of ES6 (ECMAScript 2015). This is because JSHint needs to be configured to understand ES6 syntax. Without this configuration, it may flag the use of const as an error, even though it's a valid feature in modern JavaScript.

CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
<img src="assets/readme/validator/wc3cssvalidator1.png" alt="wc3 css validator">
<img src="assets/readme/validator/cssvalidation1.jpg" alt="wc3 css validator results">
Results are no errors found

and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/).
<img src="assets/readme/validator/cssautoprefixer1.png" alt="autoprefixer css online">

Links checked with [W3C Link Checker](https://validator.w3.org/checklink).
<img src="assets/readme/validator/wc3linkerchecker1.png" alt="wc3linkchecker">

All links and anchors are working.

### General Testing

- Each time a feature was added, all the functions were tested to see if there was an impact.
- The site was sent to friends for feedback and testing.
- .gitignore file has been included to prevent system file commits.

### Manual Testing

- Player experience tested by playing the game
- Validation and functionality tested by giving the wrong inputs

### Mobile Testing

- I tested the site personally on my Android device
- The site was sent to friends and relatives for them to follow the same process. They have tested on their devices, including iOS.

### Desktop Testing

- the majority of testing occurred on VSCO.
- The site was tested by friends and relatives on numerous desktop devices.

### Testing User Stories

|     |                            User story                            |                                                                                                                                                                                         Answer to user story |
| --- | :--------------------------------------------------------------: | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| 1   |         "As a user interested in creating a funny story"         |                                                                                                          The game allows for the player to input any words they like after they've chosen their story branch |
| 2   | " As a user I'd like to see many different stories and outcomes" |                                                          The game features 3 branches at the start, and 2 branches in the end, and allows the player to choose freely from the branches and their own inputs |
| 3   |   "I'd like to clearly know what I can't and what I can write"   | The game clearly states what stories can be picked from, if the input should be a letter or a number. Error messages states what the correct input must be. Normal messages states what branch you've picked |

## Bugs

### Known Bugs

- No known bugs

### Fixed Bugs

- [Not using stored inputs](https://github.com/PetterJohanssonTilia/Project-3/issues/1) After choosing the second branch the game didn't use the previously entered inputs
- [Validation not working](https://github.com/PetterJohanssonTilia/Project-3/issues/2)
  The validation didn't work if you input a number outside of the choices range

---

# Deployment

## Local Deployment

### Local Preparation

**Requirements:**

- A terminal of your choice, VSCO recommended.

### Local Instructions

1. Download a copy of the project repository [here](https://github.com/PetterJohanssonTilia/Project-3/archive/refs/heads/main.zip) and extract the zip file
2. Open the app.py in your terminal
3. Enjoy the game!

## Github Deployment

### Github Preparation

- It is possible to copy or clone the repository to directly for deployment,
  **Requirements:**
- A free GitHub account.
- A free EmailJS account.

### Github Instructions

1. Log in to your GitHub account.
   navigate to [https://github.com/PetterJohanssonTilia/Project-3](https://github.com/PetterJohanssonTilia/Project-3).
1. You can set up your own repository and copy or clone it, or you fork the repository.
1. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
1. GitHub pages will update from the Main branch by default.
1. Go to the **Settings** page of the repository.
1. Scroll down to the **Github Pages** section.
1. Select the Main Branch as the source and **Confirm** the selection.
1. Wait a minute or two and it should be live for viewing.

## Credits and Contact

### Content

All the image content was from pixabay.com and all the objects and their weights was generated by chatgpt

### Contact

Please feel free to contact me at `fake.email@hotmail.com`
