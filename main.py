import store
import products
import sys

MENU = f"""\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit
  """


def print_products(store_obj):
    active_product_list = store_obj.get_all_products()
    item_number = 1
    print("------")
    for i in active_product_list:
        print(f"{item_number}. {i.show()}")
        item_number += 1
    print("------")


def start(store_obj):
    active_product_list = store_obj.get_all_products()
    while True:
        print(MENU)
        try:
            user_choice = int(input("Please enter a menu choice (1-4): "))
            if user_choice > 4:
                raise ValueError

        except ValueError:
            print("\n****Please Enter A Number Between 1-4****\n")

        # ----------------------------------------------------------------
        if user_choice == 1:
            print()  # Spacing
            print_products(store_obj)
            print()

        # ----------------------------------------------------------------
        if user_choice == 2:
            item_count = store_obj.get_total_quantity()
            print(f"\nTotal of {item_count} items in store\n")
        # ----------------------------------------------------------------
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

                except ValueError:
                    print("\n***Sorry we dont have enough to fulfil your order***\n")

                if total_payment is None:
                    print('This Product is out of stock or we dont have enough to fulfil your order')
                else:
                    print(f"Order Made! Total Payment: {total_payment}")




        # ------------------------------------------------------------------------
        if user_choice == 4:
            sys.exit('\nThanks For Shopping With Us, Til Next Time BYE\n')

        input("Press Enter To Continue")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)

    try:
        start(best_buy)
    except IndexError:
        print("This product is not active/ avialable")


if __name__ == "__main__":
    main()