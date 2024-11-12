#store management
# With class

class Item:
    pass #keyword to avoild empty declaration
    """ Define a function inside a class called a Method"""
    "Python passes object to methods"
    def calculate_total_price(self, price, quantity):
        return price * quantity

#Object of class Iteam
item1 = Item()

#Attributes to the class
item1.name = "Phone"
item1.price = 1000
item1.quantity = 5

#call the function
print(item1.calculate_total_price(item1.price, item1.quantity))

print(item1)
print(item1.name)
print(item1.price)
print(item1.quantity)
