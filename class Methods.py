import math

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")


    @classmethod                                #changes the class variables value (forms a finction for changing class variables value)
    def changecompany(cls , newCompany):
        cls.comapny = newCompany



e1 = Employee()
e1.name = "Pranjal"
e1.changecompany("Tesla")
e1.show()

print(Employee.company)