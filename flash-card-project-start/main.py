BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
current_card={}
to_learn={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)

    canvas.itemconfigure(language, text="French",fill="black")
    canvas.itemconfigure(word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfigure(word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)
def is_known():
    global list,current_card
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
#.....................UI Setup.........................
window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="./images/card_front.png")
card_background=canvas.create_image(410,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
card_back=PhotoImage(file='images/card_back.png')
try:
    data=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

language=canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word=canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

right=PhotoImage(file="./images/right.png")
right_btn=Button(image=right,highlightthickness=0,command=is_known)
right_btn.grid(column=1,row=1)

wrong=PhotoImage(file="./images/wrong.png")
wrong_btn=Button(image=wrong,highlightthickness=0,command=next_card)
wrong_btn.grid(row=1,column=0)

back_card=PhotoImage(file="./images/card_back.png")
#..........................Creating Flash Cards.....................................
next_card()



window.mainloop()
