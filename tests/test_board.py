from classes.board import Board
from classes.boat import Boat

def test_populate():

    boat1 = Boat(1)
    boat2 = Boat(2)
    boat3 = Boat(3)
    boat4 = Boat(4)

    board22 = Board(2,2)
    board77 = Board(7,7) 

    assert board22.populate(boat4) == True
    
    assert board77.populate(boat4) == False
    assert board77.populate(boat3) == False
    assert board77.populate(boat2) == False
    assert board77.populate(boat1) == False

    number_of_blank = 0

    for ligne in board77.matrice:
        for elm in ligne:   
            if elm == 'X':
                number_of_blank = number_of_blank + 1
    assert number_of_blank == 39

def test_position_aload():
    
    board44 = Board(4,4) #wich is not smart cause user cant do this
    list_of_places = board44.position_aload(4)

    assert len(list_of_places) == 8

    board44.populate(Boat(4))

    assert len(list_of_places)

def test_repr():
    boar = Board(4,4)
    assert isinstance(boar.__repr__(), str)

def test_init():
    board = Board(4,4)
    assert len(board.matrice) == 4
    assert len(board.matrice[0]) == 4
