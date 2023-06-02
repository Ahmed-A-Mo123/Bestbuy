from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name_offer, percent=0):
        self.offer = name_offer
        self.percentage = percent

    def get_promotion_name(self):
        return self.offer
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        sub_total = 0
        for i in range(1, quantity + 1):
            if i % 2 == 0:
                half_off_price = product.price / 2
                sub_total += half_off_price
            else:
                sub_total += product.price
        return sub_total


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        sub_total = 0
        for i in range(1, quantity + 1):
            if i % 3 == 0:
                continue
            else:
                sub_total += product.price
        return sub_total


class PercentDiscount(Promotion):

    def apply_promotion(self, product, quantity):
        percentage = float(self.percentage / 100)
        decrease = product.price * percentage
        normal_price = product.price * quantity
        return normal_price - decrease


