import pygame
from rules.connect4 import Connect4
from bots.randombot import RandomBot
from bots.minimaxbot import MiniMaxBot
from bots.alphabetabot import AlphaBetaBot
import time

class Main:

    def __init__(self):
        self.SQUARESIZE = 100
        self.HUMAN_VS_HUMAN = 1
        self.HUMAN_VS_MACHINE = 2
        self.MACHINE_VS_MACHINE = 3
        self.run()

    def loop(self, screen, player1_is_bot = True, player2_is_bot = True, bot1 = AlphaBetaBot('y', 'r', 7), bot2 = AlphaBetaBot('r', 'y', 7)):
        next_draw = [6, 6, 6, 6, 6, 6, 6]  # Shows newt row to draw for each square printed for each column
        game = Connect4()
        SQUARESIZE = self.SQUARESIZE
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        running = True
        while running:
            player_to_move = game.player_to_move
            if player_to_move == 'y' and player1_is_bot:
                c = bot1.move(game.grid, player_to_move)
                self.move(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
            elif player_to_move == 'r' and player2_is_bot:
                c = bot2.move(game.grid, player_to_move)
                self.move(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    c = x // SQUARESIZE
                    self.move(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
            if game.game_drawn or game.yellow_wins or game.red_wins:
                running = False
        
        self.printresult(screen, game)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
    
    def printresult(self, screen, game):
        w = 7 * self.SQUARESIZE
        h = (6+1) * self.SQUARESIZE

        pygame.font.init() # Probably not necessary

        text = ""
        if game.game_drawn:
            text = "game was drawn"
        elif game.yellow_wins:
            text = "yellow (y) won"
        else:
            text = "red (r) won"

        print(text)
        font = pygame.font.Font(None, 64)
        text = font.render('Player', True, (255, 255, 255))
        textRect = pygame.Rect(0, self.SQUARESIZE, w, h) 
        screen.blit(text, textRect)

    def move(self, screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c):
        game.move(c)
        game.display_position()
        new_player_to_move = game.player_to_move
        if new_player_to_move != player_to_move: # If move was valid
            color = red if player_to_move == "r" else yellow
            pygame.draw.circle(screen, color, ((c + 0.5)*SQUARESIZE, ((next_draw[c] + 0.5)*SQUARESIZE)), SQUARESIZE/2)
            next_draw[c] -= 1
            pygame.display.flip()
            time.sleep(0.5)


    def machine_vs_machine(self, screen):
        self.loop(screen, True, True)
    
    def human_vs_human(self, screen):
        self.loop(screen, False, False)
        
    def human_vs_machine(self, screen):
        self.loop(screen, False, True)


    def run(self):  
        pygame.init()

        SQUARESIZE = self.SQUARESIZE

        w = 7 * SQUARESIZE
        h = (6+1) * SQUARESIZE

        size = (w, h)

        screen = pygame.display.set_mode(size=size)
        white = (255, 255, 255)
        blue = (0, 0, 255)
        black = (0, 0, 0)
        # Drawwing background, there probably is an easy way of just drawing background.
        for r in range(6):
            for c in range(7):
                rect = pygame.Rect((c)*SQUARESIZE, (r + 1)*SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(screen, blue, rect)

        # Drawing horizontal lines
        pygame.draw.line(screen, black, start_pos=(0, 1 * SQUARESIZE), end_pos=(w, 1*SQUARESIZE))

        # Drawing vertical lines
        for c in range(6):
            pygame.draw.line(screen, black, start_pos=((c + 1)*SQUARESIZE, 1 * SQUARESIZE), end_pos=((c + 1)*SQUARESIZE, h))

        # Drawing circles, these are centered around a middle point.
        for r in range(6):
            for c in range(7):
                x = (c + 0.5)* SQUARESIZE
                y = (r + 1.5)*SQUARESIZE
                pygame.draw.circle(screen, white, center=(x, y), radius=SQUARESIZE/2)

        # Updating screen
        pygame.display.flip()


        if True:
            self.human_vs_human(screen=screen)



if __name__ == "__main__":
    Main()