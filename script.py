import pyautogui
import time

time.sleep(5)

pyautogui.moveTo(1620, 640, duration=0.5)  # Move to (x=500, y=400)

num_clicks = 100

delay = 0.1

for i in range(num_clicks):
    pyautogui.moveTo(1624, 645, duration=0.1)  
    time.sleep(delay)
    pyautogui.moveTo(1620, 640, duration=0.1)  
    pyautogui.click()
    print(f"Click {i+1} done")

