# Mastermind

Mastermind or Master Mind is a code-breaking game for two players. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. It resembles an earlier pencil and paper game called Bulls and Cows that may date back a century or more. One player acts as the codemaker and sets the code while the other acts as the codebreaker and attempts to guess it.

There are many variations of the game using colour and letter codes but for simplicity I have chosen to use numbers, with the python random module acting as codemaker. Hence it becomes a single-player game.


### How to play:
- when player starts game, program randomly generates a 4-digit mastercode, ranging from 1-6, inclusive of repeat numbers
- player has 10 tries to guess the code
- after every try, program returns a 2-number list, which corresponds to the number of matching digits in correct positions, and number of matching digits in different positions respectively
- if player guesses the code correctly within 10 tries, he wins and can choose to play again
- if not, code is revealed and player can choose to play again


### Code explanation:
The code is basically a state machine with the states being the count of guesses. It starts from 1 and increases with a step of 1. This state machine is sustained under the condition that self.playing=True.

The returnlst is the feedback for the player after each guess. Through careful usage of f-string and string.replace in two separate 'for' loops, the program runs through each element in the guess to check first for matching digits in the correct positions, then matching digits in different positions, replacing each matching digit with '0' in both the guess and code. In this way, overcounts and undercounts in the returnlst are prevented (eg. when guess: 1111 and code: 1234, returnlst: [1,0], not [1,3]; when guess: 1212 and code: 1122, returnlst: [2,2], not [2,0]). This portion of the coding turned out to be the most tedious with more permutations and edge cases than first anticipated.

If the guess is identical to the code or the no. of tries exceeds 10, self.playing=False and the state machine loop is broken. This is followed by an option of either recursion or exit.
