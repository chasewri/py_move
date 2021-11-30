import pyautogui
import time

i = 0

while True:
  if i % 2 == 0:
    pyautogui.moveRel(0, 10)
  else:
    pyautogui.moveRel(0, -10)
  
  i += 1

  time.sleep(20)