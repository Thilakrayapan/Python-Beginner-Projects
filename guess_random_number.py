import random

number_to_guess = random.randint(1,100)
while True:
    
    try:
        user_input = int(input("Enter a number between 1 to 100: "))
        
        if user_input > number_to_guess:
            print("Too High!")
        elif user_input < number_to_guess:
            print("Too Low!")
        else:
            print("Congulations! You guess the numeber ")
            break
    except ValueError:
        print("Please Enter a valid number.")
        