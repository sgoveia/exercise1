# Check Move

Check Move is an interactive terminal program with three modes of play!

Run program with below command:

    python exercise1.py





### 1. Standard Mode:

Designed to list all possibile coordinate postions "moves" for a given Chess piece (Queen, Rook, Knight) based on an intial starting coordinate, and provides test coverage.

### 2. Target Mode:

Randomly places 8 (opposing) pieces onto the chess board tiles.
Determines the physically most distant tile from current position. Calculates and
outputs the minimum set of moves which the given piece type could take to the most distant tile.

Given that:

* Opposing pieces do not move.

* Opposing pieces may be “captured” along the way by moving to the occupied tile.

* Capturing an opposing piece marks the end of a “move”.

* Provides test coverage.

### 3. Collector Mode

* Randomly places 8 (opposing) pieces onto the chess board tiles.
* Calculates and output the minimum set of moves which the given piece type could take to capture ALL opposing pieces. (For Rook and Queen a single tile move is considered 1 move )
* Provides test coverage.


### Please follow the promt to run a given mode.


To run a test in Standard mode for all possible outcomes for Queen, Knight, and Rook, input
"test" at  prompt, for example:

    2. Please enter Piece(Queen,Knight,Rook): test

To run a test in Target mode for all possible outcomes for Queen, Knight, and Rook, input
"test" at  prompt, for example:

    2. Please enter Piece(Queen,Knight,Rook): test

To run a test in Collector mode for all possible outcomes for Queen, Knight, and Rook, input
"test" at  prompt, for example:

    2. Please enter Piece(Queen,Knight,Rook): test

To Exit program:

    Input "q" at any point to quit


#### Design Chocies:
Devloped with simplisitc modularity in mind, I intintaliy choose to not use classes. The goal was to develop this simple program using a single module to house mutable global data structrues, and with pragmatic clarity make reuse of module method calls.    