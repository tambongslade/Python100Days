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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_txt.config(text="Timer")
    txt.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global  reps,timer_text
    reps+=1
    work_sec= WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    Count_down(work_sec)
    if reps % 8 ==0:
        Count_down(long_break)
        timer_txt.config(text="break", fg=RED)
    elif reps % 2 == 0:
        Count_down(short_break)
        timer_txt.config(text="break", fg=PINK)
    else:
        Count_down(work_sec)
        timer_txt.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def Count_down(count):
    global reps
    count_min= math.floor(count/60)
    count_sec= count % 60
    if count > 0:
        global timer
        timer=window.after(1000,Count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            mark +="✓"
        txt.config(text=mark)
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Concerntrate")
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=photo)
timer_text = canvas.create_text(120,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
timer_txt = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25))
timer_txt.grid(row=0,column=1)

start_button=Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

txt=Label(text="",bg=YELLOW)
txt.grid(row=2,column=1)

stop_button=Button(text="Reset",command=reset_timer)
stop_button.grid(row=2,column=2)





window.mainloop()