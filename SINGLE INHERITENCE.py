import math

class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by an animal")

class Cat(Animal):
    def __init__(self , name , breed):
        Animal.__init__(self,name,species = "Cat")
        self.breed = breed 

    def make_sound(self):
        print("MEOW!")


d = Cat("Cat" , "CATOMPOLIS")
print(d.make_sound())
a = Animal("Cat" , "Cat")
print(a.make_sound())