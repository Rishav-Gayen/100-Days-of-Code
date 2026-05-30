from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(width=100, height=100)


entry = Entry(width=10)
entry.grid(row=1, column=2)

label = Label(text="miles")
label.grid(row=1, column=3)

label_a = Label(text="is equal to")
label_a.grid(row=2, column=1)

label_b = Label(text="0")
label_b.grid(row=2, column=2)

label_c = Label(text="km")
label_c.grid(row=2, column=3)

def miles_to_km():
    miles = int(entry.get())
    km = round(miles * 1.609344)
    label_b.config(text=f"{km}")

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=3, column=2)


window.mainloop()