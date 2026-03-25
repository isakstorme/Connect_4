from . import connect4helper

class MiniMaxBot:   # Bot is max player, human is min player
    def __init__(self, bot, opponent, maxdepth):
        self.bot = bot
        self.opponent = opponent
        self.maxdepth = max(maxdepth, 1)

    class GameNode:
        def __init__(self, grid, move, player_to_move, bot, human):
            self.grid = grid
            self.move = move
            self.player_to_move = player_to_move
            self.children = []
            self.bot = bot
            self.opponent = human
            self.value = self.evaluate()
        
        def evaluate(self):
            if connect4helper.is_winning(self.grid, self.bot):
                return 100
            elif connect4helper.is_winning(self.grid, self.opponent):
                return -100
            else:
                return 0
        
        def add_child(self, node):
            self.children.append(node)

    def build_tree(self, node, steps):  # This implementation is probably not most typical. Building the tree is typically done in the mini_max function as i understand it, as in AlphaBetaBot
        if steps == 0 or node.value != 0:
            return
        next_player_to_move = "y" if node.player_to_move == "r" else "r"
        
        for move in connect4helper.valid_moves(node.grid):
            new_grid = connect4helper.copy_and_move(node.grid, move, node.player_to_move)
            new_node = MiniMaxBot.GameNode(new_grid, move, next_player_to_move, self.bot, self.opponent)
            node.children.append(new_node)
            self.build_tree(new_node, steps - 1)



    def mini_max(self, node, max_mode):  # max_mode = True or False 
        if len(node.children) == 0:
            return node.value
        else:
            children_values = []
            if max_mode:
                for child in node.children:
                    children_values.append(self.mini_max(child, False))
                    node.value = max(children_values)
            else:
                for child in node.children:
                    children_values.append(self.mini_max(child, True))
                    node.value = min(children_values)
            return node.value
    
    def pick_move(self, node):
        best_node = max(node.children, key=lambda c: c.value)
        return best_node.move
        

    def move(self, grid, player_to_move):

        node = MiniMaxBot.GameNode(grid, None, player_to_move, self.bot, self.opponent)
        self.build_tree(node, self.maxdepth)
        self.mini_max(node, max_mode=True)
        return self.pick_move(node)