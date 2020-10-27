Python Screenshot Generator
--------

App to generate a screenshot from websites built with Python/Django and Selenium.

![Python Screenshot Generator](/static/img/python_screenshot_generator.png)

#---------------------------Another Desktop Version------------------------------#

import time
import tkinter as tk
import pyautogui as pg


def screenshot():
    name = int(round(time.time())*1000)
    #time.sleep(5)
    img = pg.screenshot("C:\\Users\\91901\\Desktop\\python\\Screenshots data\\{}.png".format(name))
    img.show()

win = tk.Tk()
win.title("ScreenshotApp")
win.geometry("450x500")
frame = tk.Frame(win)
frame.pack()
button = tk.Button(frame, text = "Capture Screenshot", command = screenshot)
button.pack(side = tk.LEFT)
close = tk.Button(frame, text = "Quit", command = quit)
close.pack(side = tk.LEFT)
win.mainloop()
