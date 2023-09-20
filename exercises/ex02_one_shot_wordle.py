__author__ = "730665331"

#Declaring the variables that I'm going to use later.
secret_word= "python"
length_of_secret_word= len(secret_word)
storing_as_string=str(length_of_secret_word)
user_guess= str=input("What is your " + storing_as_string + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


index_of_the_word: int = 0
box_emoji: str=""


while len(user_guess) != len(secret_word):
    user_guess= str=input("That was not " + storing_as_string +  " letters! Try again: ")

while index_of_the_word< len(user_guess):
    if user_guess[index_of_the_word]==secret_word[index_of_the_word]:
        box_emoji += GREEN_BOX
    else :
        exists_in_word: bool = False
        indices_of_secret: int = 0
        while exists_in_word == False and indices_of_secret < len(secret_word):
            if user_guess[index_of_the_word] == secret_word[indices_of_secret]:
                exists_in_word = True
            else:
                indices_of_secret += 1
        if exists_in_word == True:
            box_emoji += YELLOW_BOX
        else:
            box_emoji += WHITE_BOX
    index_of_the_word += 1



if user_guess==secret_word:
        print(box_emoji)
        print("Woo! You got it!")
if len(user_guess) ==length_of_secret_word and user_guess!=secret_word:
      print(box_emoji)
      print("Not quite. Play again soon!")

