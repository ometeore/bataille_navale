from classes.boat import Boat
import pytest

def test_init():

    boat1 = Boat(1)
    boat2 = Boat(2)
    boat3 = Boat(3)
    boat4 = Boat(4)

    with pytest.raises(Exception) as e:
        boat20 = Boat(20)
    
    assert str(e.type) == "<class 'ValueError'>"
    assert boat1.letter == 'S'
    assert boat2.letter == 'T'
    assert boat3.letter == 'E'
    assert boat4.letter == 'C'