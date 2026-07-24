import math

class People:
    name = "Pranjal"
    occupation = "Software Developer"
    networth = 12
    def info(self):
        print(f"{self.name} is a {self.occupation} and has a networth of ₹ {self.networth} Lakh ")



a = People()
# a.name = "BPG"
# a.occupation = "Gamer"
# print(a.name)
a.info() 