import math

class Employee:
    def __init__(self):
        self.name = "Pranjal"                         #public
        # self.__name = "Pranjal"                       #private
        # self._name = "Pranjal"                        # protected

a = Employee()
print(a.name)
# print(a._Employee__name)                  # Accessing private variable using name mangling
# print(a._name)                            # Accessing protected variable (not recommended, but possible)
print(a.__dir__())                        # To see all attributes of the object, including private ones



