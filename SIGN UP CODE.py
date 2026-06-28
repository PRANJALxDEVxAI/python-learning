import math 
import random
 
#-------------------------PASSWORD GENERATOR-------------------------

name = input("Enter Your full name: ").title()

username = "".join(name.split()).lower()
username += str(random.randint(10,9999))

choice = input("DO YOU WANT COMPUTER TO MAKE YOUR PASSWORD / YOU WANT TO MAKE YOUR OWN(TYPE OWN / COMPUTER): ").upper()
password = str("")


special = "!@#$%^&*()-_=+[]|;:',.<>?/"

while True: 
    if (choice == "OWN"):
        print("THE PASSWORD MUST CONTAIN AT LEAST 1 NUMBER , 1 SPECIAL CHARATER , 1 CAPITAL LETTER.")
        while True:
            password = input("Create Your Password: ")
            # len_password = len.password()
            # for i in range (len_password):
            has_upper = False
            has_lower = False
            has_digit = False
            has_special = False

            special = "!@#$%^&*()_+-=[]|;:',.<>?/"

            for ch in password:
                if ch.isupper():
                    has_upper = True
                elif ch.islower():
                    has_lower = True
                elif ch.isdigit():
                    has_digit = True
                elif ch in special:
                    has_special = True
                else:
                    print("Invalid character in password")

            if has_upper and has_lower and has_digit and has_special:
                print("Strong Password")
                break
            else:
                print("Weak Password")
                print("THE PASSWORD MUST CONTAIN AT LEAST 1 NUMBER , 1 SPECIAL CHARATER , 1 CAPITAL LETTER.")
                continue
        break

        while True:
            c_password = input("PLEASE CONFIRM YOUR PASSWORD: ")

            if c_password == password:
                print("NEW PASSWORD IS SAVED")
                break
            else:
                print("Incorrect password.")
                

    if (choice == "COMPUTER"):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"
        special = "!@#$%^&*"

        passw = []

        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length must be at least 4.")
            continue


        # Step 1: Add one from each category
        passw.append(random.choice(upper))
        passw.append(random.choice(lower))
        passw.append(random.choice(digits))
        passw.append(random.choice(special))

        # Step 2: Fill the remaining length
        all_characters = upper + lower + digits + special

        for i in range(length - 4):
            passw.append(random.choice(all_characters))

        # Step 3: Shuffle
        random.shuffle(passw)

            # Step 4: Convert list to string
        passw = "".join(passw)

        print(passw)

        while True:
            c_password = input("PLEASE CONFIRM YOUR PASSWORD: ")

            if c_password == passw:
                print("NEW PASSWORD IS SAVED")
                break
            else:
                print("Incorrect password.")

        break

print("NAME : " , name)
print("USERNAME : " , username)
if (choice == "OWN"):
    print("PASSWORD : " , password)
elif (choice == "COMPUTER"):
    print("PASSWORD : " , passw)


            

        


# if (any(ch.islower() for ch in password)
#     and any(ch.isupper() for ch in password)
#     and any(ch.isdigit() for ch in password)
#     and any(ch in special for ch in password)):
#     print("Strong password")
# else:
#     print("Password must contain uppercase, lowercase, number, and special character.")
