# Check Move

Run program with below command:

    python exercise1.py



Check Move is an interactive terminal program with two modes of play

1. Standard Mode:
Designed to list all possibilecoordinate postions "moves"
for a given Chess piece based on an intial starting coordinate and provides test coverage

2.Target Mode:
Randomly places 8 (opposing) pieces onto the board tiles.
Determine the physically most distant tile from Current position. Calculates and
outputs the minimum set of moves which the given piece type could take to the most distant tile.
Given that:
Opposing pieces do not move.
Opposing pieces may be “captured” along the way by moving to the occupied tile.
Capturing an opposing piece marks the end of a “move”.
Provides test coverage.


Please follow the promt to run a given mode.


To run a test in Standard mode for all possible outcomes for Queen, Knight, and Rook, input
"test" at  prompt, for example:

    2. Please enter Piece(Queen,Knight,Rook): test

To run a test in Target mode for all possible outcomes for Queen, Knight, and Rook, input
"test" at  prompt, for example:

    2. Please enter Piece(Queen,Knight,Rook): test

To Exit program:
    Input "q" at any point to quit

