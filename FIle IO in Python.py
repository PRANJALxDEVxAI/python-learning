# # READING A FILE

# # f = open('myfile.txt' , 'r')
# # text = f.read()
# # print(text)
# # f.close()


# #Writing A FILE ------------- Overwrites the existing content of the file
# # f = open('myfile.txt' , 'w')
# # f.write('Hello World!')
# # f.close()


# #ALternative Method
# # with open('myfile.txt' , 'a') as f:    #-----------------Appending the file context
# #     f.write('Hello World!')

# # f = open('myfile.txt', 'r')
# # i = 0
# # while True:
# #   i = i + 1
# #   line = f.readline()
# #   if not line:
# #     break
# #   m1 = int(line.split(",")[0])
# #   m2 = int(line.split(",")[1])
# #   m3 = int(line.split(",")[2])
# #   print(f"Marks of student {i} in Maths is: {m1*2}")
# #   print(f"Marks of student {i} in English is: {m2*2}")
# #   print(f"Marks of student {i} in SST is: {m3*2}")

# #   print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()