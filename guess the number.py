secret_number = 7
number_of_guesses = 0
guess_limit = 3

while number_of_guesses < guess_limit:
    guess = int(input("guess a number : "))
    number_of_guesses += 1
    if guess == secret_number:
        print("YOU WON!")
        break

else:
        print("YOU LOST BETTER LUCK NEXT TIME!")

    