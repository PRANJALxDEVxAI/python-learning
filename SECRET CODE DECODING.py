import random

def give():
    secret_code = input("Enter the secret code: ")
    decode = secret_code[3:-3]
    decode_word = decode[-1] + decode[0:-1]
    

    return print("DECODED WORD: " , decode_word)

def decoding():
    word = input("Enter the word to convert it into secret code: ")
    sc = word[1:len(word)]+(word[0].upper())
    alphas = "abcdefghijklmnopqrstuvwxyz"
    code_word = random.choice(alphas)+random.choice(alphas)+random.choice(alphas)+sc+random.choice(alphas)+random.choice(alphas)+random.choice(alphas)
    return print("Coded Word: " , code_word)


give()
decoding()



        
        
        