# from tkinter import *
# ^ this will import everything instead of having to refrence the model each time
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
# my_label.pack(expand=True)
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='More New Text')


#Button
def button_clicked():
    #print('I got clicked!')
    # my_label['text'] = 'Button got clicked!'
    my_label['text'] = input.get()


button = tkinter.Button(text= 'Click Me!', command=button_clicked)
button.pack()


#Entry
input = tkinter.Entry(width=10)
input.pack()
input.get()


window.mainloop()