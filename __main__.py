from hangman import Hangman
from utils import get_char

def main():
    words = '''apple orange pineapple kiwi watermelon pawpaw carrot 
    house kitchen mouse cat dog dogma crazy hydrogen kryptonite knack
    imbecile dangerous kitten amoeba titanium emerald obscure janitor
    '''

    welcome_message = "HANGMAN: Let the games begin!!!"
    welcome_message += " Guess the letters of my random word"
    
    print(welcome_message)
    gameActive = True

    while gameActive:
        print("Guess the letters")
        game = Hangman(words.split())
       
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
                print(f"So excited for you. WORD:{game.word.upper()}")
                game.attempts = 0
                gameActive = False
            elif guessFound:
                print(f"\nGreat, you found '{user_guess}'")
                print(f"@(position: {guessFound['pos'] + 1})")
                print(f"Updated Guesses: {game.guesses}")
                game.attempts += 1
            else:
                print("You're wrong!! Try Again")
            i += 1

        user_option = get_char("Do you want to play again?", ["y", "n"])
        if user_option == 'n':
            break
        else:
            gameActive = True
    return 0

if __name__ == '__main__':
    main()
