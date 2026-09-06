print("welcome to the tip calculator.")
bill = float(input("what was the total bill?"))
tip = int(input("what percentage tip would you like to give?"))
people = int(input("how much people split the bill?"))
tip_amount = bill* (tip / 100) + bill
print(tip_amount)