from tkinter import *
from PIL import ImageTk, Image
import random
import os
from Stats import Score, engine
from sqlalchemy.orm import sessionmaker
import datetime

class RPS:
    def __init__(self, master):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        self.master = master
        self.field = Frame(self.master)
        self.field.pack()
        self.cur_dir = os.getcwd()
        self.time = datetime.date.today()
        self.player_win_index = 0
        self.computer_win_index = 0
        self.var = None
        self.image_rock = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\Rock.jpg'))
        self.image_paper = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\Paper.jpg'))
        self.image_scissors = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\Scissors.jpg'))
        self.img_list = [self.image_rock, self.image_paper, self.image_scissors]
        self.computer_label = Label(self.field, text='Computers Choice', justify=CENTER)
        self.player_label = Label(self.field, text='Your Choice', justify=CENTER)
        self.select_random = Label(self.field)
        self.rock_button = Button(self.field, image=self.image_rock, command=self.pick_rock)
        self.paper_button = Button(self.field, image=self.image_paper, command=self.pick_paper)
        self.scissor_button = Button(self.field, image=self.image_scissors, command=self.pick_scissors)
        self.status_bar = Label(self.field, text='Make Your Pick', bd=1, relief=SUNKEN, anchor=W)
        self.restart_button = Button(self.field, text='Play Again!', command=self.game_restart)
        self.computer_label.grid(row=0, columnspan=5)
        self.select_random.grid(row=1, column=2)
        self.player_label.grid(row=2, columnspan=5)
        self.rock_button.grid(row=3, column=0)
        self.paper_button.grid(row=3, column=2)
        self.scissor_button.grid(row=3, column=4)
        self.restart_button.grid(row=4, columnspan=5, sticky=W + E)
        self.status_bar.grid(row=5, columnspan=5, sticky=W + E)
        self.field.after(0, self.play_choices)

    def play_choices(self):
        self.rand = random.choice(self.img_list)
        self.select_random.config(image=self.rand)
        self.var = self.field.after(50, self.play_choices)
        self.restart_button.configure(state=DISABLED)

    def unbind(self):
        self.rock_button.unbind('<Button-1>')
        self.paper_button.unbind('<Button-1>')
        self.scissor_button.unbind('<Button-1>')

    def computer_pick(self):
        self.computer_selection = random.choice(self.img_list)
        self.select_random.config(image=self.computer_selection)
        if self.computer_selection == self.image_rock:
            self.computer_win_index = 1
        elif self.computer_selection == self.image_paper:
            self.computer_win_index = 2
        elif self.computer_selection == self.image_scissors:
            self.computer_win_index = 3

    def pick_rock(self):
        self.rock_button['bg'] = 'green'
        self.player_win_index = 1
        self.paper_button.configure(state=DISABLED)
        self.scissor_button.configure(state=DISABLED)
        self.field.after_cancel(self.var)
        self.computer_pick()
        self.check_winner()

    def pick_paper(self):
        self.paper_button['bg'] = 'green'
        self.player_win_index = 2
        self.rock_button.configure(state=DISABLED)
        self.scissor_button.configure(state=DISABLED)
        self.field.after_cancel(self.var)
        self.computer_pick()
        self.check_winner()

    def pick_scissors(self):
        self.scissor_button['bg'] = 'green'
        self.player_win_index = 3
        self.rock_button.configure(state=DISABLED)
        self.paper_button.configure(state=DISABLED)
        self.field.after_cancel(self.var)
        self.computer_pick()
        self.check_winner()

    def check_winner(self):
        if self.player_win_index == self.computer_win_index:
            self.status_bar['text'] = 'Tie! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Tie')
        elif self.player_win_index == 1 and self.computer_win_index == 3:
            self.status_bar['text'] = 'You Won! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Victory')
        elif self.player_win_index == 1 and self.computer_win_index == 2:
            self.status_bar['text'] = 'You Lose! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Loss')
        elif self.player_win_index == 2 and self.computer_win_index == 1:
            self.status_bar['text'] = 'You Won! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Victory')
        elif self.player_win_index == 2 and self.computer_win_index == 3:
            self.status_bar['text'] = 'You Lose! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Loss')
        elif self.player_win_index == 3 and self.computer_win_index == 2:
            self.status_bar['text'] = 'You Won! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Victory')
        elif self.player_win_index == 3 and self.computer_win_index == 1:
            self.status_bar['text'] = 'You Lose! Play Again?'
            self.stats = Score('Rock Paper Scissors', self.time, 'Loss')
        self.restart_button.configure(state=NORMAL)
        self.session.add(self.stats)
        self.session.commit()

    def game_restart(self):
        self.play_choices()
        self.rock_button.configure(state=NORMAL)
        self.paper_button.configure(state=NORMAL)
        self.scissor_button.configure(state=NORMAL)
        self.rock_button['bg'] = 'white'
        self.paper_button['bg'] = 'white'
        self.scissor_button['bg'] = 'white'
        self.status_bar['text'] = 'Make Your Pick'
