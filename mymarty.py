# http://docs.robotical.io/python/martypy/

import martypy
mymarty = martypy.Marty('socket://192.168.2.30') # Change IP accordingly
mymarty.hello()  # Move to zero positions and wink

print("Start walking")
count = 0
while count < 10:
    print("The count is: ", count)
    mymarty.arms(127, -127, 1000)
    mymarty.walk(10)
    mymarty.circle_dance('left', 3000)
    mymarty.walk(21, 'auto', 127, 40, 1000)
    mymarty.eyes(90)
    count = count + 1
print("Done")
