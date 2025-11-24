secret_number = 6
guess = None
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        try:
            guess = int(input("Guess the number between 1 to 10: "))
        except ValueError:
            print("Please enter a number.")
            continue
        guess_count += 1
    else:
        out_of_guesses = True
        