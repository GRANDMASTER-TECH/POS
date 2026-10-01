class Billing:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.cart)
        return total

    def process_payment(self, amount_paid):
        total = self.calculate_total()
        if amount_paid < total:
            raise ValueError("Insufficient payment.")
        change = amount_paid - total
        self.cart.clear()  # Clear the cart after payment
        return change
