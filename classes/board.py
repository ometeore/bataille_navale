import random
from random import randint

class Board:
    """ The class for creating and showing the state of the board
    method: 
    __init__(length of x(int), length of y(int)) crate the matrix (list of list)
        
    populate (boat)---> add boats on random position in the board
    
    position_aload (boat.length)---> return a list of tuple 
        wich are all the valid position a boat can take on the curent board
    
    """

    def __init__(self, length_x, length_y):
        """ init du board """

        self.length_x = length_x
        self.length_y = length_y
        self.matrice = []
        for line in range(length_y):
            self.matrice.append(['X'] * length_x)


    def __repr__(self):
        """ repr du plateau 
        all show in terminal"""

        #ToDo Could be good to show letters (A B C D ...) in columns and number in lines

        str_board = "\n\n"
        for line in self.matrice:
            for elm in line:
                if elm == 'X':
                    str_board = str_board + "|" + " "
                else:
                    str_board = str_board + "|" + elm
            str_board = str_board + "|\n" #+ '_' * self.length_y * 2 + "\n" # didnt look nice
        return str_board



    def populate(self, boat):
        """ 
            return True if no position valid for a boat in the board
            return False if there was a solution and place it in self.matrice 
        """
        aload_all =self.position_aload(boat.length)
        if aload_all == []:
            return True
        else:
            position = random.choice(aload_all)
            for case in range(boat.length):
                if position[2]: #vertical
                    self.matrice[position[0] + case][position[1]] = boat.letter
                else: #horizontal
                    self.matrice[position[0]][position[1] + case] = boat.letter
            return False


    def position_aload(self, length):
        """
            return a list of tuple considering all position and the direction associated
            for aboat with length (int) 
            (length[int]) --->  [(0,0,True),...] where True mean vertical
        """
        fail_pos = False
        result = []

        #here we try to find horizontal free space
        for i in range(self.length_y):
            for j in range(self.length_x - length + 1):
                for l in range(length + 2):
                    try:        #This try catch if we are after the limit of the board
                        if j + l - 1 >= 0:
                            if self.matrice[i][j + l - 1] != 'X':
                                break
                            if self.matrice[i - 1][j + l - 1] != 'X' and i - 1 >= 0:
                                break
                            if self.matrice[i + 1][j + l - 1] != 'X':
                                break                  
                    except IndexError:
                        pass
                else:  #This else is for the for loop
                    result.append((i,j,False))

        
        #now it is vertical
        for i in range(self.length_y - length + 1):
            for j in range(self.length_x):
                for l in range(length + 2):
                    try:        #This try catch if we are after the limit of the board
                        if i + l - 1 >=0:
                            if self.matrice[i + l - 1][j] != 'X':
                                break
                            if self.matrice[i + l - 1][j - 1] != 'X' and j - 1 >= 0:
                                break 
                            if self.matrice[i + l - 1][j + 1] != 'X':
                                break
                    except IndexError:
                        pass
                else:  #This else is for the for loop
                    result.append((i,j,True))
        return result