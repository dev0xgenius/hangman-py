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
        gameActive = not game.isguesscomplete()
        
        for i in range(game.attempts):
            user_guess = get_char("")
            guessFound = game.find(user_guess)
            if guessFound:
                print(f"Great, you found '{user_guess}'")
                print(f" @(position: {guessFound['pos'] + 1})")
                print(f"Updated: {guessFound['updatedGuesses']}")
                game.attempts += 1
            else:
                print("Wrong!!!")
        
        gameActive = False
            
    return 0

if __name__ == '__main__':
    main()