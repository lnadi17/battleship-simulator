import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class Gameboard:
    # static variables (they aren't intended to change)
    nrows, ncols = 10, 10
    col_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    boat_color = colors.to_rgb('royalblue')
    hit_color = colors.to_rgb('red')
    
    def __init__(self):
        # create board image (initially completely white)
        self.board = np.ones([Gameboard.nrows, Gameboard.ncols, 3])

        # create figure and axes
        self.fig, self.ax = plt.subplots()

        # show all ticks
        self.ax.set_xticks(np.arange(Gameboard.ncols))
        self.ax.set_yticks(np.arange(Gameboard.nrows))

        # set custom labels
        self.ax.set_xticklabels(Gameboard.col_labels)
        self.ax.set_yticklabels(Gameboard.row_labels)
        
        # set up minor ticks
        self.ax.minorticks_on()
        self.ax.set_xticks(np.arange(Gameboard.ncols) + 0.5, minor=True)
        self.ax.set_yticks(np.arange(Gameboard.nrows) + 0.5, minor=True)

        # turn off the display of all ticks
        self.ax.tick_params(which='both', top=False, left=False, right=False, bottom=False)

        # show grid on minor ticks
        self.ax.grid(which='minor', linestyle='-', color='black')

        # set bounds
        self.ax.set_xbound(-0.5, 9.5)
        self.ax.set_ybound(-0.5, 9.5)
        
    # position should be a string or list of strings in [A-J][1-10] format
    def hide_ship(self, *locations):
        for location in locations:
            row = ord(location[0]) - ord('A')
            col = int(location[1:]) - 1
            self.board[row, col] = Gameboard.boat_color
            
    def unhide_ship(self, *locations):
        for location in locations:
            row = ord(location[0]) - ord('A')
            col = int(location[1:]) - 1
            # change square color to white
            self.board[row, col] = 1
    
    def clear(self):
        self.board = np.ones([Gameboard.nrows, Gameboard.ncols, 3])
        for line in self.ax.get_lines():
            line.set_marker(None)
        
    # updates gameboard and returns True if boat was hit
    def shoot(self, location):
        row = ord(location[0]) - ord('A')
        col = int(location[1:]) - 1

        # draw grey hit marker
        self.ax.plot(col, row, marker='X', markersize=15, color='darkgray')

        # check if boat's at current location and change the color of square to red if so
        if (self.board[row, col] == Gameboard.boat_color).all():
            self.board[row, col] = Gameboard.hit_color
            return True
        else:
            return False
        
    # returns matplotlib figure
    def get_figure(self):
        self.update()
        return self.fig
    
    # returns matplotlib axes
    def get_axes(self):
        self.update()
        return self.ax
    
    # applies changes made to board array
    def update(self):
        self.ax.imshow(self.board, origin='upper')
