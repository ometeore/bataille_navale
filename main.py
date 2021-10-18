from classes.board import Board
from classes.boat import Boat
from classes.ui import player_choice1, player_choice0, player_choice2

if __name__ == "__main__":
        choice0 = player_choice0()
        
        while choice0:

                board_dimension = player_choice1()
                Fleet = [
                        Boat(4),
                        Boat(3), Boat(3),
                        Boat(2), Boat(2), Boat(2),
                        Boat(1), Boat(1), Boat(1), Boat(1)
                ]

                for i in range(board_dimension[2]):

                        positionate_valid = False

                        while not positionate_valid:
                        
                                board = Board(board_dimension[0], board_dimension[1])

                                for ship in Fleet:
                                        if(board.populate(ship)):
                                                break
                                else:
                                        positionate_valid = True

                        print(board)
                
                choice0 = player_choice2()
        
        else: 
                print("Ok bye")