import keyboard
import win32api

import time
import datetime
import threading

from lib.colorz import Colors
from lib.config import Config


from tkinter import *





# Important var
toggle_program_key = "TO DO"
isON = False
time_between_clicks = 0.5






def get_click_speed():
    try:
        return float(speedDial.get())
    except:
        return time_between_clicks

def click_loop():
    global isON
    while isON:

        # Terminal Debug
        terminal.config(state=NORMAL)      # unlock
        terminal.insert(END,f'{get_click_speed()} cpm \n')  
        terminal.config(state=DISABLED)    # lock again

        
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(2, x, y, 0, 0)  # MOUSEEVENTF_LEFTDOWN
        win32api.mouse_event(4, x, y, 0, 0)  # MOUSEEVENTF_LEFTUP
        time.sleep(get_click_speed())

def autokliker_on():
    global isON
    if not isON:  # Zabezpieczenie przed uruchomieniem wielu wątków na raz
        isON = True


        button_on.config(state=DISABLED)
        button_off.config(state=ACTIVE)


        # Uruchomienie pętli klikającej w innym wątku
        threading.Thread(target=click_loop, daemon=True).start()

        # Terminal message
        terminal.config(state=NORMAL)      # unlock
        terminal.insert(END,f'{datetime.datetime.now()} Auto clicker is On \n')  
        terminal.config(state=DISABLED)    # lock again

def autokliker_off():
    global isON
    isON = False

    #temp
    button_off.config(text='XD')

    button_on.config(state=ACTIVE)
    button_off.config(state=DISABLED)


    # Terminal message
    terminal.config(state=NORMAL)      # unlock
    terminal.insert(END,f'{datetime.datetime.now()} Auto clicker is Off \n')  
    terminal.config(state=DISABLED)    # lock again


window = Tk()

window.geometry(Config.windowSize)
window.config(background=Colors.app_bg)
window.title('xxxxdddd')

button_on = Button(window,
              text="start",
              font=(Config.button_fontFamily, Config.button_fontSize), 
              bg=Colors.button_bg,
              fg=Colors.button_fg,
              activebackground='red',
              activeforeground=Colors.active_button_fg,
              command=autokliker_on,
              width=Config.buttonWidth)

button_off = Button(window,
              text="off",
              font=(Config.button_fontFamily, Config.button_fontSize), 
              bg=Colors.button_bg,
              fg=Colors.button_fg,
              activebackground=Colors.active_button_bg,
              activeforeground=Colors.active_button_fg,
              command=autokliker_off,
              width=Config.buttonWidth,
              state=DISABLED)

temp_button = Button(window,
              text="temp",
              font=(Config.button_fontFamily, Config.button_fontSize), 
              bg=Colors.button_bg,
              fg=Colors.button_fg,
              activebackground=Colors.active_button_bg,
              activeforeground=Colors.active_button_fg,
              width=Config.buttonWidth)

temp2_button = Button(window,
              text="temp",
              font=(Config.button_fontFamily, Config.button_fontSize), 
              bg=Colors.button_bg,
              fg=Colors.button_fg,
              activebackground=Colors.active_button_bg,
              activeforeground=Colors.active_button_fg,
              width=Config.buttonWidth)

terminal = Text(window,
                 state=DISABLED,
                 bg="#141229",
                 fg='#FFFFFF')

speedDial = Entry(window,
                  bg="#291257")


button_off.grid(row=5, column=3, sticky="ew")
temp_button.grid(row=4, column=2, sticky="ew")

button_on.grid(row=4, column=3, sticky="ew")
temp2_button.grid(row=5, column=2, sticky="ew")

speedDial.grid(row=0, column=0, sticky="ew")
terminal.grid(row=9, column=0, columnspan=4, sticky="ew")

# Pozwól kolumnom rozciągać się razem z oknem
for col in range(4):
    window.columnconfigure(col, weight=1)

window.mainloop()

