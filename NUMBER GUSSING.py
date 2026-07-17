import random

number = random.randint(1,100)

while True:
    attempts = 0
    while True:
        your_guess = int(input("Enter your guess: "))

        if your_guess == number:
            print("Congrats the number was:", number)
            print("It took you", attempts, "attempts.")
            break
        elif your_guess < number:
            attempts +=1
            print("Higher")
        else:
            attempts +=1
            print("Lower")

    while True:
        a = input("Want another game? YES or NO: ")
        if a == "YES":
            break
        elif a == "NO":
            print("Goodbye")
            exit()
        else:
            print("Input is not valid")

