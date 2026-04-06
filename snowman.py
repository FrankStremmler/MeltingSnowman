'''
The melting Snowman is a Hangman-Clone
'''
import random

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

def check_letter(word: str, guess: str)->bool:
    ''''''
    return guess in word

def check_won_or_lost(word: str, chosen_letters: list[str])->bool:
    '''
    Returns if all letters in word exist in chosen_letters
    :param word: str -> The word to resolve
    :param chosen_letters: list[str] -> List of every Letter chosen till now
    :return: bool -> True if all letters in word exist in chosen_letters, False otherwise
    '''
    for letter in word:
        if letter not in chosen_letters:
            return False
    return True

def get_letter():
    '''
    Get's a single Character (Lower Case). Rejects any other Input.
    :return: str -> The Letter in Lower Case
    '''
    letter = ""
    while not letter.isalpha():
        letter = input("Guess a letter: ")
        if not letter.isalpha() or len(letter) > 1:
            print("please only a single letter (a..z)")
    return letter.lower()


def play_game():
    '''Main Function for the Game'''
    # print the Title
    print("\nWelcome to Snowman Meltdown!")
#    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # initializing the Variables
    tries: int = START_TRIES
    chosen_letters = []
    secret_word = get_random_word()

    # doing the Game
    while tries > 0:
        print_snowman(tries)
        print(dotted_line(secret_word, chosen_letters))
        guess = get_letter()
        chosen_letters.append(guess)
        # reduce Tries???
        tries -= 1 if not check_letter(secret_word, guess) else
        # checking if Gamne won or lost
        if check_won_or_lost(secret_word, chosen_letters):
            print_snowman(tries)
            print(dotted_line(secret_word, chosen_letters))
            print("Congratulations, you saved the snowman!\n")
            break
        elif tries == 0:
            print_snowman(tries)
            print(f"You lost! Game over! The secret_word was: {secret_word}\n")
            break

if __name__ == "__main__":
    play_game()