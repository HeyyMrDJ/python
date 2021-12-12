# Project 1 - Rock, Paper, Scissors
import random

# Function to check player/computer inputs
def check_input(user_input, computer_input):

    # Display user and computer decissions
    print(f"\nComputer decission was: {computer_input.title()}")
    print(f"User decission was: {user_input.title()}")

    # Rock
    if user_input == 'Rock' and computer_input == 'Rock':
        game_over('Tie')
    if user_input == 'Rock' and computer_input == 'Paper':
        game_over('Lose')
    if user_input == 'Rock' and computer_input == 'Scissors':
        game_over('Win')

    # Paper
    if user_input == 'Paper' and computer_input == 'Rock':
        game_over('Win')
    if user_input == 'Paper' and computer_input == 'Paper':
        game_over('Tie')
    if user_input == 'Paper' and computer_input == 'Scissors':
        game_over('Lose')
    
    # Scissors
    if user_input == 'Scissors' and computer_input == 'Rock':
        game_over('Lose')
    if user_input == 'Scissors' and computer_input == 'Paper':
        game_over('Win')
    if user_input == 'Scissors' and computer_input == 'Scissors':
        game_over('Tie')

# Function to display results
def game_over(result):
    print("\n")
    if result == 'Tie':
        print("\tTied game!")
    if result == 'Win':
        print("\tYou Win!")
    if result == 'Lose':
        print("\tYou Lose!")
    print("\n")

# Function to print welcome screen
def game_intro():
    print("""
    WELCOME TO ROCK, PAPER, SCISSORS!!!

    \tROCK > SCISSORS
    \tPAPER > ROCK
    \tSCISSORS > PAPER
    """)

# Function to get and validate user input
def get_user_input():
    user_input = ""
    while user_input not in ['Rock', 'Paper', 'Scissors']:
        user_input = input("Enter Your choice: Rock, Paper, or Scissors\n").title()
    return user_input

# Display welcome screen
game_intro()

# Ask user for input
user_input = get_user_input()

# Randomly generate computer answer
computer_input = random.choice(['Rock', 'Paper', 'Scissors'])

# Compare user input with computer answer
check_input(user_input, computer_input)