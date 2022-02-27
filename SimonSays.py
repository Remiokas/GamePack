from tkinter import *
from PIL import ImageTk, Image
import random
import os
from winsound import *

class SimonSays:
    def __init__(self, master):
        self.master = master
        self.field = Frame(self.master)
        self.field.pack()
        self.cur_dir = os.getcwd()
        self.choices = [0, 1, 2, 3]
        self.sequence_list = []
        self.player_move_list = []
        self.image_green = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\\green.jpg'))
        self.image_blue = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\\blue.jpg'))
        self.image_yellow = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\\yellow.jpg'))
        self.image_red = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\\red.jpg'))
        self.image_list = [self.image_green, self.image_blue, self.image_yellow, self.image_red]
        self.image_empty = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\\Empty.jpg'))
        self.widgets()
        self.button_lock()

    def game_restart(self):
        self.player_move_list.clear()
        self.sequence_list.clear()
        self.start_game_button['text'] = 'Start The Game'
        self.start_game_button.config(command=self.simon_picks)
        self.your_buttons['text'] = 'Click The Corresponding Buttons'
    
    def simon_picks(self):
        sequence = random.choice(self.choices)
        self.sequence_list.append(sequence)
        self.simon_highlight()
        self.start_game_button.configure(state=DISABLED)
    
    def simon_highlight(self):
        y = 1
        for x in self.sequence_list:
            self.field.after(500 * y, self.color_change, x)
            self.field.after(400 + 500 * y, self.color_change_back, x)
            y += 1
        self.button_enable()
    
    def color_change(self, x):
        self.label_list[x]['image'] = self.image_list[x]
        self.label_list[x]['bg'] = 'black'
        if x == 0:
            Beep(600, 100)
        elif x == 1:
            Beep(800, 100)
        elif x == 2:
            Beep(1000, 100)
        elif x == 3:
            Beep(1200, 100)
    
    def color_change_back(self, x):
        self.label_list[x]['image'] = self.image_empty
        self.label_list[x]['bg'] = 'white'
    
    def click_check(self):
        if len(self.sequence_list) == len(self.player_move_list):
            self.button_lock()
            if self.sequence_list == self.player_move_list:
                self.field.after(500, self.simon_picks)
                self.player_move_list.clear()
            else:
                self.game_over()
        else:
            try:
                for x in range(len(self.sequence_list)):
                    if self.sequence_list[x] != self.player_move_list[x]:
                        self.game_over()
            except IndexError:
                pass
    
    def game_over(self):
        self.button_lock()
        self.start_game_button.configure(state=NORMAL)
        self.your_buttons['text'] = f'Game Over! Your Streak Was: {len(self.sequence_list) - 1}'
        self.start_game_button['text'] = 'Play Again?!'
        self.start_game_button.config(command=self.game_restart)
    
    def green_click(self):
        self.player_move_list.append(0)
        self.click_check()
        Beep(600, 100)
    
    def blue_click(self):
        self.player_move_list.append(1)
        self.click_check()
        Beep(800, 100)
    
    def yellow_click(self):
        self.player_move_list.append(2)
        self.click_check()
        Beep(1000, 100)
    
    def red_click(self):
        self.player_move_list.append(3)
        self.click_check()
        Beep(1200, 100)
    
    def button_enable(self):
        self.green_button.configure(state=NORMAL)
        self.blue_button.configure(state=NORMAL)
        self.yellow_button.configure(state=NORMAL)
        self.red_button.configure(state=NORMAL)
    
    def button_lock(self):
        self.green_button.configure(state=DISABLED)
        self.blue_button.configure(state=DISABLED)
        self.yellow_button.configure(state=DISABLED)
        self.red_button.configure(state=DISABLED)

    def widgets(self):
        self.green_label = Label(self.field, image=self.image_empty, bg='white')
        self.blue_label = Label(self.field, image=self.image_empty, bg='white')
        self.yellow_label = Label(self.field, image=self.image_empty, bg='white')
        self.red_label = Label(self.field, image=self.image_empty, bg='white')
        self.label_list = [self.green_label, self.blue_label, self.yellow_label, self.red_label]
        self.green_button = Button(self.field, image=self.image_green, command=self.green_click)
        self.blue_button = Button(self.field, image=self.image_blue, command=self.blue_click)
        self.yellow_button = Button(self.field, image=self.image_yellow, command=self.yellow_click)
        self.red_button = Button(self.field, image=self.image_red, command=self.red_click)
        self.button_list = [self.green_button, self.blue_button, self.yellow_button, self.red_button]
        self.your_buttons = Label(self.field, text='Click The Corresponding Buttons')
        self.start_game_button = Button(self.field, text='Start The Game', command=self.simon_picks)
        self.green_label.grid(row=0, column=0)
        self.blue_label.grid(row=0, column=1)
        self.yellow_label.grid(row=0, column=2)
        self.red_label.grid(row=0, column=3)
        self.your_buttons.grid(row=1, columnspan=4)
        self.green_button.grid(row=2, column=0)
        self.blue_button.grid(row=2, column=1)
        self.yellow_button.grid(row=2, column=2)
        self.red_button.grid(row=2, column=3)
        self.start_game_button.grid(row=3, columnspan=4, sticky=W + E)

