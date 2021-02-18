from random_word_generator import *

"""
Branch - bugfix-wincount

Bug 1 (fixed): not winning
Bug 2 (fixed): max score count causes false win


"""


class Hangman:

    def __init__(self):

        # generates random words
        self.generator = Random_Word_Generator()
        self.word = self.generator.random_word()

        # adds word into dictionary for easy access
        self.letter_list = {}

        self.construct_word(self.letter_list)
        self.guessed = ["_"] * len(self.word)

        # score count to check win
        self.win_count = len(self.word)

        # error count for checking lose
        self.max_error = 10
        self.lose_count = 0

    def construct_word(self, letter_list):

        for i in range(len(self.word)):

            if self.word[i] in letter_list:
                letter_list[self.word[i]].append(i)

            else:
                letter_list[self.word[i]] = [i]

    def letter_exists(self, l):

        if l in self.letter_list:
            for idx in self.letter_list[l]:
                self.guessed[idx] = l
            return True

        else:

            self.lose_count += 1
            return False

    def get_score(self):

        score = 0
        for guess in self.guessed:
            if guess != "_":
                score += 1

        return score

    def get_preview(self):

        return self.guessed

    def isGameOver(self):

        if self.lose_count >= self.max_error:
            return True

        if self.get_score() >= self.win_count:
            return True

        return False

    def isWin(self):

        if self.isGameOver() == True and self.get_score() == self.win_count:
            return True

        return False


class Hangman_Game:

    def __init__(self):

        self.hangman = Hangman()

    def run(self):

        message = ""
        while not self.hangman.isGameOver():
            print("[", *self.hangman.get_preview(), "]", sep=" ")
            print("[Hangman Remaining:", self.hangman.max_error -
                  self.hangman.lose_count, "]", message)

            guess = str(input("Enter your guess: "))
            if guess.isalpha():
                exists = self.hangman.letter_exists(guess)
                if exists:
                    message = ", Good Guess!"
                else:
                    message = ", Bad Guess!"
                print()
            else:
                message = ", Only letters are allowed!"

        print("The word was", self.hangman.word)

        if self.hangman.isWin():
            print("You Won!")
        else:
            print("You Lose!")
        print()
        print("Thank you for playing")


game = Hangman_Game()
game.run()
