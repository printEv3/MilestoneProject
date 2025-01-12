'''
Here is my milestone project
Let's create a class and its attributes
We need to obtain the item's name, price, and quantity from user input
'''

class item_to_purchase:
    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
item_name = str(input('Enter the name of your first item: '))
item_price = float(input('Enter the price of your item: '))
item_quantity = int(input('Enter the quantity of your item: '))
item_cost_1 = (item_price * item_quantity)
print(item_name, item_quantity, '@', item_price, '= $',item_cost_1)

item_name = str(input('Enter the name of your second item: '))
item_price = float(input('Enter the price of your item: '))
item_quantity = int(input('Enter the quantity of your item: '))
item_cost_2 = (item_price * item_quantity)
print(item_name, item_quantity, '@', item_price, '= $', item_cost_2)

total_cost = (item_cost_1 + item_cost_2)
print('Here is your total cost: $', total_cost)
print('Thank you for your order!')

'''
Shhh...don't tell the user 
But...
Spam and ice cream sounds like a recipe for Tums...
'''
