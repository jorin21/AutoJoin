import os
import time
import pyautogui
from time import sleep
from datetime import datetime



date = datetime.now().strftime("%b %d")
time = datetime.now().strftime("%I:%M%p")


with open("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Dates.txt", 'r') as read_obj:
    for line in read_obj:
        if date in line:
            ss = line.split("=")
            if ss[1].strip() == 's':
                if time >= "07:35AM" and time < "09:10AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 1.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Physics Jorge!')
                if time >= "09:15AM" and time < "10:48AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 2.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Engineering Jorge!')
                if time >= "10:55AM" and time < "11:20am":
                    print(time)
                    print("no classes right now")
                if time == "11:31AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 3.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Stats Jorge!')
                if time == "01:05PM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 4.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Econ Jorge!')
            if ss[1].strip() == 'b':
                if time >= "07:35AM" and time < "09:10AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 5.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy English Jorge!')
                if time >= "09:15AM" and time < "10:48AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 6.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Study Hall Jorge!')
                if time == "10:52AM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 7.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Psych Jorge!')
                if time == "01:05PM":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 8.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png") 
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png") 
                    pyautogui.moveTo(join)
                    pyautogui.click()
                    sleep(2)
                    print('Enjoy Media Studs Jorge!')


    