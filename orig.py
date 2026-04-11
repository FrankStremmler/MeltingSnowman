
from ascii_art import STAGES
from game_logic import WORDS, get_random_word, check_letter, check_won_or_lost, play_game


def print_snowman(lives: int)->None:
    # redo stages und STAGES[]
    '''The Snowman. If changed, it is easier to manage'''
    print()
    print_snow_hat()
    print_snow_body(lives)
    print()

def main():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    while True:
        play_game()

    print("Secret word selected: " + secret_word)  # for testing, later remove this line


    while lives > 0:

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)

if __name__ == "__main__":
    main