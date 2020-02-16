#!Python3

from pynput.keyboard import Key, Controller
import time

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

keyboard = Controller()

#types zulrah kill every 35 minutes
while True:
    keyboard.type('+m kill vorkath')
    enter()
    time.sleep(2100)


