import sys
import time
import keyboard
import pygetwindow as gw
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk
import os

# def resource_path(relative_path):
#     try:
#         # PyInstaller створює тимчасову папку _MEIPASS при запуску .exe
#         base_path = sys._MEIPASS
#     except AttributeError:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

def waiting_of_start():
    print("Waiting for the game to start...")
    while True:

        #OLD METOD

        # try:
        #     button_location_eng = pyautogui.locateOnScreen('img/buttom_accept_eng.png', confidence=0.8)
        # except pyautogui.ImageNotFoundException:
        #     button_location_eng = None
        
        # try:
        #     button_location_eng_active = pyautogui.locateOnScreen('img/buttom_accept_eng_active.png', confidence=0.8)
        # except pyautogui.ImageNotFoundException:
        #     button_location_eng_active = None

        # if button_location_eng is not None or button_location_eng_active is not None:
        #     print("Button found! Accepting the game...")
        #     return True

        # try:
        #     button_location_rus = pyautogui.locateOnScreen('img/buttom_accept_rus.png', confidence=0.8)
        # except pyautogui.ImageNotFoundException:
        #     button_location_rus = None

        # try:
        #     button_location_rus_active = pyautogui.locateOnScreen('img/buttom_accept_rus_active.png', confidence=0.8)
        # except pyautogui.ImageNotFoundException:
        #     button_location_rus_active = None

        # if button_location_rus is not None or button_location_rus_active is not None:
        #     print("Button found! Accepting the game...")
        #     return True

        try:
            button = pyautogui.locateOnScreen('img/buttom.png', confidence=0.8)
        except pyautogui.ImageNotFoundException:
            button = None

        if button is not None:
            print("Button found! Accepting the game...")
            return True

        time.sleep(5)

def show_notification():
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.config(bg="black")
    root.attributes("-transparentcolor", "black")

    duration = 2.5

    img_path = ("img/notification.png")
    img = Image.open(img_path)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo, bg="black", borderwidth=0)
    label.image = photo
    label.pack()

    root.update_idletasks()

    screen_width = root.winfo_screenwidth()
    window_width = img.width
    window_height = img.height

    x = (screen_width // 2) - (window_width // 2)
    target_y = 50
    start_y = -window_height

    root.attributes("-alpha", 0.0)
    root.geometry(f"{window_width}x{window_height}+{x}+{start_y}")

    steps = 20
    current_y = start_y

    for i in range(1, steps + 1):
        alpha = i / steps
        current_y = start_y + int((target_y - start_y) * (i / steps))

        root.attributes("-alpha", alpha)
        root.geometry(f"{window_width}x{window_height}+{x}+{current_y}")
        root.update()
        time.sleep(0.015)

    time.sleep(1.5)

    for i in range(steps, -1, -1):
        alpha = i / steps  
        current_y = start_y + int((target_y - start_y) * (i / steps))
        
        root.attributes("-alpha", alpha)
        root.geometry(f"{window_width}x{window_height}+{x}+{current_y}")
        root.update()
        time.sleep(0.015)

    root.destroy()

if __name__ == "__main__":
    window_title = "Dota 2"
    timer = 2
    wht = 0

    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        window = windows[0]
        window.activate()
        WinActiwe = True
        print(f"Window with title '{window_title}' found and activated.")
    else:
        print(f"Window with title '{window_title}' not found.")
        WinActiwe = False

    GameStarted = waiting_of_start()

    if GameStarted == True and WinActiwe == True:
        time.sleep(timer)
        while wht != 3 :
            keyboard.press_and_release('enter')
            wht += 1

        show_notification()

        print("Game Accepted")
        wht = 0
        exit()