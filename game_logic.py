import random
from ascii_art import STAGES



#############################
# Constants
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
# Tries
STAGE_COUNT = len(STAGES) -1
START_LIVES = STAGE_COUNT #so adding new stages automaticlly changes the stage


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def get_letter(chosen_letters: list[str]):
    '''
    Get's a single Character (Lower Case). Rejects any other Input.
    Check'S also if the Letter was already chosen and rejects these too
    :return: str -> The Letter in Lower Case
    '''
    letter = ""
    while letter == "":
        letter = input("Guess a letter: ")
        if not letter.isalpha() or len(letter) > 1:
            print("please only a single letter (a..z)")
            letter = ""
        if letter in chosen_letters:
            print(f"{letter} was already tried! Chose a different letter!")
            letter = ""
    return letter.lower()

def check_letter(word: str, guess: str)->bool:
    ''''''
    return guess in word

def check_won_or_lost(word: str, chosen_letters: list[str])->bool:
    '''
    Returns True if all letters in word exist in chosen_letters
    :param word: str -> The word to find
    :param chosen_letters: list[str] -> List of every Letter chosen till now
    :return: bool -> True if all letters in word exist in chosen_letters, False otherwise
    '''
    return all (letter in chosen_letters for letter in word)

def print_snowman(stage: int)->None:
    '''The Snowman. If changed, it is easier to manage'''
    print()
    print(STAGES[stage])
    print()

def dotted_line(word: str, chosen_letters: list[str])->str:
    '''
    Creates the dotted Line
    :param word: str -> The word to resolve
    :param chosen_letters: list[str] -> List of every Letter chosen till now
    :return: str -> The Dotted Line
    '''
    dotline = ""
    for letter in word:
        dotline += " _" if letter not in chosen_letters else f" {letter}"
    dotline = "Word:\t" + dotline
    return dotline


def play_game():
    '''Main Function for One Round of Melting Snowman'''

    # initializing the Variables
    stage: int = 0
    chosen_letters = []
    secret_word = get_random_word()

    # doing the Game
    while stage < STAGE_COUNT:
        print_snowman(stage)
        print(dotted_line(secret_word, chosen_letters))
        guess = get_letter(chosen_letters)
        chosen_letters.append(guess)
        # reduce Tries???
        stage += 1 if not check_letter(secret_word, guess) else 0
        # checking if Gamne won or lost
        if check_won_or_lost(secret_word, chosen_letters):
            print_snowman(stage)
            print(dotted_line(secret_word, chosen_letters))
            print("Congratulations, you saved the snowman!\n")
            break
        elif stage == STAGE_COUNT:
            print_snowman(stage)
            print(f"You lost! Game over! The secret_word was: {secret_word}\n")
            break

