import random

word_list=["python","java","react","javascript"]

#-Randomly choose a word from word list and assign to variable called chosen word.then print it

chosen_word=random.choice(word_list)
print(chosen_word)


#-Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("guess a letter: ").lower()
print(guess)

#-Check if the user guess

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

