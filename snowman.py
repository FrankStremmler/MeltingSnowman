'''
The melting Snowman is a Hangman-Clone
This is the main file, where the game is started and the main loop is running.
Each round and so the whole game-logic is an game_logic.py.
The ascii art for the snowman is in ascii_art.py.
'''
from game_logic import play_game


def main():
    print("Welcome to Snowman Meltdown!")
    while True:
        play_game()
        letter = input("Press Enter to play again... ('q'uit to exit) ")
        if letter.lower().strip() in ["quit", "q"]:
            break
    print("Thank you for playing MELTING SNOWMAN! Goodbye!")


if __name__ == "__main__":
    main()
