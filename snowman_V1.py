'''
The melting Snowman is a Hangman-Clone
'''
import random

from ascii_art import STAGES
from game_logic import play_game



#############################
# CONSTANTS
# The Snowwman
SNOW_HAT = [" ___ ", "/---\\"]
SNOW_BODY = ["(o o)", "( : )", "( : )"]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# others
START_TRIES = 3


#############################
# FUNCTIONS
def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def print_snow_hat()->None:
    '''The Hat of the Snowman'''
    for line in range(len(SNOW_HAT)):
        print(f"\t{SNOW_HAT[line]}")

def print_snow_body(lines: int)->None:
    '''The Body of the Snowman'''
    for line in range(lines):
        print(f"\t{SNOW_BODY[line]}")

def print_snowman(lines: int)->None:
    '''The Snowman. If changed, it is easier to manage'''
    print()
    print_snow_hat()
    print_snow_body(lines)
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


if __name__ == "__main__":
    play_game()