to_do = []
tasks = []

print("% taska a say can be stored and you can type 'EDIT' for editing the tasks completed or changing ")
print("------TO DO------")
for i in range (5):
    to_do = str(input(f"{i+1}: "))    #f string usage
    # to_do = input(str(i+1) , ": ")
    tasks.append(to_do)

print("TASKS STORED ARE AS FOLLOWS: ")

for j in range (5):
    print((j+1) , tasks[j])
    

edit =  input("ENTER YES/NO FOR EDITING: ").upper()
editing = []
if (edit == "YES"):
    task_number = int(input(("Enter which task is to be edited [If no more task is needed to be added then type '0']: ")))
    while task_number != 0:
        if (task_number == 1):
            edited_task = input("Enter the New task: ")
            tasks[0] = edited_task
            

        elif (task_number == 2):
            edited_task = input("Enter the New task: ")
            tasks[1] = edited_task

        elif (task_number == 3):
            edited_task = input("Enter the New task: ")
            tasks[2] = edited_task

        elif (task_number == 4):
            edited_task = input("Enter the New task: ")
            tasks[3] = edited_task

        elif (task_number == 5):
            edited_task = input("Enter the New task: ")
            tasks[4] = edited_task

        else:
            print("Invalid Number given by the user")

        task_number = int(input("Enter another task number (0 to stop): "))  

print("------TASKS ASSIGNED------")

for i in range (5):
    print((i+1) , ". " , tasks[i])

print("Thank You for using To Do APP")

