from functools import reduce

l = [2,4,6,8,10]

newl = list(map(lambda x: x**2,l))
print(newl)

def filter_function(a):
    return a>5

newnewl = list(filter(filter_function , l))

print(newnewl)

numbers = [1,2,3,4,5]
def mysum(x,y):
    return x+y

sum = reduce(mysum , numbers)

print(sum)