import random

def guess_the_number_game():
    print("Hello! What is your name?")
    name = input()

    print("Well,", name, "I am thinking of a number between 1 and 20.")

    rand_num = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        user_guess = int(input())
        guesses += 1

        if user_guess < rand_num:
            print("Your guess is too low.")
        elif user_guess > rand_num:
            print("Your guess is too high.")
        else: 
            print("Good job,", name,"! You guessed my number in", guesses, "guesses!")
            break

guess_the_number_game()