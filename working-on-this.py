import random

# Let's teach the user to play the game
print("Welcome to the guesing game!")
print("Type in exit to leave the game anytime")

while True:
    number = random.randint(0, 9)
    print("I am thinking of a number between 0 and 9. Which number is it?")
    while True:
        user_guess = int(input("Your guess: "))
        if user_command == "exit":
            break
        else:
            if user_guess > number:
                print("Your guess is too high")
            elif user_guess < number:
                print("Your guess is too low")
            elif user_guess == number: 
                print("Yes that's the number!")
                break
            break