def player_choice1():
    limit_rules = [(1,29),(2,29),(3,14),(4,13),(5,11),(6,9),(7,7)]

    complete = True
    while complete:
        largeur = input("\n    largeur du plateau?\n")
        hauteur = input('\n    hauteur du plateau?\n')
        number_of_boards = input("\n    Combien de plateaux?\n")
        try:
            numb = int(number_of_boards)
            for rule in limit_rules:
                if int(largeur) < int(hauteur) :
                    if rule[0] == int(largeur) and int(hauteur) < rule[1]:
                        print("\n    Tableau trop petit, choisissez des dimensions plus grandes")
                        break
                else:
                    if rule[0] == int(hauteur) and int(largeur) < rule[1]:
                        print("\n    Tableau trop petit, choisissez des dimensions plus grandes")
                        break
            else:
                complete = False
        except ValueError:
            print("\n    Choisissez un entier")

    return [int(largeur), int(hauteur), numb]

def player_choice0():
    print("###########################################\n\n")
    print("     Hello...\n    Wanna play?\n\n")
    print("\n\n    Renseignez la valeur demandée puis appuyez sur enter.\n\n")
    choice0 = input("    1.  Créer des plateaux\n    2.  Quitter\n")
    complete = True

    while complete:
        try:
            if int(choice0) in [1, 2]:
                complete =False
            else:
                print("\n    Choisissez 1 ou 2 puis appuyez sur enter")
                choice0 = input("    1.  Créer des plateaux\n    2.  Quitter\n")
        except ValueError:
            print("\n    Choisissez un nombre")
            print("    Choisissez 1 ou 2 puis appuyez sur enter")
            choice0 = input("    1.  Créer des plateaux\n    2.  Quitter\n")


    if int(choice0) == 1:
        return True

    else: 
        return False
    
def player_choice2():
    choice0 = input("    1.  Encore\n    2.  Quitter\n")
    complete = True

    while complete:
        try:
            if int(choice0) in [1,2]:
                complete = False
            else:
                print("\n    Appuyez sur 1 ou 2 puis enter")
                choice0 = input("    1.  Encore\n    2.  Quitter\n")
        
        except ValueError:
            print("\n    Renseigner un entier")
            print("\n    Appuyez sur 1 ou 2 puis enter")
            choice0 = input("    1.  Encore\n    2.  Quitter\n")


    if int(choice0) == 1:
        return True

    else: 
        return False