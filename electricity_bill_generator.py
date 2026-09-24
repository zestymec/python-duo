print("welcome to electricity bill calculator")
name = input("Enter your name: ")
unit = int(input("Enter your electricity bill: "))
if unit < 0:
    print("Invalid input. Please enter a non-negative number for units.")
elif unit <= 100:
    bill = unit * 15
elif unit <= 200:
    bill = (100 * 15) + (unit - 100) * 20
elif unit <= 300:
    bill = (100 * 15) + (100 * 20) + (unit - 200) * 25
else:
    bill = (100 * 15) + (100 * 20) + (100 * 25) + (unit - 300) * 30
print("hello", name, "your electricity bill is", bill)    