# FILE: /point-of-sale-system/point-of-sale-system/src/main.py
from models.product import Product
from services.billing import Billing
from services.inventory import Inventory
from utils.helpers import format_currency, validate_input

def main():
    inventory = Inventory()
    billing = Billing()
    
    while True:
        print("Welcome to the Point of Sale System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Check Stock")
        print("4. Process Sale")
        print("5. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(id=len(inventory.products) + 1, name=name, price=price, quantity=quantity)
            inventory.add_product(product)
            print(f"Product {name} added to inventory.")
        
        elif choice == '2':
            product_id = int(input("Enter product ID to remove: "))
            inventory.remove_product(product_id)
            print(f"Product ID {product_id} removed from inventory.")
        
        elif choice == '3':
            product_id = int(input("Enter product ID to check stock: "))
            stock = inventory.check_stock(product_id)
            print(f"Product ID {product_id} has {stock} in stock.")
        
        elif choice == '4':
            cart = []
            while True:
                product_id = int(input("Enter product ID to add to cart (0 to finish): "))
                if product_id == 0:
                    break
                quantity = int(input("Enter quantity: "))
                cart.append((product_id, quantity))
            total = billing.calculate_total(cart, inventory)
            print(f"Total amount due: {format_currency(total)}")
            payment = float(input("Enter payment amount: "))
            billing.process_payment(payment, total)
        
        elif choice == '5':
            print("Thank you for using the Point of Sale System!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
