from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
time = NONE
# ---------------------------- TIMER PAUSE ------------------------------- # 

    
# ---------------------------- TIMER RESET ------------------------------- # 
def reser_timer():
    global reps
    window.after_cancel(time)
    timer.config(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 3
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if(reps % 8 == 0):
        count_down(long_break_sec)
        timer.config(text="Long Break",font=(FONT_NAME,25,"bold"),fg=PINK,bg=YELLOW)
        reps += 1
    elif(reps % 2 == 0):
        count_down(short_break_sec)
        timer.config(text="Short Break",font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
        reps += 1
    else:
        count_down(work_sec)
        timer.config(text="Study Time",font=(FONT_NAME,25,"bold"),fg=RED,bg=YELLOW)
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global time
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
        time = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text = canvas.create_text(104,135,text="00:00", fill="white",font=(FONT_NAME, 30,"bold"))
canvas.grid(row=1,column=1)

timer = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(row=0,column=1)

start = Button(text="Start",command=start_timer,highlightthickness=0)
start.grid(row=2,column=0)

#pause = Button(text="Pause",command=pause_timer,highlightthickness=0)
#pause.grid(row=2,column=1)

reset = Button(text="Reset",command=reser_timer,highlightthickness=0)
reset.grid(row=2,column=2)

check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))
check_mark.grid(row=3,column=1)

window.mainloop()
