import random
name = input("Enter your name: ")
print ("Hello " + name + "Welcome to KBC")
print("Lets understand the rules of KBC ")
print ("Prize Ladder\nQ1  = ₹1,000\nQ2  = ₹2,000\nQ3  = ₹3,000\nQ4  = ₹5,000\nQ5  = ₹10,000   ← Safe Level 1")
print("Q6  = ₹20,000\nQ7  = ₹40,000\nQ8  = ₹80,000\nQ9  = ₹1,60,000\nQ10 = ₹3,20,000 ← Safe Level 2")
print("Q11 = ₹6,40,000\nQ12 = ₹12,50,000\nQ13 = ₹25,00,000\nQ14 = ₹50,00,000\nQ15 = ₹1,00,00,000")

print("You will be asked 15 questions, each question has 4 options and only one correct answer. You have to choose the correct option to win the prize money. If you answer a question incorrectly, you will leave with the last safe level amount you reached.")
print("Q1-Q4	₹0\nQ5-Q9	₹10,000\nQ10-Q14	₹3,20,000\nQ15	₹1 Crore if correct")

print("Also before every question , you will be asked if you want to quit or continue with the game")

print("Lets Start the Game")

winnings = 0

list_questions = ["What is the capital of India?\n1.New Delhi\n2.Mumbai\n3.Kolkata\n4.Bangalore" , "How many days are there in a leap year?\n1.365\n2.366\n3.364\n4.367" , "Which planet is known as the Red Planet?\n1.Venus\n2.Mars\n3.Jupiter\n4.Saturn" , "Who wrote 'Romeo and Juliet'?\n1.Mark Twain\n2.William Shakespeare\n3.Charles Dickens\n4.Henry Fielding" , "Which gas do plants absorb from the atmosphere?\n1.Oxygen\n2.Carbon Dioxide\n3.Nitrogen\n4.Hydrogen" , "What is the square root of 144?\n1.10\n2.12\n3.14\n4.16" , "Which is the largest ocean on Earth?\n1.Atantic Ocean\n2.Pacific Ocean\n3.Indian Ocean\n4.Southern Ocean" , "Who invented the telephone?\n1.Thomas Edison\n2.Alexander Graham Bell\n3.Guglielmo Marconi\n4.Nikola Tesla" , "Which is the smallest prime number?\n1.0\n2.1\n3.2\n4.3" , "What is the chemical symbol of Gold?\n1.Ag\n2.Au\n3.Fe\n4.Pb" , "Which country hosted the 2016 Summer Olympics?\n1.Brazil\n2.Argentina\n3.Colombia\n4.Peru" , "Who developed the theory of relativity?\n1.Isaac Newton\n2.Albert Einstein\n3.Nikola Tesla\n4.Galileo Galilei" , "What is the SI unit of electric current?\n1.Volt\n2.Ampere\n3.Watt\n4.Joule" , "Which Indian scientist is known as the 'Missile Man of India'?\n1.A.P.J. Abdul Kalam\n2.Homi Bhabha\n3.C.V.Raman}\n4.Srinivasa Ramanujan" , "Which article of the Indian Constitution deals with the Right to Constitutional Remedies?\n1.Article 30}\n2.Article 31}\n3.Article 32}\n4.Article 33}" , "Which is the largest desert in the world?\n1.Sahara Desert\n2.Gobi Desert\n3.Antarctic Desert\n4.Kalahari Desert" , "Which is the largest continent in the world?\n1.Africa\n2.Asia\n3.Europe\n4.Antarctica" , "Which is the largest country in the world by area?\n1.China\n2.USA\n3.Russia\n4.Canada" , "Which is the largest river in the world by discharge volume?\n1.Nile River\n2.Amazon River\n3.Mississippi River\n4.Yangtze River" , "Which is the largest island in the world?\n1.Greenland\n2.New Guinea\n3.Borneo\n4.Madagascar" , "Which is the largest mountain range in the world?\n1.Himalayas\n2.Andes\n3.Rockies\n4.Alps" , "Which is the largest lake in the world by area?\n1.Caspian Sea\n2.Lake Superior\n3.Lake Victoria\n4.Lake Huron" , "Which is the largest waterfall in the world by height?\n1.Angels Falls\n2.Iguazu Falls\n3.Victoria Falls\n4.Niagara Falls" , "Which is the largest volcano in the world?\n1.Mauna Loa\n2.Mount Everest\n3.Krakatoa\n4.Mount Fuji" , "Which is the largest desert in Asia?\n1.Gobi Desert\n2.Thar Desert\n3.Karakum Desert\n4.Kyzylkum Desert" , "Which is the largest bay in the world?\n1.Bay of Bengal\n2.Gulf of Mexico\n3.Hudson Bay\n4.Bay of Biscay"]
list_answers = [
    "1",  # Capital of India
    "2",  # Leap year
    "2",  # Red Planet
    "2",  # Romeo and Juliet
    "2",  # Carbon Dioxide
    "2",  # Square root of 144
    "2",  # Pacific Ocean
    "2",  # Alexander Graham Bell
    "3",  # Smallest prime number
    "2",  # Gold = Au
    "1",  # Brazil
    "2",  # Einstein
    "2",  # Ampere
    "1",  # A.P.J. Abdul Kalam
    "3",  # Article 32
    "3",  # Antarctic Desert
    "2",  # Asia
    "3",  # Russia
    "2",  # Amazon River
    "1",  # Greenland
    "2",  # Andes
    "1",  # Caspian Sea
    "1",  # Angel Falls
    "1",  # Mauna Loa
    "1",  # Gobi Desert
    "1"   # Bay of Bengal
]
list_prize_money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
question_correct = 0
print("Questions:", len(list_questions))
print("Answers:", len(list_answers))

for i in range(15):
    j = random.randint(0, len(list_questions) - 1)
    q = list_questions[j]
    print(q)
    while True:
        answer = input("Enter your answer (1-4): ")

        if answer in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Enter 1, 2, 3 or 4.")
  
    print("You have entered: " + str(answer))
    if answer == list_answers[j]:
        print("Correct Answer! --------------- WON ₹", str(list_prize_money[i]))
        question_correct = question_correct + 1 

        if question_correct == 5:
            print("Congratulations! You have reached the first safe level (₹10,000).")
        if question_correct == 10:
            print("Congratulations! You have reached the second safe level (₹3,20,000).")
        if question_correct == 15:
            print("Congratulations! You have won the grand prize of ₹1 Crore!")
            break
    else:
        print("Incorrect Answer! You have won ₹", str(winnings))
        break
    
    if question_correct < 5:
        winnings = 0
    elif question_correct < 10:
        winnings = 10000
    elif question_correct < 15:
        winnings = 320000
    else:
        winnings = 10000000

    qutting = input("Do you want to quit the game? (yes/no): ")
    if qutting == "yes":
        if question_correct > 0:
            winnings = list_prize_money[question_correct - 1]
        else:
            winnings = 0

        print("You have chosen to quit the game.")
        print("You have won ₹", winnings)
        break


print("\nGame Over!")
print("Your total prize money is: ₹", winnings)
print("Thank you for playing KBC. Hope you enjoyed the game!")