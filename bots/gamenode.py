from . import connect4helper

class GameNode:
    def __init__(self, grid, move, player_to_move, bot, opponent):
        self.grid = grid
        self.move = move   # move to reach this position
        self.player_to_move = player_to_move
        self.bot = bot  # I don't think self.bot and self.opponent are needed in the class, might remove.
        self.opponent = opponent
        self.value = 0
    
    def children(self):
        next_player_to_move = "y" if self.player_to_move == "r" else "r"
        children = []
        for move in connect4helper.valid_moves(self.grid):
            new_grid = connect4helper.copy_and_move(self.grid, move, self.player_to_move)
            new_node = GameNode(new_grid, move, next_player_to_move, self.bot, self.opponent)
            children.append(new_node)
        return children