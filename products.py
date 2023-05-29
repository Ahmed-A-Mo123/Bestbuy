class Product:
    def __init__(self, name, price, quantity, active=True):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = active

        if self.price < 0:
            raise ValueError("Please enter a number higher than 0")

        elif self.name == "":
            raise Exception("Please enter the name of the product")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: £ {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Insufficient quantity available")
            self.set_quantity(self.quantity)
        self.set_quantity(self.quantity - quantity)

        sub_total = self.price * quantity
        return sub_total


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    mac.show()

    bose.set_quantity(1000)


if __name__ == "__main__":
    main()