
###Introduction 
This is an individual project for EE551 python. #EE551project_gobang

###Proposal
This project aims to implement the Gobang game.
It is one of the competitive games of the World Intellectual Games 
as a purely strategic chess game played by two players. 
The two sides use black and white chess pieces respectively, arranging 
each piece at the intersection of the straight line and the horizontal line 
of the board.
The first one who form the line of 5 chess pieces wins.
This project would offer two game modes, person versus person and person 
versus machine.

###Features
* The chessboard is displayed in the form of a grid in the window.
* For the person versus person mode, you can only put one piece on the 
board at a time with one click. The first click is Black, then the Black and White take 
turns being arranged until one win. After one click, the chess piece color would 
change automatically
* For the person versus machine mode, the player can choose to make the first move
or the second, then play just like the person versus person mode.
* Program runs to judge win or lose after every click. When one side wins, there 
would be one sentence like "You win! Congratulations!" or "You lose. Keep it up!"
displayed in the window.
* When the game result is confirmed, the chess board would be cleared and the new
game would start.

###Logic 
There needs a logic to determine whether one side to win or lose.
After each click, it would count the horizontal and vertical 
axis and the two bevel from the click position respectively to see if the number of pieces of 
the same color reaches 5 or more, judge the winner and the game is over.
Every time when the piece has been arranged, it is necessary to run the logic to judge the win or lose.

###TODO
* Design one 16*16 chess board.
* Design two color chess piece, black and white.
* Design the game interface to select two game modes.
* Apply AI for the person versus machine mode.
* Set how to move chess piece.
* Let the chess board receive and display the new position of latest chess piece.
* Realize the logic of judging win and lose.
* Complete the function resetting when the game result has been confirmed.
* Set the button for quitting game.


