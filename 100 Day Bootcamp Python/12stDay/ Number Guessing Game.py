from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against the actual answer
def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining. """
    if user_guess > actual_answer:
        print("Too high")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = None

    while turns > 0 and guess != answer:
        # Let the user guess a number
        guess = int(input("Make a guess: "))

        check_answer(guess, answer,turns)

        # Track the number of turns and reduce by 1 if they get it wrong
        turns -= 1
        if guess != answer:
            print(f"You have {turns} attempts remaining.")

        if turns == 0:
            print("You've run out of guesses, you lose!")

game()
