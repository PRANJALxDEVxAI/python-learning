# import os

# # os.chdir("c:\\Users\\coolv\\AppData\\Local\\Programs\\Microsoft VS Code")

# # os.chdir("c:\\Users\\coolv\\Desktop")

# # os.chdir(r"C:\Users\coolv\Desktop")     #The r means Python won't treat \ as escape characters.

# # print(os.listdir())

# # print(os.getcwd())

# # print(os.listdir(r"C:\Users\coolv"))

# # os.mkdir(r"C:\Users\coolv\Desktop\OS MODULING")

# # os.makedirs(r"C:\Users\coolv\Desktop\OS MODULING\A,B,C")

# if os.path.exists("hello.txt"):
#     print("Exists")
# else:
#     print("Not Found")

# print(os.path.isfile("hello.txt"))

# os.remove("notes.txt")

# print(os.path.isdir("Downloads"))

# print(os.path.abspath("hello.txt"))

# os.system("explorer")

# os.system(r'explorer "C:\Users"')

# for folder, subfolders, files in os.walk("."):
#     print("Folder:", folder)
#     print("Subfolders:", subfolders)
#     print("Files:", files)
#     print()


# path = r"C:\Users\YourName\Desktop\hello.txt"

# print(os.path.basename(path))


# print(os.path.dirname(path))


# print(os.path.splitext("photo.png"))


# print(os.path.dirname(os.path.abspath(__file__)))


# filename = input("Enter filename: ")

# if os.path.exists(filename):
#     print("Found!")
#     print("Size:", os.path.getsize(filename))
#     print("Location:", os.path.abspath(filename))
# else:
#     print("File doesn't exist.")



# for file in os.listdir():
#     if file.endswith(".py"):
#         print(file)



# files = os.listdir()

# count = 1

# for file in files:
#     if file.endswith(".txt"):
#         new_name = f"File_{count}.txt"
#         os.rename(file, new_name)
#         count += 1


