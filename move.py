#!/usr/bin/env python3

import pyautogui
import time
import random

i = 0
move = 10
sleep_time = 20
print('Thanks for stopping by')

while True:
    if i % 2 == 0:
        move = random.randint(5, 25)
        pyautogui.moveRel(0, move)

    else:
        pyautogui.moveRel(0, -move)

    i += 1

    sleep_time = random.randint(5, 35)
    time.sleep(sleep_time)
