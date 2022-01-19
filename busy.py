import pyautogui
import time

pyautogui.FAILSAFE = True

while True:
    pyautogui.moveRel(300, 0, duration=0.25)
    pyautogui.click()
    time.sleep(30)
    pyautogui.moveRel(-300, 0, duration=0.25)
    pyautogui.click()
