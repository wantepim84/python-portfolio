from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time

def countdown():
    try:
        global reset_flag
        reset_flag = False

        target_time = datetime.now().replace(
            hour=int(hour.get()), minute=int(minute.get()), second=int(second.get()))
        current_time = datetime.now()

        if target_time > current_time:
            remaining_time = target_time - current_time
            total_seconds = int(remaining_time.total_seconds())

            while total_seconds > 0 and not reset_flag:
                hours, remainder = divmod(total_seconds, 3600)
                mins, secs = divmod(remainder, 60)
                display = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
                timer_label.config(text=display)
                window.update()
                time.sleep(1)
                total_seconds -= 1

            if not reset_flag:
                timer_label.config(text="Time-Up", font=('bold', 40))

                if check.get():
                    messagebox.showinfo("Notification", "Timer is Off")
        else:
            messagebox.showerror("Error", "Please enter a future time")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid time values")


def reset_timer():
    global reset_flag
    reset_flag = True
    timer_label.config(text="")
    current_time_label.config(text=datetime.now().strftime("%H:%M:%S"))
    reset_flag = False
    hour.set("")
    minute.set("")
    second.set("")


def stop_timer():
    global reset_flag
    reset_flag = True


def update_current_time():
    current_time_label.config(text=datetime.now().strftime("%H:%M:%S"))

    window.after(1000, update_current_time)

window = Tk()
window.geometry('500x500')
window.title('Countdown Timer')

hour = StringVar()
minute = StringVar()
second = StringVar()
check = BooleanVar()
reset_flag = False

head = Label(window, text="Countdown Timer",
             font=('Calibri 15'))
head.grid(row=0, column=2, columnspan=2, pady=20)

Label(window, text="Enter time", font=('bold')).grid(
    row=1, column=2, columnspan=2)

Entry(window, textvariable=hour, width=30).grid(row=2, column=2, columnspan=2)
Entry(window, textvariable=minute, width=30).grid(
    row=3, column=2, columnspan=2)
Entry(window, textvariable=second, width=30).grid(
    row=4, column=2, columnspan=2)

Button(window, text="Set Countdown", command=countdown,
       bg='yellow', font= 20).grid(row=5, column=2, columnspan=1)
Button(window, text="Reset", command=reset_timer,
       bg='red', font=10).grid(row=5, column=3, columnspan=1)
Button(window, text="Stop", command=stop_timer,
       bg='orange', font=10).grid(row=6, column=3, columnspan=1)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

Label(window, text="Current Time:", font=('bold')).grid(row=8, column=1)
current_time_label = Label(window, text=current_time, font=('bold', 20))
current_time_label.grid(row=8, column=2)

Label(window, text="Countdown Timer:", font=('bold')).grid(row=9, column=1)
timer_label = Label(window, text="", font=('bold', 20))
timer_label.grid(row=9, column=2)

window.after(1000, update_current_time)

window.mainloop()
