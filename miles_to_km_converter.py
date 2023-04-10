import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

def calculation():
    miles = float(starting_entry.get())
    km = miles * 1.609344
    conversion_num.config(text=km)

#is_equal Label
is_equal = tkinter.Label(text='is equal to')
is_equal.grid(column=0,row=1)

#starting Entry
starting_entry = tkinter.Entry()
starting_entry.insert(0, string=0)
starting_entry.grid(column=1,row=0)

#conversion number Label
conversion_num = tkinter.Label(text=0)
conversion_num.grid(column=1,row=1)

#calculate Button
calc_button = tkinter.Button(text='Calculate', command=calculation)
calc_button.grid(column=1,row=2)

#Miles Label
miles = tkinter.Label(text='Miles')
miles.grid(column=2,row=0)

#Km Label
km = tkinter.Label(text='Km')
km.grid(column=2,row=1)

window.mainloop()