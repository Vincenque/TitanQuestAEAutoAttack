from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

scriptOffMesseagePrinted = True
print("Press 'O' to turn script on")
while True:
    keyState = win32api.GetKeyState(79) #79 = O
    if keyState == 1:
        print("Script on")
    elif keyState != 1 and scriptOffMesseagePrinted == False:
        print("Script off")
        scriptOffMesseagePrinted = True
    while keyState == 1:
        scriptOffMesseagePrinted = False
        keyState = win32api.GetKeyState(79) #79 = O
        #print(pyautogui.pixel(905,65))
        if pyautogui.pixel(905,65)[0]>200:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
       
