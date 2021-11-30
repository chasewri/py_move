#!/usr/bin/env

import pyautogui
import time
import random

i = 0
move = 10
sleep_time = 20
run_option = int(input('Enter 1 for notabs or 2 for tabs: '))

while True:
    if i % 2 == 0:
        move = random.randint(5, 25)
        pyautogui.moveRel(0, move)
        if run_option != 1 and move > 15:
            for _ in range(2):
                with pyautogui.hold('command'):
                    pyautogui.press(['tab'])
    else:
        pyautogui.moveRel(0, -move)

    i += 1

    sleep_time = random.randint(15, 35)
    time.sleep(sleep_time)
