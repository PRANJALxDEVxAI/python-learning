print("Hello World")
name = "Pranjal" 
age = "18" 
print("My name is " + name + " and I am " + str(age) + " years old.")
name = input(" Enter your name: ")
print(" Hello ", name)
d = int(input("Enter your first number: "))
c = int(input("Enter your second number: "))
print("Sum = ",d + c)
if d>=c:
    
    print("The given numbers are saying that your FIRST number is GREATER than Second number you have entered.")
    print("Difference= ",d - c)
    print("Remainder= ",d % c)
    print("Quotient= ",d / c)

else: 
    print(" The given numbers are saying that your SECOND number is GREATER than FIRST number you have entered.")
    print("Difference= ",c - d)
    print("Remainder= ",c % d)
    print("Quotient= ",c / d)

print("Product= ",d * c)
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

for i in range(5):
    for j in range(i+1):
        print("*", end="")
        
    print()    



