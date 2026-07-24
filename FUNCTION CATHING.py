# import functools
from functools import lru_cache
import time

@lru_cache(maxsize = None)                #FUNCTION GETS MEMOIZED
def fx(n):
    time.sleep(5)
    return(5**n)


print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")


print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")



