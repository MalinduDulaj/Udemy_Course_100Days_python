import random

word_list=["python","java","react","javascript"]

chosen_word=random.choice(word_list)
print(chosen_word)

placeorder = "_"
word_length=len(chosen_word)
for position in range(word_length):
    placeorder += "_"
print(placeorder)

#-Use a while loop  to lrt the user guess again

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""

    #change the for loop previous correct letter in display


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "-"

    print(display)

    # if "_" not in display:
    #     game_over = True
    #     print("You Win")


