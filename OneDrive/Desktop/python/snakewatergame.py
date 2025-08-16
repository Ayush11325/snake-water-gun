import random

def snake_water_game():
    choices = ['snake', 'water', 'gun']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (snake/water/gun) or 'exit' to quit: ").lower()
        if user_choice == 'exit':
            print("Game Over!")
            break
        if user_choice not in choices: 
            print("Invalid choice! Please choose from snake, water, or gun.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'snake' and computer_choice == 'water') or \
             (user_choice == 'water' and computer_choice == 'gun') or \
             (user_choice == 'gun' and computer_choice == 'snake'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")


snake_water_game()
