import os
import time
import pyautogui
from time import sleep
from datetime import datetime


x = 1
print("starting")
date = datetime.now().strftime("%b %d")
time = datetime.now().strftime("%I:%M%p")
with open('Dates.txt', 'r') as read_obj:
    for line in read_obj:
        if date in line:
            ss = line.split("=")
            if ss[1].strip() == 'b':
                print(time)
                if time == "08:44PM":
                    print(time)
                    print(x)
                    x = x + 1
                    print("voy")
                    os.startfile("C:/Users/jorge/Desktop/Auto MS Teams Code/AutoJoin/Code/Classes/Class 1.lnk") 

    