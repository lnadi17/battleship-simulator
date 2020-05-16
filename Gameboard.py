# import all necessary libraries
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
        
        # initialize counters
        self.alive_boat_count = 0
        self.shot_count = 0
        self.hit_count = 0
        
    # position should be a string or list of strings in [A-J][1-10] format
    def hide_ship(self, *locations):
        for location in locations:
            self.alive_boat_count += 1
            row = ord(location[0]) - ord('A')
            col = int(location[1:]) - 1
            self.board[row, col] = Gameboard.boat_color
            
    def unhide_ship(self, *locations):
        for location in locations:
            self.alive_boat_count -= 1
            row = ord(location[0]) - ord('A')
            col = int(location[1:]) - 1
            # change square color to white
            self.board[row, col] = 1
    
    def clear(self):
        self.alive_boat_count = 0
        self.shot_count = 0
        self.hit_count = 0
        self.board = np.ones([Gameboard.nrows, Gameboard.ncols, 3])
        #for line in self.ax.get_lines():
        #    line.set_marker(None)
        self.ax.lines = []
        
    # updates gameboard and returns True if boat was hit
    def shoot(self, location):
        self.shot_count += 1
        
        row = ord(location[0]) - ord('A')
        col = int(location[1:]) - 1

        # draw grey hit marker
        self.ax.plot(col, row, marker='X', markersize=15, color='darkgray')

        # check if boat's at current location and change the color of square to red (destroy ship) if so
        if (self.board[row, col] == Gameboard.boat_color).all():
            self.board[row, col] = Gameboard.hit_color
            self.alive_boat_count -= 1
            self.hit_count += 1
            return True
        else:
            return False
        
    # returns True if all ships are destroyed
    def is_game_over(self):
        if self.alive_boat_count == 0:
            return True
        return False
    
    # returns number of boats currently alive
    def get_alive_count(self):
        return self.alive_boat_count
    
    # returns how many shots have been made so far
    def get_shot_count(self):
        return self.shot_count
    
    # returns how many ships are hit
    def get_hit_count(self):
        return self.hit_count
    
    # returns accuracy (# of hits) / (# of shots)
    def get_accuracy(self):
        if self.shot_count == 0:
            return 0
        else:
            return self.hit_count / self.shot_count
        
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