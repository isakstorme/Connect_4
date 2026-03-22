from . import connect4helper

class GameNode:
    def __init__(self, grid, move, player_to_move, botsign, opponentsign):
        self.grid = grid
        self.move = move   # move to reach this position
        self.player_to_move = player_to_move
        self.botsign = botsign 
        self.opponentsign = opponentsign
        self.bot_won = connect4helper.is_winning(grid=grid, p=botsign)
        self.opponent_won = connect4helper.is_winning(grid=grid, p=opponentsign)
        self.is_full = connect4helper.is_full(grid=grid)
    
    def children(self):
        next_player_to_move = "y" if self.player_to_move == "r" else "r"
        children = []
        for move in connect4helper.valid_moves(self.grid):
            new_grid = connect4helper.copy_and_move(self.grid, move, self.player_to_move)
            new_node = GameNode(new_grid, move, next_player_to_move, self.botsign, self.opponentsign)
            children.append(new_node)
        return children