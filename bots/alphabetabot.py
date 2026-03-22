from .gamenode import GameNode
from .import eval

class AlphaBetaBot:   # This bot uses minimax with Alpha Beta pruning
    def __init__(self, botsign, opponentsign, maxdepth, evaluate=eval.evaluate):
        self.botsign = botsign
        self.opponentsign = opponentsign
        self.maxdepth = max(maxdepth, 1)
        self.INF = 1000000
        self.WIN = 1000
        self.LOSS = -1000
        self.evaluate = evaluate
    

    def alpha_beta(self, node, depth, alpha, beta, max_mode):  # max_mode = True or False 
        value = self.evaluate(node)
        if depth == 0 or node.bot_won or node.opponent_won or node.is_full:
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
        return move
        

    def move(self, grid, player_to_move):

        node = GameNode(grid, None, player_to_move, self.botsign, self.opponentsign)
        return self.pick_move(node)