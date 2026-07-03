import random

# player = ["Snake" , "Water" , "Gun"]

# matches = 5
# player_score = 0
# computer_score = 0

# for i in range(matches):
#     computer = random.choice(player)

#     player_choice = input("Player Turn Snake , Water , Gun ?: ").title()

#     print("Computer Turn: Snake , Water , Gun ?: " , computer)
#     if player_choice == computer:
#         print("Its a Draw")
#     elif(player_choice == "Snake" and computer == "Water") or (player_choice == "Water" and computer == "Gun") or (player_choice == "Gun" and computer == "Snake"):
#         player_score +=1
#         print("Player Wins!")
#     else:
#         computer_score +=1
#         print("Computer Wins!")

#     matches -=1    

# print("Player Score: " , player_score)
# print("Computer Score: " , computer_score)

# if(player_score > computer_score):
#     print("Player Wins The Game!")
# elif(player_score < computer_score):
#     print("Computer Wins The Game!")
# else:
#     print("The Game is a Draw!")
    

choices = [0,1,2]
matches = 5
matrix = [[0,1,2] , [2,0,1] , [1,2,0]]
player_score = 0
computer_score = 0

while matches>0:
    while True:
        try:
            player_choice = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")
    computer_choice = random.randint(0,2)
    print("Computer Turn: ", computer_choice)
    matches -= 1
    result = matrix[player_choice][computer_choice]
    if result == 0:
        print("Its a Draw")
    elif result == 1:
        player_score += 1
        print("Player Wins!")
    else:
        computer_score += 1
        print("Computer Wins!")

print("\nFinal Score")
print("Player Score: " , player_score)
print("Computer Score: " , computer_score)
if(player_score > computer_score):
    print("Player Wins The Game!")
elif(player_score < computer_score):
    print("Computer Wins The Game!")
else:
    print("The Game is a Draw!")

