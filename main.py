from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00ff00"
YELLOW = "#fcffa4"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timing = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timing)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=("Constantia", 28, "bold"))
    tick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    shortbreak_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(longbreak_sec)
        timer.config(text="Break", fg=RED)
        winsound.Beep(1000, 500)
    elif reps % 2 == 0:
        countdown(shortbreak_sec)
        timer.config(text="Break", fg=PINK)
        winsound.Beep(1000, 500)
    else:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)
        winsound.Beep(800, 500)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timing
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timing = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_mark.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="./tomato.png")
canvas.create_image(110, 110, image=picture)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=("Constantia", "24", "bold"))
canvas.grid(row=2, column=2)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Constantia", 28, "bold"))
timer.grid(row=0, column=2)

tick_mark = Label(fg=GREEN, bg=YELLOW, font=("Constantia", 30, "bold"))
tick_mark.grid(row=4, column=2)

start = Button(text="Start", command=start_timer, bg="White", font=("Constantia", 16, "bold"))
start.grid(row=4, column=0)

reset = Button(text="Reset", bg="White", font=("Constantia", 16, "bold"), command=reset_timer)
reset.grid(row=4, column=3)

window.mainloop()
