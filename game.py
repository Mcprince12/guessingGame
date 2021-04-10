number = int(input("Guess a number (Between 1 & 10)"))
if (number == 7):
    print("Congratulations! You guessed the right number!")
elif (number < 7):
    print("Your guess is too low, try again!")
else:
    print("Your guess is too high, try again!")
