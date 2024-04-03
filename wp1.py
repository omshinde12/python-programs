import pyautogui
import time
time.sleep(3)
count=0
while count<50:
   pyautogui.typewrite("happy birthday"+ str(count))
   pyautogui.press("enter")
   count=count+1
