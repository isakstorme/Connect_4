import pygame
from rules.connect4 import Connect4
from bots.randombot import RandomBot
from bots.alphabetabot import AlphaBetaBot
from botthread import Bot_thread
import threading
from queue import Queue

class Main:

    def __init__(self):
        self.SQUARESIZE = 100
        self.HUMAN_VS_HUMAN = 1
        self.HUMAN_VS_MACHINE = 2
        self.MACHINE_VS_MACHINE = 3
        self.run()

    def loop(self, player1_is_bot = True, player2_is_bot = True, q1_in = None, q1_out = None, q2_in = None, q2_out = None): # Todo divide this function into several functions
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
        
        next_draw = [6, 6, 6, 6, 6, 6, 6]  # Shows newt row to draw for each square printed for each column
        game = Connect4()
        SQUARESIZE = self.SQUARESIZE
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        running = True
        
        has_put = False
        while running:
            player_to_move = game.player_to_move
            if player_to_move == 'y' and player1_is_bot:
                if q1_in.empty() and not has_put:
                    q1_in.put(game.grid)
                    has_put = True
                elif not q1_out.empty():
                    c = q1_out.get()
                    self.move_graphics(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
                    has_put = False
            elif player_to_move == 'r' and player2_is_bot:
                if q2_in.empty() and not has_put:
                    q2_in.put(game.grid)
                    has_put = True
                elif not q2_out.empty():
                    c = q2_out.get()
                    self.move_graphics(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
                    has_put = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if player_to_move == 'y' and not player1_is_bot:
                        x = pygame.mouse.get_pos()[0]
                        c = x // SQUARESIZE
                        self.move_graphics(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
                    elif player_to_move == 'r' and not player2_is_bot:
                        x = pygame.mouse.get_pos()[0]
                        c = x // SQUARESIZE
                        self.move_graphics(screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c)
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

        txt = ""
        if game.game_drawn:
            txt = "game was drawn"
        elif game.yellow_wins:
            txt = "yellow (y) won"
        else:
            txt = "red (r) won"

        print(txt)
        font = pygame.font.Font(None, 64)
        text = font.render(txt, True, (255, 255, 255))
        textRect = pygame.Rect(0, 0, w, h) 
        screen.blit(text, textRect)
        pygame.display.flip()

    def move_graphics(self, screen, next_draw, game, SQUARESIZE, yellow, red, player_to_move, c):
        game.move(c)
        game.display_position()
        new_player_to_move = game.player_to_move
        if new_player_to_move != player_to_move: # If move was valid
            color = red if player_to_move == "r" else yellow
            pygame.draw.circle(screen, color, ((c + 0.5)*SQUARESIZE, ((next_draw[c] + 0.5)*SQUARESIZE)), SQUARESIZE/2)
            next_draw[c] -= 1
            pygame.display.flip()


    def machine_vs_machine(self, q1_in, q1_out, q2_in, q2_out):
        self.loop(True, True, q1_in, q1_out, q2_in, q2_out)
    
    def human_vs_human(self):
        self.loop(False, False)
        
    def human_vs_machine(self, q_in, q_out, start = True):
        if not start:
            self.loop(True, False, q1_in=q_in, q1_out=q_out)
        self.loop(False, True, q2_in=q_in, q2_out=q_out)


    def run(self):  

        mode = 2

        if mode == 1:
            GUI_thread = threading.Thread(target=self.human_vs_human)
            GUI_thread.start()
        elif mode == 2:
            q_in = Queue()
            q_out = Queue()
            GUI_thread = threading.Thread(target=self.human_vs_machine, args=(q_in, q_out, True))
            GUI_thread.start()
            bot1 = AlphaBetaBot('r', 'y', 7)
            bot1_thread = Bot_thread(bot1, 'r', 'y', q_in, q_out)
            bot1_thread.start()
        elif mode == 3:    # When exiting the window in mode 3 it pops up again, fix!
            q_in = Queue()
            q_out = Queue()
            GUI_thread = threading.Thread(target=self.human_vs_machine, args=(q_in, q_out, False))
            GUI_thread.start()
            bot1 = AlphaBetaBot('y', 'r', 7)
            bot1_thread = Bot_thread(bot1, 'y', 'r', q_in, q_out)
            bot1_thread.start()
        elif mode == 4:
            bot1_waiting = True
            bot2_waiting = True  
            q1_in = Queue()  # in signals in for bot_thread
            q1_out = Queue()
            q2_in = Queue() # in signals in for bot_thread
            q2_out = Queue()
            GUI_thread = threading.Thread(target=self.machine_vs_machine, args=(q1_in, q1_out, q2_in, q2_out))
            GUI_thread.start()
            bot1 = AlphaBetaBot('y', 'r', 3)
            bot1_thread = Bot_thread(bot1, 'y', 'r', q1_in, q1_out)
            bot1_thread.start()
            bot2 = AlphaBetaBot('y', 'r', 3)
            bot2_thread = Bot_thread(bot2, 'r', 'y', q2_in, q2_out)
            bot2_thread.start()
            




if __name__ == "__main__":
    Main()