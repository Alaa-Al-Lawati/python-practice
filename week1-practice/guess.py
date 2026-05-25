from random import randint

# Generate a random number between 1 and 100
number = randint(1, 100)

print("Hello, welcome to my guessing game")
print("Let's get started!")

found = False
count = 0

while not found:
    try:
        guess = int(input("Make your guess: "))
        count += 1  # Increment guess count

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("You found it!")
            print(f"You found the number {number} in {count} tries")
            found = True
    except ValueError:
        print("Please enter a valid integer.")
