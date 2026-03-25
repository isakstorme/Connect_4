from .gamenode import GameNode
from .import eval
import time
class Stormefish:   # This bot uses minimax with Alpha Beta pruning
    def __init__(self, botsign, opponentsign, maxdepth, evaluate=eval.evaluate):
        self.botsign = botsign
        self.opponentsign = opponentsign
        self.maxdepth = max(maxdepth, 1)
        self.INF = 1000000
        self.WIN = 1000
        self.LOSS = -1000
        self.evaluate = evaluate
        self.transposition_table = dict() # In chess hashed maps are typically used it seems.
    

    def alpha_beta(self, node, depth, alpha, beta, max_mode):  # max_mode = True or False 
        value = self.evaluate(node)
        if depth == 0 or node.bot_won or node.opponent_won or node.is_full:
            return value, None
        hash = node.hash()
        if hash in self.transposition_table:
            return self.transposition_table[hash]
        
        
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
        self.transposition_table[node.hash()] = value, bestmove
        return value, bestmove
        

    def move(self, grid, player_to_move):
        node = GameNode(grid, None, player_to_move, self.botsign, self.opponentsign)
        t0 = time.time()
        move = self.alpha_beta(node=node, depth=self.maxdepth, alpha=-self.INF, beta=self.INF, max_mode=True)[1]
        t1 = time.time()
        print("time for computing move= ", t1 - t0, " seconds")
        return move