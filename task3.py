import random
print("Welcome to the Word Scramble Game!")
word = "Nader"
word_list = list(word)
random.shuffle(word_list)
scramble_word = ''.join(word_list)
print(f"Try to guess the original word from the scrambled word: {scramble_word}")
x = 5
print(f"You have {x} attempts")
while x > 0:
  z = input("Enter your guess:")
  if(z == word):
    print("Congratulations! You guessed the correct word!")
    break
  else:
    x -= 1
    if(x > 0):
      print (f"Incorrect! Try again. You have {x} attempts left.")
    else:
      print(f"You’re out of attempts! The correct word was: {word}")