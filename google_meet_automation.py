import pyautogui as pa
import os
import time

meet=str(input("Enter the meeting ID: "))

chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
os.startfile(chrome)

time.sleep(2) # seconds can be increased or decreased according to your system performance
pa.click(626,584)  #selecting the first chrome user , the arguments passed in the click fuction is x and y axis of mouse cursor

time.sleep(2)
pa.hotkey('ctrl','t') #new tab

time.sleep(3)
pa.write('https://meet.google.com/',interval=0.05)
pa.write(meet,interval=0.05)
pa.press('enter')

time.sleep(5)
pa.hotkey('ctrl','e')  #cam off

time.sleep(2)
pa.hotkey('ctrl','d') # mic off

time.sleep(2)
pa.click(1350,610)    #join now
pa.moveTo(954,524)     #centre
