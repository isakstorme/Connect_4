import random

class RandomBot:

    def move(self, grid, player_to_move): # Not checking if move is valid, it is the job of the class Connect4 to ensure all moves are legal
        c = random.randint(0, 6)

        return c