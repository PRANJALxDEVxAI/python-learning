import os

folder = input("Enter folder path: ")
extension = input("Enter the extension so that they can be renamed: ")
count = 1
for file in os.listdir(folder):
    if (file.endswith(extension)):
        print(file)
        new_name = (f"{count}.{extension}")
        old_path = os.path.join(folder , file)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        count +=1
        print(os.listdir(folder))







