import time
import tkinter as tk

from pynput.mouse import Controller
from pynput.mouse import Listener

root = tk.Tk()
mouse = Controller()

w, h = root.winfo_screenwidth() - 1, root.winfo_screenheight() - 1
print(f'mouse walking on {w+1, h+1} screen')

# Exit on user input
x_prev, y_prev = mouse.position
going_exit = False

def on_move(x, y):
    global x_prev, y_prev, going_exit

    if abs(x_prev - x) != abs(y_prev - y):
        going_exit = True
        return False
    
    x_prev, y_prev = x, y

listener = Listener(on_move=on_move)
listener.start()

# Walk
move_x = 1
move_y = 1

while True:
    mouse.move(move_x, move_y)
    time.sleep(0.001)
    
    if mouse.position[1] >= h:
        move_y = -1
    
    if mouse.position[1] <= 1:
        move_y = 1

    if mouse.position[0] >= w:
        move_x = -1
    
    if mouse.position[0] <= 1:
        move_x = 1

    if going_exit:
        break
