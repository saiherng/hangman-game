from random_word_generator import *

"""
Branch - bugfix-wincount
"""
class Hangman:

    def __init__(self):

        # generates random words
        self.word_generator = Random_Word_Generator()

        self.word = self.word_generator.random_word()

        # adds word into dictionary for easy access
        self.letter_list = {}
        self.construct_word()
        self.guessed = ["_"] * len(self.word)

        # score count to check win
        self.win_count = len(self.word)
        self.score = 0

        # error count for checking lose
        self.hangman = 10
        self.lose_count = 0

    def construct_word(self):

        for i in range(len(self.word)):

            if self.word[i] in self.letter_list:
                self.letter_list[self.word[i]].append(i)

            else:
                self.letter_list[self.word[i]] = [i]

    def letter_exists(self, l):

        if l in self.letter_list:

            for idx in self.letter_list[l]:
                self.guessed[idx] = l


            print("Good guess")

        else:
            print("Bad guess")
            self.lose_count += 1
            return False

    def get_preview(self):

        return self.guessed

    def isGameOver(self):

        if self.lose_count >= self.hangman:
            return True

        if self.score >= self.win_count:
            return True

        return False

    def isWin(self):

        if self.isGameOver() == True and self.score == self.win_count:
            return True

        return False


class Hangman_Game:

    def __init__(self):

        self.hangman = Hangman()


    def run(self):

        while not self.hangman.isGameOver():
            print(*self.hangman.get_preview(), sep=" ")
            print("Hangman Remaining: ", self.hangman.hangman - self.hangman.lose_count)

            guess = str(input("Enter your guess: "))
            self.hangman.letter_exists(guess)
            print()

        if self.hangman.isWin():
            print("You Won!")
        else:
            print("You Lose!")
            print("The word was", self.hangman.word)

        print("Thank you for playing")


game = Hangman_Game()
game.run()
