class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.id in self.products:
            self.products[product.id]['quantity'] += product.quantity
        else:
            self.products[product.id] = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity
            }

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def check_stock(self, product_id):
        return self.products.get(product_id, {}).get('quantity', 0) > 0
