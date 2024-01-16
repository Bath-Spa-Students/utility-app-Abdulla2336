class VendingMachine:
    def _init_(self):
        self.products = {
            '1': {'name': 'Coke', 'price': 1.50, 'quantity': 10},
            '2': {'name': 'Snacks', 'price': 2.00, 'quantity': 8},
            '3': {'name': 'Water', 'price': 1.00, 'quantity': 12},
            '4': {'name': 'Chocolates', 'price': 1.75, 'quantity': 5},
            '5': {"name" :"Sprite","price":1.25,'quantity': 3},
            '6': {"name" :"Fanta","price":2,'quantity': 5},
            '7': {"name" :"Fruit Juice","price":5,'quantity': 15},
            '8': {"name" :"Redbull","price":2.50,'quantity': 1},
            '9': {"name" :"Mountain Dew","price":3,'quantity': 3},
            '10': {"name" :"Dairymilk","price":4,'quantity': 5},
            '11': {"name" :"TWIX","price":2,'quantity': 13},
            '12': {"name" :"Snickers","price":2.50,'quantity': 9},
            '13': {"name" :"Protein Bar","price":2,'quantity': 7},
            '14': {"name" :"Cadbury","price":1.25,'quantity': 5},
            '15': {"name" :"Skittles","price":1.52,'quantity': 8},
            '16': {"name" :"Chicken Sandwich","price":5,'quantity': 2},
            '17': {"name" :"Veg Sandwich","price":4,'quantity': 7},
            '18': {"name" :"Lays","price":2,'quantity': 12},
            '19': {"name" :"Doritos","price":1.50,'quantity': 5},
            '20': {"name" :"Hot Chips","price":3.25,'quantity': 4}
        }
        self.balance = 0.0

    def display_products(self):
        print("Available Products:")
        for code, details in self.products.items():
            print(f"{code}: {details['name']} - ${details['price']} - Quantity: {details['quantity']}")


    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted ${amount}. Current balance: ${self.balance}")

    def dispense_item(self, code):
        if code in self.products:
            details = self.products[code]
            if details['quantity'] > 0 and self.balance >= details['price']:
                self.balance -= details['price']
                details['quantity'] -= 1
                print(f"Dispensing {details['name']}. Remaining balance: ${self.balance}")
                return True
            elif details['quantity'] == 0:
                print(f"Sorry, {details['name']} is out of stock.")
            else:
                print("Insufficient balance. Please insert more money.")
        else:
            print("Invalid product code.")

    def return_change(self):
        change = self.balance
        self.balance = 0.0
        return change

# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_products()

        product_code = input("Enter the product code (or 'exit' to end): ")
        if product_code.lower() == 'exit':
            break

        money_inserted = float(input("Insert money: $"))
        vending_machine.insert_money(money_inserted)

        if vending_machine.dispense_item(product_code):
            more_items = input("Do you want anything else? (yes/no): ").lower()
            if more_items != 'yes':
                break

    change = vending_machine.return_change()
    print(f"Returned change: ${change}. Thank you for using our vending machine. Have a nice day!")