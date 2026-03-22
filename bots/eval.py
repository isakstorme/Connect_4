from . import connect4helper

WIN = 1000  # I have duplicated these values, once in alphabetabot and once here. That is a bad sign and should probably be changed somehow
LOSS = -1000 

def evaluate_basic(node):
    if node.bot_won:
        return WIN
    elif node.opponent_won:
        return LOSS
    else:
        return 0
    

def number_possible_diag_wins_down(grid, p):
    h = len(grid)
    w = len(grid[0])
    op = "y" if p == "r" else "r"

    result = 0

    for c in range(w - 4 + 1):
        for r in range(3, h):
            r1, r2, r3 = r - 1, r - 2, r - 3
            c1, c2, c3 = c + 1, c + 2, c + 3
            if grid[r][c] != op and grid[r1][c1] != op and grid[r2][c2] != op and grid[r3][c3] != op:
                result += 1
    
    return result

def number_possible_diag_wins_up(grid, p):
    h = len(grid)
    w = len(grid[0])
    op = "y" if p == "r" else "r"

    result = 0

    for c in range(w - 4 + 1):
        for r in range(h - 4 + 1):
            r1, r2, r3 = r + 1, r + 2, r + 3
            c1, c2, c3 = c + 1, c + 2, c + 3
            if grid[r][c] != op and grid[r1][c1] != op and grid[r2][c2] != op and grid[r3][c3] != op:
                result += 1
    
    return result

def number_possible_vertical_wins(grid, p):
    h = len(grid)
    w = len(grid[0])
    op = "y" if p == "r" else "r"

    result = 0

    for c in range(w):
        for r in range(h - 4 + 1):
            r1, r2, r3 = r + 1, r + 2, r + 3
            if grid[r][c] != op and grid[r1][c] != op and grid[r2][c] != op and grid[r3][c] != op:
                result += 1
    
    return result

def number_possible_horizontal_wins(grid, p):
    h = len(grid)
    w = len(grid[0])
    op = "y" if p == "r" else "r"

    result = 0

    for r in range(h):
        for c in range(w - 4 + 1):
            c1, c2, c3 = c + 1, c + 2, c + 3
            if grid[r][c] != op and grid[r][c1] != op and grid[r][c2] != op and grid[r][c3] != op:
                result += 1
    
    return result

def number_possible_wins(grid, p):  # It could very well be does function has some bug(s)
    number_possible_wins = 0
    h = len(grid)
    w = len(grid[0])

    number_possible_wins += number_possible_horizontal_wins(grid, p)
    number_possible_wins += number_possible_vertical_wins(grid, p)
    number_possible_wins += number_possible_diag_wins_up(grid, p)
    number_possible_wins += number_possible_diag_wins_down(grid, p)

    return number_possible_wins


def evaluate(node): # Idea taken from https://stackoverflow.com/questions/10985000/how-should-i-design-a-good-evaluation-function-for-connect-4
    grid = node.grid
    botsign = node.botsign
    opponentsign = node.opponentsign
    player_to_move = node.player_to_move
    if node.bot_won:
        return WIN
    elif node.opponent_won:
        return LOSS
    elif node.is_full:
        return 0
    else:
        return number_possible_wins(grid, botsign) - number_possible_wins(grid, opponentsign)