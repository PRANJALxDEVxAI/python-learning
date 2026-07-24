import math
dic = {
    "Pranjal" : "Human Being" , 
    "Spoon" : "Object" ,
    567 : "BEAST" ,
    799 : "Harry"
}

print(dic["Spoon"])
print(dic["Pranjal"])

info = {
    "name" : "Pranjal",
    "Age" : 18,
    "Eligible" : "TRUE",
    "CRITERIA" : "ADULT"
}

print(info)
print(info["name"])  #it gives an error in the terminal while running
print(info.get("name"))   #it gives None in output without error if dictionary is not defined for that object
print(info["Age"])
print(info["Eligible"])
print(info["CRITERIA"])

print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

# for value in info.values():       
#     print(info[value])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


print(info.items())

for key , value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

# ----------------------------------DICTIONARY METHODS-------------------------------------------------------

ep1 = {122:45 , 123:89 , 567:69 , 670:69}
ep2={222:40 , 576:89 , 224:98}

# ep1.update(ep2)     #unioning of ep2 in ep1
# ep1.clear()   #clears the dictionaries pairs and make it an empt dict.
# ep1.pop(122)   #removes the key value pair from the dict. made
# ep1.popitem()     #removes the last key value pair from the defined dictinaries
# del ep1[122]
print(ep1)

empt = {}
print(empt)




     



