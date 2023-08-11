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

while True:
    keyState = win32api.GetKeyState(79) #79 = O
    while keyState == 1:
        keyState = win32api.GetKeyState(79) #79 = O
        #print(pyautogui.pixel(953,65)[0])
        if pyautogui.pixel(953,65)[0]==248 or pyautogui.pixel(953,65)[0]==90:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
       
