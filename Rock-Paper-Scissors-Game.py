# Simple rock paper scissors game 
import random
# Taking input
def get_user_choice():
    choice = input("Hey enter your choice buddy (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Nope!your choice is invalid(Check the spelling properly). Please choose between rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("cograts You win buddy!")
    else:
        print("he he! I(Computer) wins!")

def play_again():
    play_more = input("Hey buddy do you want to play another round with me ? (yes or no): ").lower()
    return play_more == "yes"

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        if not play_again():
            break

if __name__ == "__main__":
    main()
