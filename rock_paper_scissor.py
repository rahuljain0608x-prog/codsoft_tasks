# ==========================================
# Rock Paper Scissors Game
# Internship Project
# Developed in Python
# ==========================================

import random

# Available choices
choices = ["rock", "paper", "scissors"]

# Score variables
user_score = 0
computer_score = 0
ties = 0

print("=" * 50)
print("      ROCK PAPER SCISSORS GAME")
print("=" * 50)
print("Instructions:")
print("1. Choose Rock, Paper, or Scissors.")
print("2. The computer will also make a choice.")
print("3. Winner will be decided based on game rules.")
print("4. Type 'exit' anytime to quit the game.")
print("=" * 50)

while True:

    # User input
    user_choice = input("\nEnter your choice (Rock/Paper/Scissors): ").lower()

    # Exit option
    if user_choice == "exit":
        break

    # Input validation
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("\nYour Choice     :", user_choice.capitalize())
    print("Computer Choice :", computer_choice.capitalize())

    # Game Logic
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
        ties += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 Congratulations! You Win!")
        user_score += 1

    else:
        print("😔 Computer Wins!")
        computer_score += 1

    # Display Score
    print("\n---------- SCOREBOARD ----------")
    print(f"You       : {user_score}")
    print(f"Computer  : {computer_score}")
    print(f"Ties      : {ties}")
    print("--------------------------------")

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again not in ["yes", "y"]:
        break

# Final Result
print("\n" + "=" * 50)
print("              GAME OVER")
print("=" * 50)

print(f"Your Score      : {user_score}")
print(f"Computer Score  : {computer_score}")
print(f"Ties            : {ties}")

if user_score > computer_score:
    print("\n🏆 Overall Winner: You!")
elif computer_score > user_score:
    print("\n💻 Overall Winner: Computer!")
else:
    print("\n🤝 Overall Result: Match Tied!")

print("\nThank you for playing!")
print("=" * 50)