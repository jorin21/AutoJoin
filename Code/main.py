import os
import time
import pyautogui
from time import sleep
from datetime import datetime



date = datetime.now().strftime("%b %d")
time = datetime.now().strftime("%I:%M%p")


with open('Dates.txt', 'r') as read_obj:
    for line in read_obj:
        if date in line:
            ss = line.split("=")
            if ss[1].strip() == 'b':
                if time == "07:40AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Python AutoJoin Script\Code\Classes\Class 1.lnk")
                    sleep(1)
                    print('.')
                    sleep(9)
                    mute = pyautogui.locateCenterOnScreen("Images/mute.PNG") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("Images/join.PNG") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Your Class!')
            if ss[1].strip() == 's':
                if time == "07:40AM":
                    print(time)
                    os.startfile("C:/Users/jorge/Desktop/Python AutoJoin Script/Code/Classes/Class 2.lnk")
                    sleep(1)
                    print(".")
                    sleep(9)
                    mute = pyautogui.locateCenterOnScreen("Images/mute.PNG") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("Images/join.PNG") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Your Class!')


    