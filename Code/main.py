import os
import time
import pyautogui
from time import sleep
from datetime import datetime
    
date = datetime.now().strftime("%b %d")
time = datetime.now().strftime("%I:%M%p")
c_time = datetime.now().strftime("%H:%M")

with open("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Dates.txt", 'r') as read_obj:
    for line in read_obj:
        if date in line:
            ss = line.split("=")
            if ss[1].strip() == 's':
                if c_time >= "07:35" and c_time < "09:10":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 1.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Physics Jorge!')
                if c_time >= "09:15" and c_time < "10:48":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 2.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Engineering Jorge!')
                if c_time > "10:48" and c_time < "11:30":
                    print(f"It's {time}")
                    print("No classes right now Jorge. Enjoy your lunch")
                if c_time >= "11:30" and c_time < "13:02":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 3.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Stats Jorge!')
                if c_time >= "13:05" and c_time < "14:40":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes\Class 4.lnk")
                    sleep(1)
                    print('.')
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Econ Jorge!')
            if ss[1].strip() == 'b':
                if c_time >= "07:35" and c_time < "09:10":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 5.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy English Jorge!')
                if c_time >= "09:15" and c_time < "10:48":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 6.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Study Hall Jorge!')
                if c_time >= "10:52" and c_time < "12:26" and not c_time == "11:30":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 7.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Psych Jorge!')
                else:
                    print('Keep it up in Psych Jorge!')
                if c_time > "12:26" and c_time < "13:05":
                    print(f"It's {time}")
                    print('No classes at this time Jorge. Have lunch!')
                if c_time >= "13:05" and c_time < "14:40":
                    print(time)
                    os.startfile("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Classes/Class 8.lnk")
                    sleep(1)
                    print(".")
                    sleep(24)
                    mute = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\mute.png")

                    if mute == None:
                        print('Mute Not Found. Moving to next button.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(mute)
                        pyautogui.click()
                        sleep(1)

                    join = pyautogui.locateCenterOnScreen("C:/Users\jorge\Desktop\Auto MS Teams Code\AutoJoin\Code\Images\join.png")

                    if join == None:
                        print('Join Not Found. Please run again.')
                        sleep(1)
                    else:
                        pyautogui.moveTo(join)
                        pyautogui.click()
                        sleep(1)
                        print('Enjoy Media Studs Jorge!')   