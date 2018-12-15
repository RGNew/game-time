import random
import string

play_again = "yes"

while(play_again == "yes"):
    remaining_attempts = 3
    random_number = random.randint(1,10)
    #print(f"The random number is: {random_number} \n")  # Testing purposes to ensure win condition works.
    correct = False

    print("In this game, you will be asked to guess a random number. You will have 3 attempts to do so. \n")
    while(remaining_attempts > 0 and correct == False):
        
        guessed_number = int(input("Please select a number between 1 and 10."))

        if(guessed_number == random_number):
            correct = True
            print("That is correct! You won the game! \n")
        else:
            remaining_attempts -= 1
            print(f"That's incorrect. Remaining attempts: {remaining_attempts} \n")

    if (correct == False):
        print("You lost. \n")
    else:
        print("You won! \n")   

    play_again = input("Would you like to play again? Please enter 'yes' or 'no'. \n").lower()

print("Thanks for playing! \n")