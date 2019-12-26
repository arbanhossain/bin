import ctypes
import time
import pyautogui as pg

"""
After 20 mins of work, tells to
give the eyes a rest for 20 sec

After 50 mins of work, tells to
take a break for 10 mins
"""

while True:
    time.sleep(20*60)
    ctypes.windll.user32.MessageBoxW(0, "Avert your eyes\nfor 20 seconds", "20-20-20" , 0)
    time.sleep(20*60)
    ctypes.windll.user32.MessageBoxW(0, "Avert your eyes\nfor 20 seconds", "20-20-20" , 0)
    time.sleep(10*60)
    ctypes.windll.user32.LockWorkStation()
    time.sleep(10*60)
    pg.press('enter')
    print("\a")
