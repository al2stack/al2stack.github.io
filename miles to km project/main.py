from tkinter import *
window=Tk()
window.title("Miles to km convertor")

def convert():
   rqdmiles= float(km.get())
   rqdmiles *=1.6
   conversion.config(text=f"{round(rqdmiles)}")

km=Entry()
km.grid(column=1,row=0)

miles=Label(text="Miles")
miles.grid(column=2,row=0)

equal=Label(text="Is equal to")
equal.grid(column=0,row=1)

conversion=Label(text="0")
conversion.grid(column=1,row=1)

km_label=Label(text="km")
km_label.grid(column=2,row=1)

convertor=Button(text="Calculate",command=convert)
convertor.grid(column=1,row=2)

window.mainloop()