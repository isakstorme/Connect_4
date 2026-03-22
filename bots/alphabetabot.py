from . import connect4helper
from .gamenode import GameNode

class AlphaBetaBot:   # This bot uses minimax with Alpha Beta pruning
    def __init__(self, bot, opponent, maxdepth):
        self.bot = bot
        self.opponent = opponent
        self.maxdepth = max(maxdepth, 1)
        self.INF = 1000000
        self.WIN = 1000
        self.LOSS = -1000
    
    
    def evaluate(self, node): # One could imagine this class but where the function evaluate is taken as an argument to have high flexibility. (strategy pattern?)
        if connect4helper.is_winning(node.grid, self.bot):
            return self.WIN
        elif connect4helper.is_winning(node.grid, self.opponent):
            return self.LOSS
        else:
            bad_height = 0
            for c in range(7):
                r = 5
                while node.grid[r][c] != node.player_to_move and r >= 0:
                    r -= 1
                bad_height -= r * 5
            return bad_height

    def alpha_beta(self, node, depth, alpha, beta, max_mode):  # max_mode = True or False 
        value = self.evaluate(node)
        if depth == 0 or value == self.WIN or value == self.LOSS:
            return value, None
        
        bestmove = None
        if max_mode:
            value = -self.INF
            for child in node.children():
                value = max(value, self.alpha_beta(node=child, depth=depth - 1, alpha=alpha, beta=beta, max_mode=False)[0])
                if value > alpha:
                    alpha = value
                    bestmove = child.move
                    if beta <= alpha:
                        #print(beta)
                        break
        else:
            value = self.INF
            for child in node.children():
                value = min(value, self.alpha_beta(node=child, depth=depth - 1, alpha=alpha, beta=beta, max_mode=True)[0])
                if value < beta:
                    beta = value
                    bestmove = child.move
                    if beta <= alpha:
                        break
        return value, bestmove

    def pick_move(self, node):
        move = self.alpha_beta(node=node, depth=self.maxdepth, alpha=-self.INF, beta=self.INF, max_mode=True)[1]
        #print(self.alpha_beta(node=node, depth=self.maxdepth, alpha=-self.INF, beta=self.INF, max_mode=True)[0])
        return move
        

    def move(self, grid, player_to_move):

        node = GameNode(grid, None, player_to_move, self.bot, self.opponent)
        return self.pick_move(node)