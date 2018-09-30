import matplotlib.pyplot as plt

#Reference visual.py

class visual():

    def __init__(self, gbsize, win_standard):
        self.gbsize = gbsize
        self.win_standard = win_standard
        self.player1 = 1
        self.player2 = -1

    def prepare_display(self):
        plt.ion()
        fig, axis = plt.subplots(figsize=(self.gbsize, self.gbsize))
        fig.canvas.mpl_connect("close_event", exit)
        axis.set_facecolor("xkcd:puce")
        plt.axis((-1, self.gbsize, -1, self.gbsize))

        for y in range(0, self.gbsize):
            plt.axhline(y=y, color="k", linestyle="-")
            plt.axvline(x=y, color="k", linestyle="-")

        return fig, axis

    def draw_screen(self, player, act, gameover):
        plt.title("Tobigo : Human vs AI")
        if (gameover == False):
            if (player == self.player1):
                plt.plot(act[0], act[1], 'ko', markersize=30)
            else:
                plt.plot(act[0], act[1], 'wo', markersize=30)
        else:
            
            plt.close("all")  
            self.prepare_display()
