def derive_turn(game):
    moves_from_a = [m for m in game.moves if m.occupier == 'A']
    moves_from_b = [m for m in game.moves if m.occupier == 'B']
    if len(moves_from_a) == len(moves_from_b):
        return 'A'
    elif len(moves_from_a) - 1 == len(moves_from_b):
        return 'B'
    else:
        raise Exception('Game in invalid state')
