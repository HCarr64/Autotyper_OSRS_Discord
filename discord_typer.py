#!Python3

from pynput.keyboard import Key, Controller
import time
import csv

def confirm():
    keyboard.press('c')
    keyboard.press('o')
    keyboard.press('n')
    keyboard.press('f')
    keyboard.press('i')
    keyboard.press('r')
    keyboard.press('m')

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

keyboard = Controller()

time.sleep(2)
with open('disc_inv.csv', 'r') as f:
    reader = csv.reader(f)
    your_list =list(reader)

for row in your_list:
    string=row[0]+' '+row[1]+' '+ row[2]
    keyboard.type(string)
    enter()
    time.sleep(4)
    confirm()
    enter()
    time.sleep(4)


