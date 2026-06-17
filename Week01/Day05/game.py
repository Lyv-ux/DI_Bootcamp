import random

class Game:
    
    def get_user_item(self):
        while True:
            choice = input("Select an item (rock, paper, scissors): ").strip().lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            
            print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        
        user_wins = (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        )
        
        if user_wins:
            return "win"
        else:
            return "loss"

    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        
        result = self.get_game_result(user_choice, computer_choice)
        
        if result == "win":
            result_text = "You win!"
        elif result == "loss":
            result_text = "You lose"
        else:
            result_text = "You drew!"
            
        print(f"\nYou selected {user_choice}. The computer selected {computer_choice}. {result_text}\n")
        
        return result