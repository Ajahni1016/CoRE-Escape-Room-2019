# CoRE Escape Room 2019
A puzzle created for the CoRE 2019 Escape Room

The final Mastermind puzzle is hidden behind 4 code words that need to be found and inputted before the player(s) can proceed.

![Title Screen](/designs/TitleScreenLocked.png)

When the program is started, the screen above is shown. This screen is controlled only through the mouse. Nothing will happen if the players try to use the keyboard. The 4 lock icons represent each of the code words that need to be found. On the successful input of a code, one of the locks will open and the password will be displayed next to it. 


If the unlock button is clicked then the following input screen will open up:

![Blank Input](/designs/InputScreenBlank.png)

From here the player can type in any word that they believe may be one of the codes and click on the [ENTER] button to test it. Once the [ENTER] button is clicked, the only way to proceed is to press the [BACK] button. 

The 4 code words are WHALE, NAVY, DRIZZLE, and KELP.

If the code is incorrect, a locked padlock will appear above the input box.

![Wrong input](/designs/InputScreenWrong.png)

if the code is correct, an unlocked padloc will appear above the input box.

![Corrent input](/designs/InputScreenRight.png)

Once all 4 code words are entered, the main menu will appear as follows:

![Title Unlocked](/designs/TitleScreenUnlocked.png)

If the [UNLOCK] button is pressed at this point, screen will switch to the Mastermind Puzzle.

![Lights off](/designs/MastermindBlank.png)

The player(s) can click on any button on the keypad to input a number and the [CLR] and [ENT] buttons stand for clear and enter, respectively.

When the [ENT] button is pressed and 4 digits have been selected, the lights on the left and right sides will light up. 

![Lights on](/designs/MastermindAttempt.png)

A blue light means that one of the numbers selected is the correct, but it's in the wrong spot in the code.
A green light means that one of the numbers selected is both in the code and in the right spot.

![Correct code](/designs/MastermindComplete.png)

4 green lights indicates that the correct code has been found and the game is over.
