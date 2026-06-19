import random
choice = ('r','p','s')
choices = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}
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
      (user_choice == 'r' and computer_choice == 's') or
      (user_choice == 's' and computer_choice == 'p') or
      (user_choice == 'p' and computer_choice == 'r')
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
            break
        
play_game()