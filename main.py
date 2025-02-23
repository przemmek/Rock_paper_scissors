from enum import Enum
import random

class Shape(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    
class Player:
    def __init__(self):
        self.score = 0
        self.shapes = [Shape.PAPER.name, Shape.ROCK.name, Shape.SCISSORS.name]
        self.name = "Player"
        
    def choose(self):
        while True:
            user_input = input("Please enter your choice (rock, paper, scissors): ").upper()
            if (user_input in self.shapes):
                print(f"Player choose: {user_input}")
                return user_input
            print("Invalid option. Please try again (rock, paper, scissors)")

class Computer:
    def __init__(self):
        self.score = 0
        self.shapes = [Shape.PAPER.name, Shape.ROCK.name, Shape.SCISSORS.name]
        self.name = "Computer"
        
    def choose(self):
        choice = random.choice(self.shapes)
        print(f"Computer choose: {choice}")
        return choice
    
        
class Game:
    def __init__(self):
        self.max_round =  3
        self.round = 0
        self.computer = Computer()
        self.player = Player()
        
    def play(self):
        while (self.round < self.max_round):
            player_choice = self.player.choose()
            computer_choice = self.computer.choose()
            self.adjust_score(computer_choice, player_choice)
            self.display_score()
        winner = self.determine_winner()
        print(f"{winner} WON!")
            
    def adjust_score(self, computer_choice, player_choice):
        if (computer_choice == player_choice):
                return
        if ((computer_choice == Shape.ROCK.name and player_choice == Shape.SCISSORS.name) or \
            (computer_choice == Shape.PAPER.name and player_choice == Shape.ROCK.name) or \
            (computer_choice == Shape.SCISSORS.name and player_choice == Shape.PAPER.name)):
            self.computer.score += 1
        else:
            self.player.score += 1
        self.round +=1
            
    def determine_winner(self):
            if (self.computer.score > self.player.score):
                return self.computer.name
            else:
                return self.player.name
            
    def display_score(self):
            print(f"{self.player.name} score: {self.player.score}")
            print(f"{self.computer.name} score: {self.computer.score}")
            
              
if __name__ == "__main__":
    game = Game()
    game.play()