import math


# from abc import ABC, abstractmethod


# class Promotion(ABC):
#   def __init__(self, name_offer):
#     self.offer = name_offer

#   @abstractmethod
#   def apply_promotion(product, quantity):
#       pass

# class SecondHalfPrice(Promotion):

#   def apply_promotion(self, product, quantity):
#         sub_total = 0
#         for i in range(1, quantity + 1):
#             if i % 2 == 0:
#                 half_off_price = product.price / 2
#                 sub_total += half_off_price
#             else:
#                 sub_total += product.price
#         return sub_total

# class ThirdOneFree(Promotion):

#   def apply_promotion(product, quantity):
#     pass

# class PercentDiscount(Promotion):
#     def __init__(self, percentage_offer):
#       super().__init__(self, name_offer)
#       self.percentage = percentage_offer

#     def apply_promotion(product, quantity):
#       pass


class Product:
    def __init__(self, name, price, quantity, promotion=False, active=True):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = active
        self.promotion = promotion

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
        if self.quantity <= 0:
            self.deactivate()

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, new_promotion):
        self.offer_name = new_promotion.get_promotion_name()
        self.promotion = new_promotion

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        if self.promotion is False:
            return f"{self.name}, Price: £ {self.price}, Quantity: {self.quantity}"
        else:
            return f"{self.name}, Price: £ {self.price}, Quantity: {self.quantity}, Promotion: {self.offer_name}"

    def buy(self, quantity):

        if self.price < 0 or self.name == "":
            raise ValueError
        elif self.quantity < quantity:
            self.set_quantity(self.quantity)
            raise ValueError("Insufficient quantity available")

        elif self.promotion is False:
            self.set_quantity(self.quantity - quantity)
            sub_total = self.price * quantity
            return sub_total

        else:
            return self.promotion.apply_promotion(self, quantity)


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=100 ** 100000):
        super().__init__(name, price, quantity)
        self.quantity = quantity

    def show(self):
        if self.promotion is False:
            return f"{self.name}, Price: £ {self.price}"
        else:
            return f"{self.name}, Price: £ {self.price},Promotion: {self.offer_name}"

    def buy(self, quantity):
        super().buy(self, quantity)
        static_quantity = math.inf  # Not sure how to make it infinite/limitless so used the math module
        self.set_quantity(static_quantity)
        sub_total = self.price * quantity
        return sub_total


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        if self.promotion is False:
            return f"{self.name}, Price: £ {self.price}, (order once per order)"
        else:
            return f"{self.name}, Price: £ {self.price},Promotion: {self.offer_name}"

    def buy(self, quantity):
        super().buy(self, quantity)
        self.set_quantity(self.maximum)
        if quantity > self.maximum:
            raise ValueError()
        sub_total = self.price * 1
        return sub_total


def main():
    pass


if __name__ == "__main__":
    main()
