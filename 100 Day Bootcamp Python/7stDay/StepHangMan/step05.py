import random

stages = [
        """
        -----
        |   |
        O   |
        /|\\  |
        / \\  |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
        /|\\  |
        /    |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
        /|\\  |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
        /|   |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        ---------
        """,
        """
        -----
        |   |
            |
            |
            |
            |
        ---------
        """
    ]

word_list=["python","java","react","javascript"]

#Create a variable called "lives" to track of the number
#Set lives equal 6

lives = 6

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

    #If guess a not in letter in the chosen_word, then reduce "lives" by 01.
    #if lives goes to down 0then the game should stop and it should print  "You lose"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over=True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You Win")

    #print the ASCII ART from 'stages'
    #that corresponds to the current number of the "lives" the user has remaining
    
    print(stages[lives])