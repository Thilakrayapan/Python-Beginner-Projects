import random
choice = ('r','p','s')
choices = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}

while True:
    user_choice = input("Enter rock paper scissors (r/p/s): ").lower()
    computer_choice = random.choice(choice)
    
    print(f"User_choice: {choices[user_choice]}\nComputer_choice: {choices[computer_choice]}")
    
    if user_choice not in choice:
        print('Invalid Choice!')
        
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
        
    should_continue = input("If you continue (y/n): ").lower()
    if should_continue == 'n':
        break
    
        
    


    