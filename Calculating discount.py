def discount(t, e):
    result = t
    if e >= 0:
        dis = (e / 100) * t
        result = t - dis
    return result

price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = discount(price, discount_percent)
print(f"The final price after discount is: {final_price:.2f}")
