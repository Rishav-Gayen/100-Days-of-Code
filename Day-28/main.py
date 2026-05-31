from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer

    window.after_cancel(timer)
    reps = 0
    timer = None
    canvas.itemconfig(time_text, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_text.config(text="Break", fg=GREEN)
        count_down(long_break_sec)
    elif reps % 2 != 0:
        timer_text.config(text="Work", fg=RED)
        count_down(work_sec)
    else:
        timer_text.config(text="Break", fg=GREEN)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
        global reps

        minutes = math.floor(count / 60)
        seconds = count % 60

        if seconds < 10:
            seconds = f"0{seconds}"
        elif seconds == 0:
            seconds = "00:00"

        if count >= 0:
            global timer
            canvas.itemconfig(time_text, text = f"{minutes}:{seconds}")
            timer = window.after(1000, count_down, count - 1)
        else:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


# window.after(1000, say_something, "Hello")

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

time_text = canvas.create_text(100, 120, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()