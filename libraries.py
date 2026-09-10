import random
print("Welcome to the random number guessing game!")
user = int(input("enter a number between 1 and 999: "))
number = random.randint(1, 999)
print(f"The random number was: {number}")
if user == number:
    print("you win")
else:
    print("you lose")   

