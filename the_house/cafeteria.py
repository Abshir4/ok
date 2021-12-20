from shop_item import inventory
from account import Account


class Cafe:

    # Construct an Account object
    def __init__(self, inventory):
        self.inventory = inventory

    def add_item(self, key, value):
        # add any new item to the inventory
        # use dictionary modification/updation
        # dictionary_name[´key name'] = some value
        self.inventory[key] = value

    def remove_item(self, key):
        del self.inventory[key]
        # add any new item to the inventory

    def check_item(self, item):
        if item in self.inventory:
            return True
        return False

# class which takes care of customers purchase details
class Orders:
    def __init__(self, cafe):
        self.purchase = []
        self.cafe = cafe

# Add to purchase if item found in the inventory
    def add_to_purchase(self, item):
        # if self.cafe.check_item(item):
        #     self.purchase.append(item)
        # else:
        #     print("item is not present in the inventory")
        if item in self.cafe.inventory.keys():
            self.purchase.append(item)
        else:
            print("item is not present in the inventory")


    def remove_item_purchase(self, item):
        if item in self.purchase:
            self.purchase.remove(item)
            print(f"{item.capitalize()} was removed from your purchase.\n")

    def display_total(self):
        if len(self.purchase) < 1:
            print("Please order something.")
        else:
            total = 0
            for item in self.purchase:
                total += self.cafe.inventory.get(item)
            print(f"Your total is ${total:.2f}")
        return total


    def display_order(self):
        if len(self.purchase) > 0:
            print("Purchase:")
            for item in self.purchase:
                print(f"     {item}")
            print(len(self.purchase))
        else:
            print("Your haven't ordered anything.\n")

# Pays the bill and reduces the amount from the account
    def total_purchase(self, accountobj):
        total = self.display_total()
        if accountobj.balance >= total:
            purchase_command = input("Ready to pay? Yes or no\n").lower()
            if purchase_command[0] == "y":
                print(f"You had ${accountobj.balance:.2f}")
                accountobj.balance -= total
                print(f"Thank you for your purchase, you have ${accountobj.balance:.2f} remaining.\n")
                self.purchase.clear()
        else:
            print(f"Sorry you only have ${accountobj.balance:.2f}: and your total is {total:.2f}.\n")


# Display the inventory and format a string from our <dict> and remove certain objects.
    def display_inventory(self):
        inventory = str(self.cafe.inventory)
        replace_characters = ["'", "{", "}"]
        for val in replace_characters:
            inventory = inventory.replace(val, "")
        inventory = inventory.replace(": ", " $")
        inventory_list = inventory.split(", ")
        for item in inventory_list:
            print(item)

    def buy(self):
        while True:
            buy_command = input("What would you like to order?.\n").lower()
            if buy_command == "help":
                print("inventory = see the list of the inventory items to purchase and prices")
                print("stop = Stop adding items in to your order.\n")

            elif buy_command == "inventory":
                self.display_inventory()
            elif buy_command == "stop":
                break
            else:
                self.add_to_purchase(buy_command)
                print(f"{buy_command.capitalize()} was added to your order.\n")



def find_account(accounts):
    # Reading id from user
    pin = int(input("\nEnter account pin: "))
    # Loop till id is valid
    while pin < 1000 or pin > 9999:
        pin = int(input("\nInvalid Id.. Re-enter: "))
    # Getting account object
    for acc in accounts:
        # Comparing account id
        if acc.getPin() == pin:
            accountobj = acc
            break
    return accountobj


def home_cafe(accounts):
    c1 = Cafe(inventory)
    # create an object for Order class to buy items and pay bill
    order1 = Orders(c1)

    while True:
        command = input("What would you like to do? write help to get assistance\n").lower()
        if command == "help":
            print("\nYou may type: buy leave, pay, total, remove, or balance")
            print("buy = Pick items to purchase.")
            print("leave = Stop the purchase.")
            print("remove = Remove items from your your order.")

            print("pay = Get the total of your items and purchase them.")
            print("total = See the what you have in your order")
            print("order = See all the items in your order. ")

        elif command == "buy":
            order1.buy()

        # not buying anything;¨ust leave the cafe
        elif command == "leave":
            print("Bye, have a nice day\n")
            break

        # finding the account using the pin and paying the bill
        elif command == "pay":
            # have to keep record of accounts in the set
            accountobj = find_account(accounts)
            order1.total_purchase(accountobj)

        # if i just want to find the total amount
        elif command == "total":
            order1.display_total()

        # if i just want to find the items in my order
        elif command == "order":
            order1.display_order()

        elif command == "remove":
            if len(order1.purchase) < 1:
                print("There are no items to remove.\n")
            else:
                remove_command = input("What item would you like to remove ").lower()
                order1.remove_item_purchase(remove_command)
        else:
            print("Im sorry. I dont understand. Type help for of a list of commands.\n")

