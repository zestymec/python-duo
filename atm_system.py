print("Welcome to Smart ATM")

PIN = 1234
DAILY_LIMIT = 10000
MIN_BALANCE = 500

balance = 0

for attempt in range(3):
    pin = int(input("Enter your PIN: "))

    if pin == PIN:
        print("PIN verified successfully.")
        break

    print("Incorrect PIN. Attempts left:", 2 - attempt)
else:
    print("Too many incorrect PIN attempts. Card locked.")
    exit()

try:
    balance = int(input("Enter your starting balance: "))
except ValueError:
    print("Invalid balance. Defaulting to 0.")
    balance = 0

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("Current balance:", balance)
        if balance < MIN_BALANCE:
            print("Low balance warning")

    elif choice == "2":
        try:
            amount = int(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount. Please enter a whole number.")
            continue

        if amount <= 0:
            print("Invalid deposit amount")
        else:
            balance += amount
            print("Deposit successful")
            print("Updated balance:", balance)

    elif choice == "3":
        try:
            amount = int(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount. Please enter a whole number.")
            continue

        if amount <= 0:
            print("Invalid amount")
        elif amount > DAILY_LIMIT:
            print("Daily withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
            if balance < MIN_BALANCE:
                print("Low balance warning")
            else:
                print("Transaction successful")

    elif choice == "4":
        print("Thank you for using Smart ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
