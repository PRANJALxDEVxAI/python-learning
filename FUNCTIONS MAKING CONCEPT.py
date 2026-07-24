import math 
def calculateGmean(a, b):
  mean = (math.sqrt(a*b))
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
    print("The lesser number is: ", min(a, b))
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
isLesser(a,b)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
isLesser(c,d)  