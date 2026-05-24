from game import Game

def get_user_menu_choice():
    print("=== MAIN MENU ===")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    return choice

def print_results(results):
    print("\n===============================")
    print("        GAME SUMMARY           ")
    print("===============================")
    print(f"Wins   : {results['win']}")
    print(f"Losses : {results['loss']}")
    print(f"Draws  : {results['draw']}")
    print("===============================")
    print("Thank you for playing! See you soon! 👋✨\n")

def main():
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    print("Welcome to Rock, Paper, Scissors!\n")
    
    while True:
        menu_choice = get_user_menu_choice()
        
        if menu_choice == "1":
            current_game = Game()
            game_result = current_game.play()
            scores[game_result] += 1
            
        elif menu_choice == "2":
            print_results(scores)
            
        elif menu_choice == "3":
            print_results(scores)
            break
            
        else:
            print("\n❌ Invalid choice! Please select 1, 2, or 3.\n")

# Lancement du programme principal
if __name__ == "__main__":
    main()