# adventure_game.py
for this project, the idea is to focus on some key things that we need if want to make a working game:
1. One thing the game will need to do is to print messages for the player to describe what is happening. Like at the start of the example game, these lines are printed:
    You find yourself standing in an open field, filled with grass and yellow wildflowers.  
    Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.
2. Pausing between printing descriptions to add some delay
3. you'll need to get some input from the player, and then change what happens depending on what that input is
4. Make sure the player gives a valid input, your program should not crash on invalid input.
5. The game also includes some random factors, so that it's a little different each time (Used some randomness in game)
6. The game has conditions for winning and losing.
7. When the game is over, it asks if the player wants to play again.



CRITERIA                                                =>     MEETS SPECIFICATIONS
* Output text to the console.				==> 	  * Descriptions are printed to the console for the player to see.
* Import modules and use functions 
from thosemodules.                          ==>       * The time.sleep function is used to create delays between messages so that they aren't all printed at once.
					              * The random.choice or random.randint function is used to influence the game so that each game is different insome way.
* Use the input function in combination
with conditional statements(e.g., if and while) ==>   *The input function is used to ask the player what they would like to do.
								The player's choices affect what happens in the game, including:
									* Whether the player wins or loses
									* Whether to restart or exit after the game is over
									* to create an interactive program.  
														 			
* Use a conditional loop to handle invalid input.==> * If the player enters a choice that is not valid, the game gives them the chance to retry until they enter a valid option.
						     * The game does not crash and does not treat invalid input as a valid choice.
* Refactor code by defining and calling functions. ==> * The code includes at least four function definitions that are used to improve the code in some way, such as by:
								* Reducing repetition
								* Reducing complexity
								* Improving the readability or organization of the code
								* Each function should have a single purpose and a name that describes that purpose.

* Write code that follows the standard Python style guide. ==>  * The pycodestyle tool reports zero errors and zero warnings.
* Test code and produce an error-free program.            ==>   * The program is a playable game, and runs from start to finish without crashing or displaying errors.
