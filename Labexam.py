products = {
    101: {"name": "Laptop", "price": 999, "stock": 45},
    102: {"name": "Smartphone", "price": 500, "stock": 20},
    103: {"name": "Tablet", "price": 300, "stock": 15},
    104: {"name": "Headphones", "price": 100, "stock": 30},
    105: {"name": "Smartwatch", "price": 200, "stock": 25}
}

# Adding items to the cart
cart = {}
cart[101] = 1
cart[102] = 2
cart[103] = 1

# Unique cart product IDs
product_ids = set(cart.keys())
print("Unique Product IDs:", product_ids)

# Products exceeding stock limit
exceeding_stock_limit = {
    product_id: details
    for product_id, details in products.items()
    if details["stock"] > 50
}
print("Products exceeding stock limit:", exceeding_stock_limit)

# Calculating total
total = sum(
    products[product_id]["price"] * quantity
    for product_id, quantity in cart.items()
)

# Applying discount
if total < 1000:
    discount_percentage = 0
elif total <= 2999:
    discount_percentage = 5
else:
    discount_percentage = 10

discount = total * discount_percentage / 100
total_discount = total - discount

# Adding GST
gst_percentage = 18
gst = total_discount * gst_percentage / 100
total_with_gst = total_discount + gst

# Printing itemized bill
print("\nItemized Bill:")

for product_id, quantity in cart.items():
    product_name = products[product_id]["name"]
    product_price = products[product_id]["price"]
    item_total = product_price * quantity

    print(product_name, "x", quantity, "=", item_total)

print("Subtotal:", total)
print("Discount:", discount)
print("Total after discount:", total_discount)
print("GST:", gst)
print("Final Total:", total_with_gst)