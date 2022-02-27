from tkinter import *
from PIL import ImageTk, Image
import os
from XnOComplete import XnOPackage
from RockPaperScizors import RPS
from MemoryGame import Mmrgame
from SimonSays import SimonSays


class Home_window():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.curdir = os.getcwd()
        self.header = Label(self.frame, text='Choose A Game')
        self.xno = Button(self.frame, text='Tick Tack Toe')
        self.rps = Button(self.frame, text='Rock Paper Scissors')
        self.mmr = Button(self.frame, text='Memory Game')
        self.ss = Button(self.frame, text='Simon Says')
        self.frame.grid(row=0, column=0)
        self.header.grid(row=0, columnspan=4)
        self.xno.grid(row=1, column=0)
        self.rps.grid(row=1, column=1)
        self.mmr.grid(row=1, column=2)
        self.ss.grid(row=1, column=3)
        self.xno.config(command=self.tick_tack_toe)
        self.rps.config(command=self.rock_paper_scizorrs)
        self.mmr.config(command=self.memory_game)
        self.ss.config(command=self.simon_says)

    def tick_tack_toe(self):
        self.tictacktoe = Toplevel(self.master)
        self.tictacktoe2 = XnOPackage(self.tictacktoe)

    def rock_paper_scizorrs(self):
        self.rockpaperscizors = Toplevel(self.master)
        self.rockpaperscizors2 = RPS(self.rockpaperscizors)

    def memory_game(self):
        self.memorygame = Toplevel(self.master)
        self.memorygame2 = Mmrgame(self.memorygame)

    def simon_says(self):
        self.simonsays = Toplevel(self.master)
        self.simonsays2 = SimonSays(self.simonsays)

#functions
def main():
    field = Tk()
    app = Home_window(field)
    field.iconbitmap('gamepack.ico')
    field.title('Game Pack')
    field.mainloop()
#widgets

#grid

#config
#launch
main()