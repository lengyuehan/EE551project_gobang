### Introduction 
This is an individual project for EE551 python. #EE551project_gobang

### Proposal
This project aims to implement the Gobang game.
It is one of the competitive games of the World Intellectual Games 
as a purely strategic chess game played by two players. 
The two sides use black and white chess pieces respectively, arranging 
each piece at the intersection of the straight line and the horizontal line 
of the board.
The first one who form the line of 5 chess pieces wins.
This project offer mode person versus person.

### Features
* The chessboard is displayed in the form of a grid in the window.
* Player can only put one piece on the chessboard at a time with one click. 
The first click is Black, then the Black and White take 
turns automatically until one side win. After one click, the chess piece color would 
change automatically and the hint label would change automatically too.
* Program runs to judge win or lose after every click. When one side wins, there 
would be one sentence like "Black win! Congratulations!" or "White win! Congratulations!"
displayed in a message box.
* When the game result is confirmed, the chessboard would be cleared and the new
game would start.

### Logic 
There needs a logic to determine whether one side to win or lose.
After each click, it would count the horizontal and vertical 
axis and the two bevel from the click position respectively to see if the number of pieces of 
the same color reaches 5 or more, judge the winner and the game is over.
Every time when the piece has been arranged, it is necessary to run the logic to judge the win or lose.

### Optimization Direction
* Design the game interface to select two game modes.
* Apply AI for the person versus machine mode.

### TODO
* Draw one 15*15 chessboard.
* Draw two color chess pieces, black and white.
* Connect the mouse click action to the canvas of the chessboard.
* Let the chess board receive and display the new position of latest chess piece.
* Realize the logic of judging win and lose.
* Set the label as a hint about the black turn or white turn changed automatically.
* Draw a button for 'Restart'.
* Set the function restart when the 'Restart' button has been clicked.
* Complete the function restart when the game result has been confirmed.
* Create the individual window for this game.
* Record a video on screen to demonstrate how this program (Gobang game) work as the test.
