import random
import utils

class Hangman():
    """For Managing HANGMAN Game"""
    def __init__(self, words):
        self.word = random.choice(words)
        self.attempts = len(self.word)
        self.guesses = ['_' for i in range(self.attempts)]
        self.track_word = self.word[:]
        
    def isguesscomplete(self):
        return utils.join(self.guesses) == self.word
        
    def find(self, guessed_letter):
        guessed_letter = guessed_letter.lower()
        
        if guessed_letter in self.track_word:
            letter_pos = self.track_word.find(guessed_letter)
            self.guesses[letter_pos] = guessed_letter
            self.track_word = utils.swapchar(self.track_word, letter_pos, '_')
            
            return {'pos' : letter_pos, 'updatedGuesses' : self.guesses}
        return False
        
    def end(self):
        print("You won, crazy!!!")