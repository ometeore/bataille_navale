from classes import ui
# import mock 

# def test_player_choice1():
#     with mock.patch.object(__builtins__, 'input', lambda: 7):
#         assert ui.player_choice1() == [7,7,7]

def test_prout():
    valid_input_values = [7,7,7]
    wrong_input_values = [4,2,1,7,7,7]
    
    output = []
    
    def mock_input(s):
        output.append(s)
        return valid_input_values.pop(0)

    ui.input = mock_input

    assert ui.player_choice1() == [7,7,7]

    def mock_input(s):
        output.append(s)
        return wrong_input_values.pop(0)
    
    ui.input = mock_input
    ui.print = lambda s : output.append(s)

    assert ui.player_choice1() == [7,7,7]
    assert output == [
        '\n    largeur du plateau?\n',
        '\n'
        '    hauteur du plateau?\n',
        '\n'
        '    Combien de plateaux?\n',
        '\n'
        '    largeur du plateau?\n',
        '\n'
        '    hauteur du plateau?\n',
        '\n'
        '    Combien de plateaux?\n',
        '\n'
        '    Tableau trop petit, choisissez des dimensions plus grandes',
        '\n'
        '    largeur du plateau?\n',
        '\n'
        '    hauteur du plateau?\n',
        '\n'
        '    Combien de plateaux?\n',
        ]


def test_player_choice2():
    valid_input_values = ["bv",7,2]
    output = []
    def mock_input(s):
        output.append(s)
        return valid_input_values.pop(0)
    ui.input = mock_input

    assert ui.player_choice2() == False 
