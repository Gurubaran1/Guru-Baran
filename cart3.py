class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_item_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product, quantity):
        cart_item = CartItem(product, quantity)
        self.cart_items.append(cart_item)

    def update_item_quantity(self, product_id, new_quantity):
        for item in self.cart_items:
            if item.product.product_id == product_id:
                item.quantity = new_quantity
                return True
        return False 

    def remove_item(self, product_id):
        for item in self.cart_items:
            if item.product.product_id == product_id:
                self.cart_items.remove(item)
                return True
        return False 

    def calculate_total_price(self):
        total_price = 0
        for item in self.cart_items:
            total_price += item.calculate_item_price()
        return total_price



product1 = Product(1, "mango", 20.0)
product2 = Product(2, "apple", 30.0)
product3 = Product(3, "pineapple", 40.0)
product4 = Product(4, "orange", 45.0)

cart = Cart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 4)
cart.add_item(product4, 3)

cart.update_item_quantity(1, 3)

cart.remove_item(1)

total_price = cart.calculate_total_price()

print("Products in Cart:")
for item in cart.cart_items:
    print(f"Product ID: {item.product.product_id}, Name: {item.product.product_name}, "
          f"Price: {item.product.price}, Quantity: {item.quantity}")

print(f"Total Price: {total_price}")
