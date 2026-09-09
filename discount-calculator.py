print("welcome to the discount calculator")
customer_bill = float(input("original amount: "))
discount = float(input("discount:"))
discount_amount= customer_bill * (discount / 100)
final_price = customer_bill - discount_amount
print(discount_amount)
print(final_price)
