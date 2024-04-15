# _Lam_

Lam is a pure Python language program, running in Code Institute mock terminal deployed on Heroku.

Feel free to challenge yourself in this nostalgic game, while using your memory and your deduction skills to guess the right animal name in english.

  ![Mock Up](/assets/images/Mockup.png)

## How to play

DESCRIBE HOW TO PLAY THE GAME

## Features

### Existing Features

- __WHAT THIS DO?__

 - BLA BLA BLA BLA
 - BLA BLA BLA

  ![Land Page](/assets/images/Start-Page.png)

- __WHAT THIS DO?__

 - BLA BLA BLA BLA


  ![Guesses Conditions](/assets/images/)

- __WHAT THIS DO?__

 - BLA BLA BLA BLA

  ![ Stages](/assets/images/)

- __Game Over Menssage__
 
  - BLA BLA BLA.

  ![Game Over](/assets/images/Game-Over.png)

### Features Left to Implement

  - WHAT WOULD BE GOOD TO IMPLEMENT??
  - WHAT WOULD BE GOOD TO IMPLEMENT??
  - WHAT WOULD BE GOOD TO IMPLEMENT??

## Testing

  - I have tested the code by the following methods:
  - Passed on the validator code PEPE8, no issues found.
  - I manually tested the code, passing invalid inputs, such as, more than one letters, numbers, spaces, special characters etc.
  - I tried all possibles ways to win or lose the game, and no bugs were found.
  - The game was tested on Heroku terminal and on the local terminal.

## Validator Testing

  - No errors were returned when passing through the official [PEP8](https://pep8ci.herokuapp.com/) validator.

  ![PEP8 Validator](/assets/images/PEP8.png)

## Bugs

### Solved Bugs

  - When I wrote the function to check if the guess was in the word, the code unexpectedly appended two characters in the same index list, if they both were in the word, causing me a problem to evaluates when the game was finished, that error occurred because I allowed the user to input two characters strings as a guess, the solution was to accept only the whole word or one single character.
  - When I fixed the bug described above, I didn't get the expected logical result when I inputed the word to be guessed, that happened because I was checking if the user inputted only one letter before checking if the user had guessed the whole word, in other words, was a flow bug.

### Reaming Bugs
  
  - No bugs reaming

## Deployment

  - This project was deployed at Heroku, steps for deploy are listed bellow:
    - Fork or clone the repository.
    - Creat a new Heroku app.
    - Set up the configs for the deployment.
    - Link the Heroku app to the repository, then Deploy.

    - The live link can be found here: [My Game](https://)

## Credits:

  - I also searched for solutions of the problems that occurred during the project development on the following websites:
    - [Stackoverflow](https://stackoverflow.com/)
    - [Geeksforgeeks](https://www.geeksforgeeks.org/)
    - [Freecodecamp](https://www.freecodecamp.org/news)
  - The Code Institute for the deployment terminal