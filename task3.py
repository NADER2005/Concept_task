import random
print("Welcome to the Word Scramble Game!")
word_list = ["Nader" , "Elsayed" , "Hassan" , "Soliman"]
word = random.choice(word_list)
chosen_word = list(word) # Nader-> ['N' , 'a' , 'd' , 'e' , 'r']
random.shuffle(chosen_word)
scramble_word = ''.join(chosen_word)
print(f"Try to guess the original word from the scrambled word: {scramble_word}")
x = 5
print(f"You have {x} attempts.")
while x > 0:
    z = input("Enter your guess: ")
    if(z == word):
      print("Congratulations! You guessed the correct word!")
      break
    else:
        x -= 1 # x = x-1
        if(x > 0):
            print(f"Incorrect! Try again. You have {x} attempts left.")
        else:
            print(f"You’re out of attempts! The correct word was: {word}")