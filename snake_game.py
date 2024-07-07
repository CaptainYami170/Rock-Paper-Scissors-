import random

# Function to play the game
def play_game():
    computer = random.choice([1, 2, 3])
    youstr = input('Enter "r", "p", or "s" (or "q" to quit): ')

    # Valid inputs
    valid_inputs = {"r": 1, "p": 2, "s": 3}
    reversedictionary = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

    # Check if the user wants to quit
    if youstr == "q":
        print("Thanks for playing! Goodbye!")
        return False

    # Check if the input is valid
    if youstr in valid_inputs:
        you = valid_inputs[youstr]
        print(f"You chose {reversedictionary[you]}\nComputer chose {reversedictionary[computer]}")
        
        if computer == you:
            print("It's a draw!")
        else:
            if (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
                print("You WIN!")
            else:
                print("You LOSE!")
    else:
        print("Something went wrong!")

    return True

# Main loop to keep playing
while True:
    if not play_game():
        break
