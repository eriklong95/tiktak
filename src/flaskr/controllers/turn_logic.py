def derive_turn(game):
    '''
        Return 'A' or 'B' dependending on whose turn it is
        in the game passed a argument. Player A always starts
        the game. 
        
        Raise an exception if the game is in an invalid state.
    '''
    return 'A' if len(game.moves) % 2 == 0 else 'B'

