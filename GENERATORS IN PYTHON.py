def my_generator():
    for i in range(5):
        yield i       #genrates a genrator


gen = my_generator()
# print(next(gen))    #To access the generator
# print(next(gen))    #To access the generator
# print(next(gen))    #To access the generator
# print(next(gen))    #To access the generator
for j in gen:
    print(j)          #To access the generator
