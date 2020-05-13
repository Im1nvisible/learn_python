from tkinter import *
import pyautogui, win32gui, time

win = Tk()
win.title("Bot RAID")
win.geometry('300x120+770+450')

def run_bot(seconds=0, cycles=0, cvar1=0):
    i = 1
    while i <= cycles:
        raid = win32gui.FindWindow(None, r'Raid: Shadow Legends')
        win32gui.SetForegroundWindow(raid)
        time.sleep(1)
        pyautogui.click(1100, 980)
        time.sleep(1)
        if cvar1 == 1:
            pyautogui.keyDown('altleft')
            pyautogui.press('tab')
            pyautogui.keyUp('altleft')
        time.sleep(seconds)
        i += 1


tl_1 = Label(win, text="Enter the number in seconds", fg='black')
tl_1.config(font=('Canvas', 12))
tl_1.pack()
tl_1.place(x=10, y=0)

edit_1 = Entry(win, width=10, bg='white')
edit_1.pack()
edit_1.place(x=220, y=5)

tl_2 = Label(win, text="Enter the number of cycles", fg='black')
tl_2.config(font=('Canvas', 12))
tl_2.pack()
tl_2.place(x=10, y=30)

edit_2 = Entry(win, width=10, bg='white')
edit_2.pack()
edit_2.place(x=220, y=35)

cvar1 = BooleanVar()
cvar1.set(1)
c1 = Checkbutton(text="AltTab", variable=cvar1, onvalue=1, offvalue=0)
c1.pack(anchor=W)
c1.place(x=120, y=55)

button = Button(win, text='Run')
button.bind('Button-1', lambda event: run_bot(int(edit_1.get()),
                                              int(edit_2.get()),
                                              int(cvar1.get())))
button.pack()
button.place(x=130, y=80)


win.mainloop()
