import maths

class Person:
    def __init__(self,n,o):
        print("Hey I am a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")


#self is a keyword which is used to refer to the current instance of the class. It is used to access variables that belong to the class.


a = Person("Harry" , "Developer")
b = Person("PRANAY" , "Designer")
a.info()
b.info()
0