class Connect4:
    def __init__(self):
        self.grid = self.init_grid()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.players = ["y", "r"]
        self.player_to_move = "y" # It seems yellow starts in connect4
        self.yellow_wins = False
        self.red_wins = False
        self.game_drawn = False
        self.game_finished = False

    
    def init_grid(self):
        result = []
        for r in range(6):
            result.append(["-", "-", "-", "-", "-", "-", "-"])
        return result
    
    def display_position(self):
        for r in range(self.height - 1, -1, -1):
            print(
                self.grid[r][0], "  ", self.grid[r][1], "  ", self.grid[r][2] 
                ,"  ", self.grid[r][3], "  ", self.grid[r][4], "  ", self.grid[r][5], "  ", self.grid[r][6])
        print("____________________________")
    
    def move(self, c):
        if self.game_finished:
            return
        
        r = 0
        while self.grid[r][c] != "-":
            r += 1
            if r == self.height:
                return
        
        self.grid[r][c] = self.player_to_move
        if self.is_winning(self.player_to_move):
            self.set_player_win(self.player_to_move)
        elif self.is_full():
            self.set_draw()

        self.player_to_move = "y" if self.player_to_move == "r" else "r"



    def is_row(self, r, p):
        in_seq = 0
        c = 0

        while c < self.width:
            if self.grid[r][c] == p:
                in_seq += 1
            else:
                in_seq = 0

            if in_seq == 4:
                return True 
            c += 1
        
        return False
    
    def is_col(self, c, p):
        in_seq = 0
        r = 0

        while r < self.height:
            if self.grid[r][c] == p:
                in_seq += 1
            else:
                in_seq = 0

            if in_seq == 4:
                return True 
            r+= 1
        
        return False
    
    def is_diagonal(self, p):
        for r in range(self.height):
            for c in range(self.width):
                if self.is_right_diagonal(r, c, p):
                    return True
                if self.is_left_diagonal(r, c, p):
                    return True
        
        return False   
    
    def is_right_diagonal(self, r, c, p):
        r1 = r + 1
        c1 = c + 1
        r2 = r + 2
        c2 = c + 2
        r3 = r + 3
        c3 = c + 3
        if r3 >= self.height or c3 >= self.width:
            return False
        elif self.grid[r][c] == p and self.grid[r1][c1] == p and self.grid[r2][c2] == p and self.grid[r3][c3] == p:
            return True
        
        return False
    
    def is_left_diagonal(self, r, c, p):
        r1 = r + 1
        c1 = c - 1
        r2 = r + 2
        c2 = c -2
        r3 = r + 3
        c3 = c - 3
        if r3 >= self.height or c3 < 0:
            return False
        elif self.grid[r][c] == p and self.grid[r1][c1] == p and self.grid[r2][c2] == p and self.grid[r3][c3] == p:
            return True
        
        return False

    def is_winning(self, p):  # this is likely inefficient. To check if a move results in a win it should be enough to use last move as a starting coordinate for calculating if it is a win
        for r in range(self.height):
            if self.is_row(r, p):
                return True

        for c in range(self.width):
            if self.is_col(c, p):
                return True
        
        if self.is_diagonal(p):
            return True

        return False
        

    
    def is_full(self):
        for c in range(self.width):
            if self.grid[self.height - 1][c] == "-":
                return False
        
        return True
    
    def set_player_win(self, p):
        if p == "r":
            self.red_wins = True
        elif p == "y":
            self.yellow_wins = True
        
        self.game_finished = True
    
    def set_draw(self):
        self.game_drawn = True
        self.game_finished = True