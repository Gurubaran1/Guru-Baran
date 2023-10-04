cart = {
    "apple": {"price": 0.5, "quantity": 2},
    "banana": {"price": 0.3, "quantity": 3},
    "orange": {"price": 0.6, "quantity": 1},
    "grapes": {"price": 1.0, "quantity": 4}
}


def update_product(cart, product_name, new_quantity):
    if product_name in cart:
        cart[product_name]["quantity"] = new_quantity
        print(f"{product_name} quantity updated to {new_quantity} in the cart.")
    else:
        print(f"{product_name} not found in the cart.")


def remove_product(cart, product_name):
    if product_name in cart:
        del cart[product_name]
        print(f"{product_name} removed from the cart.")
    else:
        print(f"{product_name} not found in the cart.")


def calculate_total(cart):
    total = 0
    for product, details in cart.items():
        total += details["price"] * details["quantity"]
    return total


print("Original Cart:\n", cart)
update_product(cart, "apple", 5)
remove_product(cart, "banana")
print("\nUpdated Cart:\n", cart)

total_bill = calculate_total(cart)
print("\nTotal Bill: $", total_bill)
