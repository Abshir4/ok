import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        # creates an account with balance 0 and cash 0
        self.account = Account(1111)
        # creates an account with balance 1000 and cash 0
        self.account1 = Account(1111, 1000)

    # checks for an account with 0 balance
    def test_empty_account(self):
        self.assertEqual(self.account.balance, 0, "Empty account with 0 balance")

    # checks for an account with default 1000 as balance
    def test_balance_account(self):
        self.assertEqual(self.account1.balance, 1000, "Default account balance is 1000")

    # checks whether a given amount is deposited in the account and updates the balance
    def test_deposit_amount(self):
        # trying to deposit an amount of 500
        self.account1.deposit(500)
        self.assertEqual(self.account1.getBalance(), 1500, "deposit 500 to the account(balance 1000) and updates the balance to 1500")

    # checks whether the given amount is withdrawn and updates the balance appropriately
    def test_withdraw_amount(self):
        self.account1.withdraw(300)
        self.assertEqual(self.account1.getBalance(), 700, "withdrawn 300 from account having 1000;¨should update the balance to 700")
        self.assertEqual(self.account1.getCash(), 300, "The withdrawn amount is present as cash in hand which should be 300")

    # checks whether the given amount is withdrawn and updates the balance appropriately
    def test_withdraw_insufficient_amount(self):
        expected = "Insufficient balance"
        actual = self.account1.withdraw(1300)
        self.assertEqual(expected, actual, "Withdrawal Amount is greater than the account balance")

if __name__ == '__main__':
    unittest.main()
