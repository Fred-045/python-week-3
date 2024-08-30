def calculate_discount(price, discount_percent):
    
    if discount_percent >= 25:
        # the discount amount
        discount_amount = price * (discount_percent / 100)
        # discount - original price
        final_price = price - discount_amount
        return final_price
    else:
    
        return price


original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# the final price
final_price = calculate_discount(original_price, discount_percent)


if final_price == original_price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
else:
    print(f"Discount applied. The final price is: ${final_price:.2f}")
    