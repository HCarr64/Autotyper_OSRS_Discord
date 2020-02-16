#!Python3

from pynput.keyboard import Key, Controller
import time
import csv

def confirm():
    keyboard.type('confirm')

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

keyboard = Controller()

time.sleep(2)
with open('disc_inv.csv', 'r') as f:
    reader = csv.reader(f)
    your_list =list(reader)

for row in your_list:
    string=row[0]+' '+row[2]+' '+ row[1]
    keyboard.type(string)
    enter()
    time.sleep(3)
    confirm()
    enter()
    time.sleep(3)


