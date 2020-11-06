

class Hangman:

    def __init__(self):

        self.word = "photocopy"
        self.letter_list = {}
        
        self.guessed = ["_"] * len(self.word)

        self.win_count = len(self.word)
        self.score = 0

        self.hangman = 6
        self.lose_count = 0
        

    def generate_word(self):

        for i in range(len(self.word)):
            
            if self.word[i] in self.letter_list:
                self.letter_list[self.word[i]].append(i)

            else:
                self.letter_list[self.word[i]] = [i]


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


        if self.lose_count > self.hangman:
            return True

        if self.score > self.win_count:
            return True
        
        return False

game = Hangman()

game.generate_word()

class Hangman_Game:


    def __init__(self):

        self.hangman = Hangman()
    
    def run(self):

        while not self.hangman.isGameOver():

            print(*self.hangman.get_preview(), sep=" ")
            print("Hangman Remaining: ", 6 - self.hangman.lose_count)

            guess = str(input("Enter your guess: "))
            self.hangman.letter_exists(guess)
            

        print("Thank you for playing")



game = Hangman_Game()
game.run()

