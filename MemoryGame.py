from tkinter import *
from PIL import ImageTk, Image
import random
import os
from winsound import *
from Stats import Score, engine
from sqlalchemy.orm import sessionmaker
import datetime

class Mmrgame:
    def __init__(self, master):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        self.time = datetime.date.today()
        self.master = master
        self.field = Frame(self.master)
        self.field.pack()
        self.cur_dir = os.getcwd()
        self.button_list = []
        self.files = []
        self.turn_counter = 0
        self.row_marker = 0
        self.column_marker = 0
        self.cards_revealed = 0
        self.first_card_id = 0
        self.second_card_id = 0
        self.image_empty = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Empty.png'))
        self.image1 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image1.png'))
        self.image2 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image2.png'))
        self.image3 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image3.png'))
        self.image4 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image4.png'))
        self.image5 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image5.png'))
        self.image6 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image6.png'))
        self.image7 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image7.png'))
        self.image8 = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}/Image8.png'))
        self.image_list = [self.image1, self.image2, self.image3, self.image4,
                           self.image5, self.image6, self.image7, self.image8,
                           self.image1, self.image2, self.image3, self.image4,
                           self.image5, self.image6, self.image7, self.image8]
        self.widgets()
        self.game_start()

    def game_start(self):
        self.turn_counter = 0
        random.shuffle(self.image_list)

    def button_click(self, button_id):
        self.turn_counter += 1
        self.button_list[button_id].config(image=self.image_list[button_id])
        self.cards_revealed += 1
        if self.cards_revealed == 1:
            self.first_card_id = button_id
        if self.cards_revealed == 2:
            self.second_card_id = button_id
            for x in range(16):
                self.button_list[x].config(command=NONE)
            self.field.after(1000, self.two_flipped)
            self.cards_revealed = 0

    def two_flipped(self):
        self.match_pictures()
        for x in range(16):
            self.button_list[x].config(command=lambda c=x: self.button_click(c))

    def match_pictures(self):
        if self.button_list[self.first_card_id]['image'] == self.button_list[self.second_card_id]['image']:
            self.button_list[self.first_card_id].configure(state=DISABLED)
            self.button_list[self.second_card_id].configure(state=DISABLED)
            Beep(600, 100)
            Beep(1000, 100)
        else:
            self.button_list[self.first_card_id].config(image=self.image_empty)
            self.button_list[self.second_card_id].config(image=self.image_empty)
            Beep(60, 500)

    def game_restart(self):
        self.stats = Score('Memory Game', self.time, f'Game Ended in {self.turn_counter} Turns')
        self.session.add(self.stats)
        self.session.commit()
        for x in range(16):
            self.button_list[x]['image'] = self.image_empty
            self.button_list[x].configure(state=NORMAL)
        self.game_start()

    def widgets(self):
        for i in range(16):
            self.files.append(f'Button{str(i+1)}')
        for i in range(len(self.files)):
            self.button_list.append(Button(self.field, text=self.files[i], image=self.image_empty,
                                           command=lambda c=i: self.button_click(c)))
            self.button_list[i].grid(row=self.row_marker, column=self.column_marker)
            self.column_marker += 1
            if self.column_marker == 4:
                self.row_marker += 1
                self.column_marker = 0
        self.restart_button = Button(self.field, text='Play Again!', command=self.game_restart)
        self.restart_button.grid(row=4, columnspan=4, sticky=W + E)
