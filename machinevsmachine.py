from rules.connect4 import Connect4
from bots.randombot import RandomBot
from bots.minimaxbot import MiniMaxBot
import time

def machine_vs_machine():
    bot1_choice = int(input("if you want machine 1 to be RandomBot type 1: if you want bot 1 to be MiniMaxBot type 2"))

    if bot1_choice == 2:
        bot1_depth = int(input("Write the number ofhalf moves that bot 1 shall be able to calculate maximally"))

    bot2_choice = int(input("if you want bot 2 to be RandomBot type 1: if you want bot 2 to be MiniMaxBot type 2"))

    if bot2_choice == 2:
        bot2_depth = int(input("Write the number ofhalf moves that bot 1 shall be able to calculate maximally"))
    
    bot1sign = "y"
    bot2sign = "r"

    bot1 = MiniMaxBot(human=bot2sign, bot=bot1sign, maxdepth=bot1_depth) if bot1_choice == 2 else RandomBot()
    bot2 = MiniMaxBot(human=bot1sign, bot=bot2sign, maxdepth=bot2_depth) if bot2_choice == 2 else RandomBot()

    game = Connect4()
    player_to_move = "y"
    while not game.game_finished:
        if player_to_move == bot1sign:
            c = bot1.move(game.grid, player_to_move)
            game.move(c)
            game.display_position()
            player_to_move = game.player_to_move
        
        elif player_to_move == bot2sign:
            c = bot2.move(game.grid, player_to_move)
            game.move(c)
            game.display_position()
            player_to_move = game.player_to_move
        time.sleep(1)
    
    if game.game_drawn:
        print("game ended in a draw")
    elif game.yellow_wins:
        print("Yellow (y) wins")
    elif game.red_wins:
        print("Red (r) wins")

if __name__ == "__main__":
    machine_vs_machine()