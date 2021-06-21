import random

random_number = random.randint(0, 21)

wrong_guess = 0

while True:
    user_guess = input("Type a number between 0 and 20: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print(f"You guessed right!'\n'The correct answer is {random_number}!")
            print(f"You needed {wrong_guess} tries!")
            quit()
        elif user_guess > random_number:
            print("Your guess is too high! Try again")
            wrong_guess += 1
        elif user_guess < random_number:
            print("Your guess is too low! Try again")
            wrong_guess += 1
    else:
        print("Please type a number between 0 and 20!")
        continue
