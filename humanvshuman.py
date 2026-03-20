from rules.connect4 import Connect4

def human_game():
    game = Connect4()
    while not game.game_finished:
        c = int(input("c: "))
        game.move(c)
        game.display_position()
    
    print(game.red_wins)
    if game.game_drawn:
        print("game ended in a draw")
    elif game.yellow_wins:
        print("player yellow (y) wins")
    elif game.red_wins:
        print("player red (r) wins")



if __name__ == "__main__":
    human_game()