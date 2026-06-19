import random

# In python Captial letters are indicates that are constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

choices = {
    ROCK:'Rock',
    PAPER:'Paper',
    SCISSORS:'Scissors'
}

choice = tuple(choices.keys())

def get_user_choice():
    while True:
        user_choice = input("Enter rock paper scissors (r/p/s): ").lower()
        if user_choice in choice:
            return user_choice
        else:
            print("Invalid choice")

def display_choices(user_choice, computer_choice):
        print(f"User_choice: {choices[user_choice]}\nComputer_choice: {choices[computer_choice]}")
     
def display_result(user_choice, computer_choice):
    if user_choice == computer_choice:
            print("Result: Tie")   
    elif (
      (user_choice == ROCK and computer_choice == SCISSORS) or
      (user_choice == SCISSORS and computer_choice == PAPER) or
      (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("Result: You Win")   
    else:
        print("Result: You Lost")
def play_game():   
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choice)
    
        display_choices(user_choice, computer_choice)    
        display_result(user_choice, computer_choice)  
   
        should_continue = input("If you continue (y/n): ").lower()
        if should_continue == 'n':
            print("'-' Thank You for Palying!")
            break
        
play_game()