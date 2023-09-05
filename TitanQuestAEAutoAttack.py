from pyautogui import *
import pyautogui
import time
import win32api, win32con
import customtkinter
import threading
import pydirectinput

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

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
                scriptOnOffLabel.configure(text = "Script is off", text_color = "red")
                scriptOffMesseagePrinted = True
            while keyState == 1:
                scriptOffMesseagePrinted = False
                scriptOnOffLabel.configure(text = "Script is on", text_color = "green")
                keyState = win32api.GetKeyState(79) #79 = O
                if pyautogui.pixel(905,65)[0] > 200 and pyautogui.pixel(905,65)[1] > 180 and pyautogui.pixel(905,65)[2] > 60:
                    hpBarOnScreen = True
                else:
                    hpBarOnScreen = False
                #print(pyautogui.pixel(905,65))
                if hpBarOnScreen == True and fightType.get() == "Ranged":
                    print("Ranged")
                    pydirectinput.keyDown('shift')
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    pydirectinput.keyUp('shift')
                elif hpBarOnScreen == True and fightType.get() == "Melee":
                    print("Melee")
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

nameLabel = customtkinter.CTkLabel(root, text = "Titan Quest Anniversary Edition Auto Attack Script", fg_color = "#0062b1", corner_radius=8)
nameLabel.pack(pady=10, padx=30) 

fightType = customtkinter.StringVar(value = "Melee")
meleeRadioButton = customtkinter.CTkRadioButton(root, text = "Melee", variable = fightType, value = "Melee")
meleeRadioButton.pack(pady=10, padx=10)
rangedRadioButton = customtkinter.CTkRadioButton(root, text = "Ranged", variable = fightType, value = "Ranged")
rangedRadioButton.pack(pady=10, padx=10)

toggleLabel = customtkinter.CTkLabel(root, text = "Press 'O' to toggle script")
toggleLabel.pack(pady=3, padx=30)

scriptOnOffLabel = customtkinter.CTkLabel(root, text = "Script is off", text_color = "red")
scriptOnOffLabel.pack(pady=3, padx=30)
root.mainloop()




    
