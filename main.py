import store
import products
import sys
import promotions

MENU = """\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n"""


def print_products(store_obj):
    """Prints all products in the store with their details."""
    print("------")
    item_number = 0
    for item in store_obj.get_all_products():
        print(f'{item_number} ~ {item.show()}')
        item_number += 1
    print("------")


def start(store_obj):
    """
    Starts the store management system.
    """
    active_product_list = store_obj.get_all_products()
    while True:
        print(MENU)
        try:
            user_choice = int(input("Please enter a menu choice (1-4): "))
            if user_choice > 4:
                raise ValueError

        except ValueError:
            print("\n****Please Enter A Number Between 1-4****\n")
            user_choice = 'Void'

        if user_choice == 1:
            print()  # Spacing
            print_products(store_obj)
            print()
#-----------------------------------------------------------------------------------------
        if user_choice == 2:
            item_count = store_obj.get_total_quantity()
            print(f"\nTotal of {item_count} items in store\n")
#-----------------------------------------------------------------------------------------
        if user_choice == 3:
            print_products(store_obj)
            shopping_list = []
            while True:
                print("When you want to finish order, enter empty text.")
                try:
                    product_choice = int(input("Which product # do you want? "))
                    product_obj = active_product_list[product_choice - 1]
                    amount_choice = int(input("What amount do you want? "))
                    if product_choice and amount_choice == "":
                        raise ValueError

                except ValueError:
                    break

                shopping_list.append((product_obj, amount_choice))
                print("Product Added to the list\n")

                try:
                    total_payment = store_obj.order(shopping_list)
                    if total_payment is None:
                        print('Sorry Your order has Failed')

                except ValueError:
                    print("\n***Sorry we don't have enough to fulfill your order***\n")

                else:
                    print(f"Order Made! Total Payment: {total_payment}")
#------------------------------------------------------------------------------------------
        if user_choice == 4:
            sys.exit('\nThanks For Shopping With Us, Til Next Time BYE\n')

        input("Press Enter To Continue")


def main():
    """
    Initializes the store and starts the store management system.

    """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[3].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[0].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    try:
        start(best_buy)
    except IndexError:
        print("This product is not active/ available")


if __name__ == '__main__':
    main()
