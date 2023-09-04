from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import customtkinter
import threading

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def buttonClicked():
    print("Button clicked")
    #myLabel2 = Label(root, text = "Test3")
    #myLabel2.grid(row = 2, column = 0)

def radioButtonClicked():
    print("Radio button clicked")
    #myLabel3 = customtkinter.CTkLabel(root, text = fightType.get())
    #myLabel3.grid(row = 6, column = 0)


class MyApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global scriptOffMesseagePrinted
        while True:
            keyState = win32api.GetKeyState(79) #79 = O
            if keyState == 1:
                print("Script on")
            elif keyState != 1 and scriptOffMesseagePrinted == False:
                print("Script off")
                myLabel4.configure(text = "Script is off", text_color = "red")
                scriptOffMesseagePrinted = True
            while keyState == 1:
                scriptOffMesseagePrinted = False
                myLabel4.configure(text = "Script is on", text_color = "green")
                keyState = win32api.GetKeyState(79) #79 = O
                #print(pyautogui.pixel(905,65))
                if pyautogui.pixel(905,65)[0]>200:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    

scriptOffMesseagePrinted = True
print("Press 'O' to turn script on") 
app = MyApp()
app.start()

root = customtkinter.CTk()
root.geometry("400x210")
root.title("Titan Quest Anniversary Edition - Auto Attack Script")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

myLabel1 = customtkinter.CTkLabel(root, text = "Titan Quest Anniversary Edition Auto Attack Script", fg_color = "#0062b1", corner_radius=8)
myLabel1.pack(pady=10, padx=30) 

fightType = customtkinter.StringVar(value = "Melee")
radioButton1 = customtkinter.CTkRadioButton(root, text = "Melee", variable = fightType, value = "Melee", command = radioButtonClicked)
radioButton1.pack(pady=10, padx=10)
radioButton2 = customtkinter.CTkRadioButton(root, text = "Ranged", variable = fightType, value = "Ranged", command = radioButtonClicked)
radioButton2.pack(pady=10, padx=10)

myLabel3 = customtkinter.CTkLabel(root, text = "Press 'O' to toggle script")
myLabel3.pack(pady=3, padx=30)

myLabel4 = customtkinter.CTkLabel(root, text = "Script is off", text_color = "red")
myLabel4.pack(pady=3, padx=30)
root.mainloop()




    
