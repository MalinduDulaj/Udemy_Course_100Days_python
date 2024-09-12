import random

word_list=["python","java","react","javascript"]

chosen_word=random.choice(word_list)
print(chosen_word)

#Create a "placeorder" with the same number of blanks as the chosen word

placeorder = "_"
word_length=len(chosen_word)
for position in range(word_length):
    placeorder += "_"
print(placeorder)

guess = input("guess a letter: ").lower()

#create  "display" that puts the guest letter

display = ""

for letter in chosen_word:
    if letter ==guess:
        display += letter
    else:
        display += "-"

print(display)


