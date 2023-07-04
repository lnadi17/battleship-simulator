# battleship-simulator

Battleship game simulator based on [DataGenetics' battleship analysis.](http://www.datagenetics.com/blog/december32011/) There are multiple Jupyter Notebooks which implement different game strategies and their statistical analysis.

## Notebooks

- **random-strategy.ipynb** - The first possible strategy implemented. It is to make shots totally at random. It implements Random strategy class, calculates number of shots and accuracy distribution.
- **hunt-and-target-strategy.ipynb** - This strategy greatly improves the result. Initially, shots can be fired at random, but once part of a ship has been hit, it's possible to search up, down, left and right looking for more of the same ship. This notebook also calculates shot and accuracy distributions.
- **hat-with-parity-strategy.ipynb** - This strategy makes a slight improvement to the Hunt part of the hunt and target algorithm using parity. Because the minimum length of a ship is two units long, we don't need to random search every location on the board. Even the shortest ship has to span two adjacent squares.
- **final-strategy** - This is the most effiecient strategy that can be implemented when playing a fair battleship game. It calculates the probability distribution of ship cells on the board. Then the most probable cell is chosen to be shot at.
