a = True
print(a := False)

numbers  = [1,2,3,4,5]
while(n:= len(numbers)) > 0:            # ":" - Helps to define the value of n with in the condition or execution 
    print(numbers.pop())

print(numbers)