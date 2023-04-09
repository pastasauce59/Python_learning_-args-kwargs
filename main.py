# from tkinter import *
# ^ this will import everything instead of having to refrence the model each time
import tkinter


def button_clicked():
    #print('I got clicked!')
    # my_label['text'] = 'Button got clicked!'
    my_label['text'] = input.get()


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
# my_label.pack(expand=True)
# my_label.config(text='More New Text')
my_label['text'] = 'New Text'
# my_label.pack()
# my_label.place(x=100, y=200) --> very specific and requires exact coordinates of each widget
my_label.grid(column=0,row=0)
my_label.config(padx=50, pady=50)

#Button
button = tkinter.Button(text= 'Click Me!', command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#New Button
new_button = tkinter.Button(text='New Button')
new_button.grid(column=2,row=0)

#Entry
input = tkinter.Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3,row=2)

window.mainloop()