"""EX03 - Wordle with functions!"""
__author__ = "730665331"

# Defining the variables.

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # defining the variables
    secret: str = "codes"
    length_of_secret: int = len(secret)
    user_guess: str = ""
    emoji: str = ""
    turns: int = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        # getting user's input
        user_guess = input_guess(length_of_secret)
        # setting up to show user their guesses in boxes
        emoji = emojified(user_guess, secret)
        print(emoji)

    # If statements to see if the user won or not
        if user_guess == secret:
            print(f"You won in {turns}/6 turns!")
            turns = 10
        elif user_guess != secret and turns < 6:
            turns += 1
        else:
            turns += 1
            print("X/6 - Sorry, try again tomorrow!")


# checks every letter in the word
def contains_char(word_being_searched: str, character_to_look_for: str) -> bool:
    """Checks every letter in the word."""
    assert len(character_to_look_for) == 1 
    i: int = 0
    word_len = int(len(word_being_searched))
    while i < word_len:
        if word_being_searched[i] == character_to_look_for:
            return True
        else:
            i += 1
    return False

# outputing different box emojis based on the user's guess and the secret word


def emojified(guess: str, secret: str) -> str:
    """Assigning different box emojis based on the user's guess and the secret word."""
    assert len(guess) == len(secret)
    index_of_the_word: int = 0
    box_emoji: str = ""
    length_of_guess = len(guess)

    while index_of_the_word < length_of_guess:
        if guess[index_of_the_word] == secret[index_of_the_word]:
            box_emoji += GREEN_BOX
        elif contains_char(secret, guess[index_of_the_word]):
            box_emoji += YELLOW_BOX
        else:
            box_emoji += WHITE_BOX
        index_of_the_word += 1
    return box_emoji

# making sure that user's input is the same length as the secret word


def input_guess(length_of_input: int) -> str:
    """Checks to see if the user's input is the same length as the secret word."""
    expected_length: str = (input(f"Enter a {length_of_input} character word: "))
    while len(expected_length) != length_of_input:
        expected_length = input(f"That wasn't {length_of_input} chars! Try again: ")
    return (expected_length)


if __name__ == "__main__":
    main()
