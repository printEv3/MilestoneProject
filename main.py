'''Here is my milestone project
Define a class with parameters for item's name, price, quantity, and description
and another one for name, date, and cart items and define customer's options'''
class item_to_purchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_of_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"Number of Items: {self.get_num_of_items_in_cart()}")

        for item in self.cart_items:
            total_item_cost = item.item_price * item.item_quantity
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${total_item_cost}")

            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output item's description")
    print("o - Output shopping cart")
    print("q - Quit")
    print("Choose an option:")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)

    choice = ''
    while choice != 'q':
        print_menu()
        choice = input().lower()

        if choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: $"))
            item_quantity = int(input("Enter the item quantity: "))

            new_item = item_to_purchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)

        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))


            # Create a modified item with only the new quantity
            modified_item = item_to_purchase(item_name, 0, new_quantity, "none")
            cart.modify_item(modified_item)

        elif choice != 'q':
            print("Not an option on the menu, try again.")


if __name__ == "__main__":
    main()