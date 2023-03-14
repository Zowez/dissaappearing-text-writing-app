from tkinter import Tk, Text, Label, END


COLOURS = ["#ffc9b7", "#ffae95", "#ff9273", "#ff7453", "#FF0000"]

timer = 0
has_written = False


def time():
    global has_written

    if has_written:
        global timer

        timer += 1

        timer_label.config(text=timer)
        window.config(background=COLOURS[timer-1])
        text_label.config(background=COLOURS[timer-1])
        timer_label.config(background=COLOURS[timer-1])

        if timer >= 5:
            delete_text()
            has_written = False

        window.after(1000, time)

def reset_timer():
    global timer
    timer = 0


def check_flag(event=None):
    global has_written

    if has_written:
        reset_timer()
    else:
        has_written = True
        text_window.config(highlightbackground="white", highlightcolor="white")
        time()


def delete_text():
    words = text_window.get("1.0", "end-1c")
    wordcount = len(words.split(" "))
    charcount = len(words)
    print(words)

    timer_label.config(text=f"Your timer has ended. You've written {wordcount} words and typed {charcount} character.")
    text_window.delete("1.0", END)

    reset_timer()


window = Tk()

window.title("Disappearing Text Writing App")
window.geometry("1440x900")
window.config(background="#ffe4db")

text_window = Text(window, height=20, width=70, font=("Bradley Hand ITC", 20))
text_label = Label(window, text="If you stop typing, your writing will be lost.", background="#ffe4db")
timer_label = Label(window, font=("Agency FB", 20, "bold"), background="#ffe4db")

text_window.bind("<Key>", check_flag)
text_label.config(font=("Agency FB", 20, "bold"))

text_label.pack()
text_window.pack()
timer_label.pack()

window.mainloop()
