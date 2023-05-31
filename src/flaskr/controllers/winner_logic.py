def find_winner(game):
    '''
        Return the winner of the game passed as argument
        by returning the string 'A' or the string 'B'.
        
        Return the string 'undecided' if the game has no winner.
    '''
    moves = game.moves
    
    if player_has_won(moves, 'A'):
        return 'A'
    
    if player_has_won(moves, 'B'):
        return 'B'
    
    return 'undecided'


def player_has_won(moves, player):
    player_moves = get_player_moves(moves, player)

    has_row_win = any([has_win_in_row(player_moves, i) for i in indices])
    has_col_win = any([has_win_in_col(player_moves, i) for i in indices])
    has_diag_win = has_player_won_on_diagonal(player_moves)

    return has_row_win or has_col_win or has_diag_win

def get_player_moves(moves, player):
    return [m for m in moves if m.occupier == player]

def has_win_in_row(moves, i):
    return len([m for m in moves if m.y == i]) == 3

def has_win_in_col(moves, i):
    return len([m for m in moves if m.x == i]) == 3

indices = [0,1,2]

def has_win_in_col(moves, i):
    return len([m for m in moves if m.x == i]) == 3

def has_player_won_on_diagonal(moves):
    diag1 = len([m for m in moves if m.x == m.y]) == 3
    diag2 = len([m for m in moves if m.x == 2 - m.y]) == 3
    return diag1 or diag2


