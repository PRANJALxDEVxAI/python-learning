def multiplication(a,b):
    return a*b

def name():
    n = input("What is your name: ")
    print("Warm greeting to "+n)

def add(c,d):
    return a+bin
def subtract(ef):
    if e>=f:
        return e-f
    else:
        return f-e
        
def divide(g,h):
    if h!=0:
        return (g/h)
    else:
        return ("Error:DIVISION BY ZERO IS UNDEFINED")

def modulus(i,j):
    if j!=0:
        return (i%j)
    else:
        return ("Error:DIVISION BY ZERO IS UNDEFINED")

def exponent(k,l):
    return (k**l)

def floor_division(m,n):
    if n!=0:
        return (m//n)
    else:
        return ("Error:DIVISION BY ZERO IS UNDEFINED")
while True:

    choice = input("Enter operation (+,-,/,//,%,*,**,QUIT): ")
    if(choice == "QUIT"):
        print("Exiting the calculator. Goodbye!")
        break
    else:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))


        if(choice == "+"):
            result = add(x,y)
        elif(choice == "-"):
            result = subtract(x,y)
        elif(choice == "/"):
            result = divide(x,y)
        elif(choice == "//"):
            result = floor_division(x,y)
        elif(choice == "%"):
            result = modulus(x,y)
        elif(choice == "*"):
            result = multiplication(x,y)
        elif(choice == "**"):
            result = exponent(x,y)
        else:
            print("Invalid operation")
        print("Result: ",result)
        


    