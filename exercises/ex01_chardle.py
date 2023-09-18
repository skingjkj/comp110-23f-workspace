"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730665331"

enter_a_five_character_word: str = input("Enter a 5-character word: ")

if len(enter_a_five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
 
enter_a_single_character: str = input("Enter a single character: ")

if len(enter_a_single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

counting_matching_characters: int = 0


print("Searching for " + enter_a_single_character + " in " + enter_a_five_character_word)

if enter_a_single_character == enter_a_five_character_word[0]:
    print(enter_a_single_character + " found at index 0")
    counting_matching_characters += 1
if enter_a_single_character == enter_a_five_character_word[1]:
    print(enter_a_single_character + " found at index 1")
    counting_matching_characters += 1
if enter_a_single_character == enter_a_five_character_word[2]:
    print(enter_a_single_character + " found at index 2")
    counting_matching_characters += 1
if enter_a_single_character == enter_a_five_character_word[3]:
    print(enter_a_single_character + " found at index 3")
    counting_matching_characters += 1
if enter_a_single_character == enter_a_five_character_word[4]:
    print(enter_a_single_character + " found at index 4")
    counting_matching_characters += 1

if counting_matching_characters == 0:
    print("No instances of " + enter_a_single_character + " found in " + enter_a_five_character_word)

elif counting_matching_characters == 1:
    print(str(counting_matching_characters) + " instance of " + enter_a_single_character + " found in " + enter_a_five_character_word)
else:
    print(str(counting_matching_characters) + " instances of " + enter_a_single_character + " found in " + enter_a_five_character_word)
