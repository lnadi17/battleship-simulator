import random as pyrandom

class Random:
    def __init__(self):
        # possible locations list isn't affected by the methods
        self.possible_locations = []
        self.available_locations = []
        for i in Gameboard.row_labels:
            for j in Gameboard.col_labels:
                self.possible_locations.append(i + str(j))
                self.available_locations.append(i + str(j))
        
    def reset_available_locations(self):
        self.available_locations = self.possible_locations.copy()
        
    # chooses random location from available locations list and removes it if keep is False
    def choose(self, keep=False):
        choice = pyrandom.choice(self.available_locations)
        if not keep:
            self.available_locations.remove(choice)
        return choice
    
    # returns random location from possible locations list
    def choose_from_all(self):
        return pyrandom.choice(self.possible_locations)
    
    # generates random locations for ships of various length and returns them
    # WARGING: current implementation is not optimal and should be changed sometime in the future
    # NOTE: this method currently uses choose method but it resets available locations at the end
    def generate_ship_locations(self, lengths=[5, 4, 3, 3, 2]):
        locations = []
        
        for length in lengths:
            orientation = pyrandom.choice(['horizontal', 'vertical'])
            
            # randomize a ship location until it fits
            while True:
                choice_pivot = self.choose(keep=True)
                choices = [choice_pivot]
                if orientation == 'horizontal':   
                    # generate all other choices (for horizontal orientation)
                    for i in range(length - 1):
                        # when orientation is horizontal, column is changed
                        choice_next = choice_pivot[0] + str(int(choice_pivot[1:]) + i + 1)
                        choices.append(choice_next)
                else:
                    # generate all other choices (for vertical orientation)
                    for i in range(length - 1):
                        # when orientation is vertical, row is changed
                        choice_next = chr(ord(choice_pivot[0]) + i + 1) + choice_pivot[1:]
                        choices.append(choice_next)
                # after generation, we must check if locations are legal
                is_legal = True
                for choice in choices:
                    if choice not in self.available_locations:
                        is_legal = False
                # if they're legal, we update available locations and break the loop
                if is_legal:
                    self.available_locations = [x for x in self.available_locations if x not in choices]
                    locations += choices
                    break
        
        # reset available locations and return result
        self.reset_available_locations()
        return locations