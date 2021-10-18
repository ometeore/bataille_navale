class Boat:
    """ Boats ^^
    __init__(length of the boat(int))
    self.letter = C if length 4, E if 3, T if 2, S if 1"""

    def __init__(self, length):

        self.length = length

        letter_list = [(1,'S'),(2,'T'),(3,'E'),(4,'C')]

        for tup in letter_list:

            if self.length == tup[0]: 

                self.letter = tup[1]
                break

        else:

            raise ValueError("Boat must be in 1 to 4 size")


    def __repr__(self):
        return "this boat have a {} case size".format(self.length)