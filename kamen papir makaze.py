import random

print("Let's play Rock-Paper-Scissors!")
print("The rules are: rock beats scissors, paper beats rock, and scissors beat paper.")
print("")

choices = ["rock", "paper", "scissors"]
play_again = True

while play_again:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please choose again.")
        continue
    
    print("You chose: " + user_choice)
    print("The computer chose: " + computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock") \
        or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    play_again_input = input("Do you want to play again? (y/n): ").lower()
    if play_again_input == "n":
        play_again = False

print("Thanks for playing!")
