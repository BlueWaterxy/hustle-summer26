import random
# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Santiago Avila Ignacio
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Rubber ducks
# ============================================================



# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class RubberDuck:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be below $0.")
        else:
            self.price = amount

    def deliver(self):
        print("Your rubber duck is floating your way!")




# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: the code will break due it not working.
#   Paste the message you see here:"Price cannot be below $0."

        

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class GiantDuck(RubberDuck):
    def deliver(self):
        print("A giant splash! Your giant duck is on the way!")


item4 = GiantDuck("Giant Rainbow Duck", 15)



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things:The same method name can do two different things because each class
# (removed stray duplicate functions)


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
# PREDICT: I prdecit it will show classic yellow duck because it's the first item. 
# print(item1.name) will show "Classic Yellow Duck"
item1 = RubberDuck("Classic Yellow Duck", 5)
item2 = RubberDuck("Pirate Duck", 8)
item3 = RubberDuck("King Duck", 10)

print(item1.name)
item1.set_price(3)

print(item1.name + " is on sale for $" + str(item1.price) + "!")


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        total = 0

        for item in self.items:
            item.deliver()
            total += item.price

        print("Total: $" + str(total))
# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.



# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()


welcome_messages = [
    "Welcome to the Rubber Duck Store!",
    "Quack! Thanks for stopping by!",
    "Find your perfect rubber duck today!"
]
print("Here is what we have:")

for number, item in store.items():
    print(number + ": " + item.name + " - $" + str(item.price))

print(random.choice(welcome_messages))

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: Classic Yellow Duck will be added to the cart.
# TICKET 8: Let customers shop
while True:
    choice = input("Pick 1, 2, 3, or 'done': ")

    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
        print(store[choice].name + " added!")
    else:
        print("Sorry, that's not on the menu!")
        print("----- Your Receipt -----")
    print("You bought " + str(len(cart.items)) + " items.")



for item in cart.items:
    print(item.name + " ..... $" + str(item.price))

print("You bought " + str(len(cart.items)) + " items.")
cart.checkout()



# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
