import math 
def average(numbers):
    print(type(numbers))
    sum = 0
    for i in numbers: 
        sum = sum + i
    print("Average of numbers is: ", sum / len(numbers))


rang_ = int(input("Enter the range of the number to be asked from you for input: "))
sum = 0
for j in range(rang_):
    num = int(input("Enter" + str(j+1) + " number: "))
    sum = sum+num

average((sum,))