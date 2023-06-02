from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name_offer, percent=0):
        self.offer = name_offer
        self.percentage = percent

    def get_promotion_name(self):
        """Returns the name of the promotion."""
        return self.offer

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Abstract method to apply the promotion to a product."""
        pass


class SecondHalfPrice(Promotion):
    """Promotion class for applying a "Second Half Price" discount."""
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
    """Promotion class for applying a "Third One Free" discount."""
    def apply_promotion(self, product, quantity):
        sub_total = 0
        for i in range(1, quantity + 1):
            if i % 3 == 0:
                continue
            else:
                sub_total += product.price
        return sub_total


class PercentDiscount(Promotion):
    """Promotion class for applying a percentage discount."""
    def apply_promotion(self, product, quantity):
        percentage = float(self.percentage / 100)
        decrease = product.price * percentage
        normal_price = product.price * quantity
        return normal_price - decrease
