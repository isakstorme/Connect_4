def copy_position(grid):
    h = len(grid)
    w = len(grid[0])
    copy = [["-", "-", "-", "-", "-", "-", "-"] for i in range(h)]
    for r in range(h):
        for c in range(w):
            copy[r][c] = grid[r][c]
    return copy

def valid_moves(grid):
    h = len(grid)
    w = len(grid[0])
    moves = []
    for c in range(w):
        if grid[h - 1][c] == "-":
            moves.append(c)
    return moves

def copy_and_move(grid, c, p):
    h = len(grid)
    newgrid = copy_position(grid)
    r = 0
    while r < h:
        if newgrid[r][c] == "-":
            break
        r += 1
    
    if r == h:
        return
    newgrid[r][c] = p
    
    return newgrid


def is_row(grid, r, p):
    w = len(grid[0])
    in_seq = 0
    c = 0
    while c < w:
        if grid[r][c] == p:
            in_seq += 1
        else:
            in_seq = 0
        if in_seq == 4:
            return True 
        c += 1
    
    return False

def is_col(grid, c, p):
        h = len(grid)
        in_seq = 0
        r = 0

        while r < h:
            if grid[r][c] == p:
                in_seq += 1
            else:
                in_seq = 0

            if in_seq == 4:
                return True 
            r+= 1
        
        return False

def is_diagonal(grid, p):
    h = len(grid) 
    w = len(grid[0])

    for r in range(h):
        for c in range(w):
            if is_right_diagonal(grid, r, c, p):
                return True
            if is_left_diagonal(grid, r, c, p):
                return True
    
    return False   
    
def is_right_diagonal(grid, r, c, p):
    h = len(grid)
    w = len(grid[0])
    r1 = r + 1
    c1 = c + 1
    r2 = r + 2
    c2 = c + 2
    r3 = r + 3
    c3 = c + 3
    if r3 >= h or c3 >= w:
        return False
    elif grid[r][c] == p and grid[r1][c1] == p and grid[r2][c2] == p and grid[r3][c3] == p:
        return True
    
    return False
    
def is_left_diagonal(grid, r, c, p):
    h = len(grid)

    r1 = r + 1
    c1 = c - 1
    r2 = r + 2
    c2 = c -2
    r3 = r + 3
    c3 = c - 3
    if r3 >= h or c3 < 0:
        return False
    elif grid[r][c] == p and grid[r1][c1] == p and grid[r2][c2] == p and grid[r3][c3] == p:
        return True
    
    return False

def is_winning(grid, p):  # this is likely inefficient. To check if a move results in a win it should be enough to use last move as a starting coordinate for calculating if it is a win
    h = len(grid)
    w = len(grid[0])
    
    for r in range(h):
        if is_row(grid, r, p):
            return True
    for c in range(w):
        if is_col(grid, c, p):
            return True
    
    if is_diagonal(grid, p):
        return True
    return False


def is_full(grid):
    h = len(grid)
    w = len(grid[0])

    for c in range(w):
        if grid[h - 1][c] == "-":
            return False
    
    return True

def display_position(grid):
    h = len(grid)

    for r in range(h - 1, -1, -1):
        print(
            grid[r][0], "  ", grid[r][1], "  ", grid[r][2] 
                ,"  ", grid[r][3], "  ", grid[r][4], "  ", grid[r][5], "  ", grid[r][6])