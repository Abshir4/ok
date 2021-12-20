import random
from shoping_map import the_shop
from blackjack import play_blackjack 
from blackjack import buy_chips, cash_in_chips
from blackjack import Chips
from account import Account
    from cafeteria import *
    
    def set_accounts():
        accounts = []
        for i in range(1000, 9999):
            account = Account(i, 1000)
            accounts.append(account)
        return accounts
    
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
    
    def bank(accounts):
    accountobj = None
    # ATM Processes
    is_banking = True
    while is_banking:

        accountobj = find_account(accounts)

        # Iterating over account session
        while True:

            # Printing menu
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            # Reading selection
            selection = int(input("\nEnter your selection: "))

            # View Balance
            if selection == 1:
                # Printing balance
                print(accountobj.getBalance())

            # Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")

                if ver_withdraw == "Yes".lower():
                    print("Verify withdraw")
                else:
                    break

                if amt <= accountobj.getBalance():
                    # Calling withdraw method
                    accountobj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountobj.getBalance()) + "$")
                    print("\nUpdated cash: " + str(accountobj.getCash()) + "$")
                else:
                    print("\nYour balance is less than withdrawal amount: " + str(accountobj.getBalance()) + "$")
                    print("\nPlease make a deposit.")

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount" + str(amt) + "$ Yes, or No ?\n")

                if ver_deposit == "Yes".lower():
                    # Calling deposit method
                    accountobj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountobj.getBalance()) + "$\n")
                else:
                    break

            elif selection == 4:
                print("\nTransaction is now complete.")
                print("\nTransaction number: ", random.randint(10000, 1000000))
                print("\nThanks for choosing us as your bank\n")

            # Any other choice
            else:
                print("That's an invalid choice.")
            is_banking = False
            break



def main():
    row = 0
    col = 2
    running = True
    # Creating accounts
    global accounts
    accounts = set_accounts()

    while running:
        print("You are now in", the_shop[row][col]['description'])
        print("You can go", the_shop[row][col]['exits'])
        command = input("> ")
        
        # Use ATM at the entrance
        if command == "ATM" and (row, col) == (0, 2):
            bank(accounts)

        # Play blackjack from the blackjack room
        elif command == "play blackjack" and (row, col) == (0, 0):
            if('bought_chips' in locals()):
                chips = play_blackjack(bought_chips)
            else:
                print("You dont have any chips. Buy chips first !\n")

        # To buy chips from the blackjack room
        elif command == "buy chips" and (row, col) == (0, 0):
            # for an existing player, who wants to buy more chips
            if('chips' in locals()):
                bought_chips = buy_chips(accounts, chips)
            else:
                # for first time players
                player_chips = Chips()
                bought_chips = buy_chips(accounts, player_chips)

        # Cash in chips from the blackjack room
        elif command == "cash in chips" and (row, col) == (0, 0):
            if('chips' in locals()):
                accounts = cash_in_chips(accounts, chips)
            elif('bought_chips' in locals()):
                accounts = cash_in_chips(accounts, bought_chips)
            else:
                print("You haven't played blackjack yet. Play and win some chips first !")    

        # to do something from the cafeteria
        elif command == "enter cafeteria" and (row, col) == (0, 1):
            home_cafe(accounts)

        # To go somewhere  
        else:
            go = command.split()
            if go[0].lower() == "go":
                if go[1].lower() in the_shop[row][col]['exits']:
                    if go[1].lower() == "east":
                        col += 1
                    elif go[1].lower() == "west":
                        col -= 1
                else:
                    print("You can't go in that direction.")
            elif go[0].lower() == "quit":
                running = False
            if command == "ATM":
                print("there is no atm here")

if __name__ == '__main__':
    main()