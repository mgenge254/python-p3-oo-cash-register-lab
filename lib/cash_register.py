#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize the cash register with an optional discount."""
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        """Add an item to the cash register."""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """Apply a discount if available, and print the result."""
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction
        self.last_transaction = 0.0
