secret_number = 6
guess = None
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_count += 1
    else:
        out_of_guesses = True