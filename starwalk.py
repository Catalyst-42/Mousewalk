import os
import time

os.system("clear")
w, h = os.get_terminal_size()
x, y = w // 2, h // 2
x_direction, y_direction = 1, 1

h -= 1

while True:
    time.sleep(.1)
    for i in range(h):
        if i == y:
            print(' '*(x-1) + '*' + ' '*(w-x)) 
        else:
            print(' '*w)

        
    if x == w: x_direction = -1
    elif x == 0: x_direction = 1

    if y == h: y_direction = -1
    elif y == 0: y_direction = 1

    x += x_direction
    y += y_direction        

