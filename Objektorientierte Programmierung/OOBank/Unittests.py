import unittest
from Bank import Bank

class MyTestCase(unittest.TestCase):
    def test_transfer(self):
        bank, firstIban, secondIban = self.__initiation()
        bank.
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

def __initiation(self):
    bank = Bank('UBS')
    bank.add_new_customer('Peter', hash('123'))
    bank.add_new_customer('Paul', hash('123'))
    bank.open_new_account('Peter', 'Jugendkonto', hash('123'))
    first_accountIban_peter = bank.show_accounts('Peter', hash('123'))[0]
    bank.deposit(first_accountIban_peter, 1000)
    bank.open_new_account('Paul', 'Privatkonto', hash('123'))
    first_accountIban_paul = bank.show_accounts('Paul', hash('123'))[0]
    bank.deposit(first_accountIban_paul, 1000)
    return bank, first_accountIban_peter, first_accountIban_paul
