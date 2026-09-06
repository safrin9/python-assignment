name=input("Enter customer name: ")

product1 = input("\nEnter Product 1 name: ")
price1 = float(input(f"Enter price for {product1}: "))

product2 = input("\nEnter Product 2 name: ")
price2 = float(input(f"Enter price for {product2}: "))

product3 = input("\nEnter Product 3 name: ")
price3 = float(input(f"Enter price for {product3}: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000 and subtotal < 5000:
    discount_rate = 0.10
elif subtotal >= 1000 and subtotal < 3000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_total = subtotal - discount

print("\n\n--Shopping Summary--")
print(f"\nCustomer Name: {name}")
print(f"\nProduct 1: {product1}")
print(f"Price: {price1:.0f}")
print(f"\nProduct 2: {product2}")
print(f"Price: {price2:.0f}")
print(f"\nProduct 3: {product3}")
print(f"Price: {price3:.0f}")
print(f"\nSubtotal: {subtotal:.0f}")
print(f"Discount: {discount:.0f}")
print(f"Final Total: {final_total:.0f}")