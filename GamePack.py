from tkinter import *
from PIL import ImageTk, Image
import os
from XnOComplete import XnOPackage
from RockPaperScizors import RPS
from MemoryGame import Mmrgame
from SimonSays import SimonSays
from Stats import Score, engine
from sqlalchemy.orm import sessionmaker

class Home_window():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.curdir = os.getcwd()
        self.rps_image = ImageTk.PhotoImage(Image.open(f'{self.curdir}\\RPS.png'))
        self.xno_image = ImageTk.PhotoImage(Image.open(f'{self.curdir}\\tic-tac-toe.jpg'))
        self.mmr_image = ImageTk.PhotoImage(Image.open(f'{self.curdir}\\mmrgm.png'))
        self.ss_image = ImageTk.PhotoImage(Image.open(f'{self.curdir}\\Simonsays.png'))
        self.header = Label(self.frame, text='Choose A Game')
        self.xno = Button(self.frame, text='Tick Tack Toe', image=self.xno_image)
        self.rps = Button(self.frame, text='Rock Paper Scissors', image=self.rps_image)
        self.mmr = Button(self.frame, text='Memory Game', image=self.mmr_image)
        self.ss = Button(self.frame, text='Simon Says', image=self.ss_image)
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.sub_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Menu', menu=self.sub_menu)
        self.sub_menu.add_command(label='Statistics', command=self.stats_window)
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label='Exit', command=self.close_game)
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

    def stats_window(self):
        self.statswindow = Toplevel(self.master)
        self.statswindow2 = Stats(self.statswindow)

    def close_game(self):
        self.master.destroy()

class Stats:
    def __init__(self, master):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        self.stats = self.session.query(Score).all()
        self.master = master
        self.frame = Frame(self.master)
        self.listbox = Listbox(self.frame, width=50)
        self.exitButton = Button(self.frame, text='Main Menu', command=self.close_stats)
        self.stat_list()
        self.frame.pack()
        self.listbox.grid(row=0, column=0)
        self.exitButton.grid(row=1, column=0)

    def stat_list(self):
        n = 1
        for x in self.stats:
            self.listbox.insert(n, x)
            n += 1

    def close_stats(self):
        self.master.destroy()


#functions
def main():
    field = Tk()
    app = Home_window(field)
    field.iconbitmap('gamepack.ico')
    field.title('Game Pack')
    field.mainloop()

main()