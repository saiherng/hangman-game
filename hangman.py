from random_word_generator import *

"""
Branch - bugfix-wincount

Bug 1 (fixed): not winning
Bug 2 : max score count causes false win
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
        self.score = 0

        # error count for checking lose
        self.max_error = 10
        self.lose_count = 0

    def construct_word(self, letter_list ):

        for i in range(len(self.word)):

            if self.word[i] in letter_list:
                letter_list[self.word[i]].append(i)

            else:
                letter_list[self.word[i]] = [i]

    def letter_exists(self, l):

        if l in self.letter_list:
            for idx in self.letter_list[l]:
                self.guessed[idx] = l
                self.score += 1
            print("Good guess")

        else:
            print("Bad guess")
            self.lose_count += 1
            return False

    def get_preview(self):

        return self.guessed



    def isGameOver(self):

        if self.lose_count >= self.max_error:
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
            print("Hangman Remaining: ", self.hangman.max_error - self.hangman.lose_count)

            guess = str(input("Enter your guess: "))
            self.hangman.letter_exists(guess)
            print()
            print(self.hangman.letter_list)

        if self.hangman.isWin():
            print("You Won!")
        else:
            print("You Lose!")
            print("The word was", self.hangman.word)

        print("Thank you for playing")


game = Hangman_Game()
game.run()
