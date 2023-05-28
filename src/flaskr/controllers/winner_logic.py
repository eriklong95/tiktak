def find_winner(game):
    '''
        Return the winner of the game passed as argument
        by returning the string 'A' or the string 'B'.
        
        Return the string 'undecided' if the game has no winner.
    '''
    if player_won(game, 'A'):
        return 'A'
    elif player_won(game, 'B'):
        return 'B'
    else:
        return 'undecided'


def player_won(game, role):
    moves_for_this_player = [m for m in game.moves if m.occupier == role]
    if len(moves_for_this_player) < 3:
        return False
    
    sum_of_xs = sum([m.x for m in moves_for_this_player])
    sum_of_ys = sum([m.y for m in moves_for_this_player])

    if sum_of_xs % 3 == 0 and sum_of_ys % 3 == 0:
        return True
    else:
        return False
