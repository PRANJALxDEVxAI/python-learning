import math
import time

def usingWhile():
    i = 0
    while i<50000:
        i = i+1
        print(i)

def usingFor():
    for i in range (50000):
        print(i)

init  = time.time()
usingFor()
print(time.time() - init)
init = time.time()
usingWhile()
print(time.time() - init)
print(4)
print("This message is printed 5 sec after the previous")
t = time.localtime()
formatted_time = time.strftime("%Y - %m - %d %H:%M:%S" , t)
print(formatted_time)