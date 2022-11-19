from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps = 1
    while reps != 0:
        if reps % 2 == 1:
            count_down(60*WORK_MIN)
        elif reps % 2 == 0 and reps < 8:
            count_down(60*SHORT_BREAK_MIN)
        else:
            count_down(60*LONG_BREAK_MIN)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    min = math.floor(count/60)
    sec = count % 60

    #Dynamic types
    # if sec < 10:
    #     sec = f"0{sec}"
    #

    # canvas.itemconfig(text_timer, text=f"{int(count/60):02d}:{(count%60):02d}")
    canvas.itemconfig(text_timer, text=f"{min:02d}:{sec:02d}")

    if count > 0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

img_png = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img_png)
text_timer = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

#Count Down

# count_down(5)

#Label

label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

label_check_marks = Label(text="✅", bg=YELLOW, fg=GREEN)
label_check_marks.grid(column=1, row=3)

#Button

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)


window.mainloop()