x = int(input("Enter Your number: "))

match x: 
    case _ if (x>0):
        print("Positive number")
    case _ if (x<0):
        print("Negative number")
    case _:
        print("Zero")

