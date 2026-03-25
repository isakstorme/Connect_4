import threading
from queue import Queue
import time

class Bot_thread(threading.Thread):
    def __init__(self, bot, botsign, opponentsign, q_in, q_out):
        super(Bot_thread, self).__init__()
        self.bot = bot
        self.botsign = botsign
        self.opponentsign = opponentsign
        self.q_in = q_in
        self.q_out = q_out
        self.daemon = True

    def run(self):
        while True:
            grid = self.q_in.get()
            t0 = time.time()
            move = self.bot.move(grid, self.botsign)
            t1 = time.time()
            print(t1 - t0)
            self.q_out.put(move)
