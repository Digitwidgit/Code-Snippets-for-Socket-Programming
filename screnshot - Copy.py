import pyautogui
import time
import os


for i in range(5):

    pic= pyautogui.screenshot()
    pic.save('screenshot_{0}.png'.format(i))

    time.sleep(5)
    
