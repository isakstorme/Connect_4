from rules.connect4 import Connect4
from bots.randombot import RandomBot
from bots.minimaxbot import MiniMaxBot
from bots.alphabetabot import AlphaBetaBot

def human_vs_machine():
    player_choice = (input("if you want to start, type y, else type r"))
    human = "y"
    botsign = "r"
    if player_choice == "r":
        human = "r"
        botsign = "y"
    
    bot_choice = int(input("if you want to play against randomBot, type 1\nif you want to play against MiniMaxBot type 2\nif you want to play against AlphaBetaBot type 3"))

    bot = RandomBot()
    if bot_choice == 2:
        bot = MiniMaxBot(opponent=human, bot=botsign, maxdepth=4)
    elif bot_choice == 3:
        bot = AlphaBetaBot(opponentsign=human, botsign=botsign, maxdepth=8)
    game = Connect4()
    player_to_move = "y"
    while not game.game_finished:
        if player_to_move == human:
            c = int(input("c: "))
            game.move(c)
            game.display_position()
            player_to_move = game.player_to_move
        
        elif player_to_move == botsign:
            c = bot.move(game.grid, player_to_move)
            game.move(c)
            game.display_position()
            player_to_move = game.player_to_move
    
    if game.game_drawn:
        print("game ended in a draw")
    elif game.yellow_wins:
        print("Yellow (y) wins")
    elif game.red_wins:
        print("Red (r) wins")

if __name__ == "__main__":
    human_vs_machine()