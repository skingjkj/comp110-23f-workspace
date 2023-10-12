"""EX02 - One-shot Wordle!"""
__author__ = "730665331"

# Declaring the variables that I'm going to use later.
secret_word = "python"
length_of_secret_word = len(secret_word)
letters = str(length_of_secret_word)
user_guess = input("What is your " + letters + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Setting up the variables I need for the response.
index_of_the_word: int = 0
box_emoji: str = ""

# Loop that prompt user to put a guess that have the same length as the secret word.
while len(user_guess) != len(secret_word):
    user_guess = input("That was not " + letters + " letters! Try again: ")

# Loop that compares user's guess to the secret word
while index_of_the_word < len(user_guess):
    # If the letters are in the correct spot, a green box will be added in the respective spot.
    if user_guess[index_of_the_word] == secret_word[index_of_the_word]:
        box_emoji += GREEN_BOX
    # setting up the variables for conditions to test for yellow box.
    else:
        exists_in_word: bool = False
        indices_of_secret: int = 0
    # checks to see if each letter of user's guess are in the secret word but just in the wrong spot.
        while exists_in_word is False and indices_of_secret < len(secret_word):
            if user_guess[index_of_the_word] == secret_word[indices_of_secret]:
                exists_in_word = True
            else:
                indices_of_secret += 1
        if exists_in_word is True:
            box_emoji += YELLOW_BOX
    # A white box is placed if the the letter isn't in the word
        else:
            box_emoji += WHITE_BOX
    index_of_the_word += 1


# Response that is going to be printed based on user's guess.
if user_guess == secret_word:
    print(box_emoji)
    print("Woo! You got it!")
if len(user_guess) == length_of_secret_word and user_guess != secret_word:
    print(box_emoji)
    print("Not quite. Play again soon!")