from tkinter import *
from PIL import ImageTk, Image
import os

class XnOPackage:
    def __init__(self, master):
        self.master = master
        self.field = Frame(self.master)
        self.field.pack()
        self.cur_dir = os.getcwd()
        self.turn_counter = 1
        self.button_list = []
        self.files = []
        self.image_x = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\X.jpg'))
        self.image_o = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\O.jpg'))
        self.image_empty = ImageTk.PhotoImage(Image.open(f'{self.cur_dir}\Empty.jpg'))
        self.widgets()
    
    def widgets(self):
        self.restart_button = Button(self.field, text='Play Again!', command=self.game_restart)
        self.status_bar = Label(self.field, text='Player X Turn...', bd=1, relief=SUNKEN, anchor=W)
        self.restart_button.grid(row=4, columnspan=3, sticky=W + E)
        self.status_bar.grid(row=5, columnspan=3, sticky=W + E)
        self.row_marker = 0
        self.column_marker = 0
        for i in range(9):
            self.files.append(f'Button{str(i + 1)}')
            self.button_list.append(Button(self.field, text=self.files[i], image=self.image_empty,
                                           command=lambda c=i: self.button_click(c)))
            self.button_list[i].grid(row=self.row_marker, column=self.column_marker)
            self.column_marker += 1
            if self.column_marker == 3:
                self.row_marker += 1
                self.column_marker = 0

                
    def button_click(self, button_id):
        if self.turn_counter % 2 == 0:
            self.button_list[button_id].config(image=self.image_o)
            self.button_list[button_id]['text'] = 'o'
            self.status_bar['text'] = 'Player X Turn...'
        else:
            self.button_list[button_id].config(image=self.image_x)
            self.button_list[button_id]['text'] = 'x'
            self.status_bar['text'] = 'Player O Turn...'
        self.button_list[button_id].configure(state=DISABLED)
        self.turn_counter += 1
        self.check_winner()
    
    def check_winner(self):
        if self.button_list[0]['text'] == 'o' and self.button_list[1]['text'] == 'o' and self.button_list[2]['text'] == 'o':
            self.button_list[0]['bg'] = 'green'
            self.button_list[1]['bg'] = 'green'
            self.button_list[2]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[0]['text'] == 'x' and self.button_list[1]['text'] == 'x' and self.button_list[2]['text'] == 'x':
            self.button_list[0]['bg'] = 'green'
            self.button_list[1]['bg'] = 'green'
            self.button_list[2]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[0]['text'] == 'o' and self.button_list[3]['text'] == 'o' and self.button_list[6]['text'] == 'o':
            self.button_list[0]['bg'] = 'green'
            self.button_list[3]['bg'] = 'green'
            self.button_list[6]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[0]['text'] == 'x' and self.button_list[3]['text'] == 'x' and self.button_list[6]['text'] == 'x':
            self.button_list[0]['bg'] = 'green'
            self.button_list[3]['bg'] = 'green'
            self.button_list[6]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[1]['text'] == 'o' and self.button_list[4]['text'] == 'o' and self.button_list[7]['text'] == 'o':
            self.button_list[1]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[7]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[1]['text'] == 'x' and self.button_list[4]['text'] == 'x' and self.button_list[7]['text'] == 'x':
            self.button_list[1]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[7]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[2]['text'] == 'o' and self.button_list[5]['text'] == 'o' and self.button_list[8]['text'] == 'o':
            self.button_list[2]['bg'] = 'green'
            self.button_list[5]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[2]['text'] == 'x' and self.button_list[5]['text'] == 'x' and self.button_list[8]['text'] == 'x':
            self.button_list[2]['bg'] = 'green'
            self.button_list[5]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[3]['text'] == 'o' and self.button_list[4]['text'] == 'o' and self.button_list[5]['text'] == 'o':
            self.button_list[3]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[5]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[3]['text'] == 'x' and self.button_list[4]['text'] == 'x' and self.button_list[5]['text'] == 'x':
            self.button_list[3]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[5]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[6]['text'] == 'o' and self.button_list[7]['text'] == 'o' and self.button_list[8]['text'] == 'o':
            self.button_list[6]['bg'] = 'green'
            self.button_list[7]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[6]['text'] == 'x' and self.button_list[7]['text'] == 'x' and self.button_list[8]['text'] == 'x':
            self.button_list[6]['bg'] = 'green'
            self.button_list[7]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[0]['text'] == 'o' and self.button_list[4]['text'] == 'o' and self.button_list[8]['text'] == 'o':
            self.button_list[0]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[0]['text'] == 'x' and self.button_list[4]['text'] == 'x' and self.button_list[8]['text'] == 'x':
            self.button_list[0]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[8]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.button_list[2]['text'] == 'o' and self.button_list[4]['text'] == 'o' and self.button_list[6]['text'] == 'o':
            self.button_list[2]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[6]['bg'] = 'green'
            self.status_bar['text'] = 'Player O Won!'
            self.game_over()
        elif self.button_list[2]['text'] == 'x' and self.button_list[4]['text'] == 'x' and self.button_list[6]['text'] == 'x':
            self.button_list[2]['bg'] = 'green'
            self.button_list[4]['bg'] = 'green'
            self.button_list[6]['bg'] = 'green'
            self.status_bar['text'] = 'Player X Won!'
            self.game_over()
        elif self.turn_counter > 9:
            self.status_bar['text'] = 'Draw! Try Again?'
    
    def game_over(self):
        for button in self.button_list:
            button.configure(state=DISABLED)
    
    def game_restart(self):
        for button in self.button_list:
            button['state'] = NORMAL
            button['text'] = ''
            button['bg'] = 'white'
            button['image'] = self.image_empty
        self.status_bar['text'] = 'Player X Turn...'
        self.turn_counter = 1


