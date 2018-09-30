import numpy as np
from phan import Phan
from visual import visual

class Omokgame():

    def __init__(self, gbsize, win_standard):
        self.gbsize = gbsize
        self.win_standard = win_standard

    def startphan(self):
        b = Phan(self.gbsize, self.win_standard)
        return np.array(b.board)

    def getboardsize(self):
        return self.gbsize, self.gbsize

    def actionsize(self):
        return self.gbsize * self.gbsize + 1

    def nextstate(self, board, newboard, player, action):
        if action == self.gbsize * self.gbsize:
            return board, -player, newboard

        b = Phan(self.gbsize, self.win_standard)
        b.board = np.copy(board)
        b.board3d = np.copy(newboard)
        move = (int(action / self.gbsize), action % self.gbsize)
        b.moving(move, player)
        b.dim_moving(newboard, board)
        return b.board, -player, b.board3d

    def validmove(self, board, player):

        valids = [0] * self.actionsize()
        b = Phan(self.gbsize, self.win_standard)
        b.board = np.copy(board)
        dun_soo = b.dun_soo()

        if len(dun_soo) == 0:
            valids[-1] = 1
            return np.array(valids)

        for x, y in dun_soo:
            valids[self.gbsize * x + y] = 1

        return np.array(valids)

    def ggeutnam(self, board, player):
        b = Phan(self.gbsize, self.win_standard)
        b.board = np.copy(board)

        if b.iswin(player):
            return 1
        if b.iswin(-player):
            return -1
        if b.ganeung_soo():
            return 0

        return 1e-4

    def oneminusone(self, board, player):
        return player * board

    def symme(self, board, pi):
        assert (len(pi) == self.gbsize ** 2 + 1)
        pi_board = np.reshape(pi[:-1], (self.gbsize, self.gbsize))
        l = []
        for i in range(1, 5):
            for j in [True, False]:
                newb = np.array([np.rot90(board[0], i), np.rot90(board[1], i), np.rot90(board[2], i)])
                newpi = np.rot90(pi_board, i)

                if j:
                    newb = np.fliplr(newb)
                    newpi = np.fliplr(newpi)

                l += [(newb, list(newpi.ravel()) + [pi[-1]])]

        return l

    def stringstring(self, board):
        return board.tostring()

    def dim_board(self):
        b = Phan(self.gbsize, self.win_standard)
        return b.board3d

