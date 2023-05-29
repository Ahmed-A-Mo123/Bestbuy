import products


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)

        else:
            print("That product doesn't exist")

    def get_total_quantity(self):
        return len(self.product_list)

    def get_all_products(self):
        active_list = [i for i in self.product_list if i.is_active() == True]
        return active_list

    def order(self, shopping_list):
        total = 0
        for product, quantity1 in shopping_list:
            try:
                total += product.buy(quantity1)
            except ValueError:
                print(product.name)
                return None
        return total


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    all_products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(all_products[0], 100), (all_products[1], 2)]))


if __name__ == "__main__":
    main()