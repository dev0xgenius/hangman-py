from hangman import Hangman
from utils import get_char

def main():
    words = '''apple orange pineapple kiwi watermelon pawpaw carrot'''

    print('HANGMAN: Let the games begin!!!\n\
    Guess the letters of my random word')
    game = Hangman(words.split())
    gameActive = True
    
    while gameActive:
        print("Guess the letters")
       
        i = 1
        while i <= game.attempts:
            gameActive = not game.isguesscomplete()
            user_guess = get_char("")
            guessFound = game.find(user_guess)

            print(f"{i} guess(es) so far")
            print(f"Remaining guess(es): {game.attempts - i}")

            if game.isguesscomplete():
                print("You sneaky bastard, congratulations")
                print("You won =_7_7f7d=7s776<F6>yssh")
                print(f"So excited for you. WORD:{game.word}")
            elif guessFound:
                print(f"\nGreat, you found '{user_guess}'")
                print(f"@(position: {guessFound['pos'] + 1})")
                print(f"Updated: {game.guesses}")

                game.attempts += 1
            else:
                print("You're not correct!!!")
                print("Try Again")
            i += 1
    return 0

if __name__ == '__main__':
    main()
