from Bank import Bank
from Interface import Interface
bank = Bank('UBS')

bank.add_new_customer('Peter', hash('123'))
bank.add_new_customer('Paul', hash('123'))

bank.open_new_account('Peter', 'Jugendkonto', hash('123'))
first_accountIban_peter = bank.show_accounts('Peter', hash('123'))[0]
bank.deposit(first_accountIban_peter,1000)

bank.open_new_account('Paul', 'Privatkonto', hash('123'))
first_accountIban_paul = bank.show_accounts('Paul', hash('123'))[0]
bank.deposit(first_accountIban_paul,1000)


print(f"IBAN Peter: {first_accountIban_peter}")
print(f"IBAN Paul: {first_accountIban_paul}")



interface = Interface(bank)
interface.start()