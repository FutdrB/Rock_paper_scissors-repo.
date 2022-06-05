import random

while True:
    choices = ["r","p","s"]

    computer = random.choice(choices)
    user = None

    while user not in choices:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    if user == computer:
        print("computer: ",computer)
        print("player: ",user)
        print("Tie!")

    elif user == "r":
        if computer == "p":
            print("computer: ", computer)
            print("player: ", user)
            print("You lose!")
        if computer == "s":
            print("computer: ", computer)
            print("player: ", user)
            print("You win!")

    elif user == "s":
        if computer == "r":
            print("computer: ", computer)
            print("player: ", user)
            print("You lose!")
        if computer == "p":
            print("computer: ", computer)
            print("player: ", user)
            print("You win!")

    elif user == "p":
        if computer == "s":
            print("computer: ", computer)
            print("player: ", user)
            print("You lose!")
        if computer == "r":
            print("computer: ", computer)
            print("player: ", user)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Thank you and Goodbye!")
