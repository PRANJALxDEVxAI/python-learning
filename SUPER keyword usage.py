import math 

class Employee:
    def __init__(self , name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self ,name,id, lang):
        super().__init__(self,id)
        self.lang = lang


pranjal = Employee("Pranjal Gupta" , "420")
harry = Programmer("Harry" , "2345" , "Python" )
print(pranjal.name)
print(pranjal.id)
print(harry.lang)