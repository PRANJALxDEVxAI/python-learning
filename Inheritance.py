import math
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"Employee name: {self.name} , Employee ID : {self.id}")

    
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


employee1 = Employee("John", 101)
employee1.show_details()

programmer1 = Programmer("Alice", 102)
programmer1.show_details()
programmer1.showLanguage()