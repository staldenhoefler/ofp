from Jugendkonto import Jugendkonto
from Privatkonto import Privatkonto
import random
import string
class Bank():
    def __init__(self, name):
        self.name = name
        self.__account = dict()
        self.__customer = dict()
        self.__create_initial_bankaccount()
        self.__initial_bankaccount = self.__customer['Admin']['Konten'][0]

    def open_new_account(self, person, account_type, hashed_password):
        iban = self.__generate_IBAN()
        self.__customer[person]['Konten'].append(iban)

        if account_type == 'Jugendkonto':
            self.__account[iban] = Jugendkonto(hashed_password)
        elif account_type == 'Privatkonto':
            self.__account[iban] = Privatkonto(hashed_password, -1000)
        else:
            print('Diese Art von Konto gibt es nicht')

    def deposit(self, iban, value):
        try:
            self.__account[iban].deposit(value, 'Bareinzahlung')
        except ValueError:
            print(ValueError)
        except KeyError:
            print('Diese IBAN existiert nicht')



    def transfer(self, iban, target_iban, value, hashed_password):
        try:
            if value > 0:
                if self.__account[iban].transfer(value, f'Buchung an {target_iban}', hashed_password):
                    self.__account[self.__initial_bankaccount].deposit(value * 0.005, f'Gebühr für Buchung von {iban} an {target_iban}')
                    self.__account[target_iban].deposit(value, f'Einzahlung von {iban}')
            else:
                raise ValueError('Betrag muss grösser als 0 sein')
        except ValueError:
            print(ValueError)
        except KeyError:
            print('Eine der IBANs existiert nicht')

    def get_account_balance(self, iban, hashed_password):
        try:
            return self.__account[iban].get_account_balance(hashed_password)
        except ValueError:
            print(ValueError)
        except KeyError:
            print('Diese IBAN existiert nicht')

    def last_transfer_info(self, iban, hashed_password):
        try:
            return self.__account[iban].last_transfer_info(hashed_password)
        except ValueError:
            print(ValueError)
        except KeyError:
            print('Diese IBAN existiert nicht')

    def close_account(self, person, iban, hashed_password):
        try:
            if self.get_account_balance(iban, hashed_password) == 0:
                self.__account.pop(iban)
                self.__customer[person]['Konten'].remove(iban)
            else:
                raise ValueError('Konto kann nur geschlossen werden, wenn der Kontostand 0 ist')
        except ValueError:
            print(ValueError)
        except KeyError:
            print('Diese IBAN existiert nicht')

    def login_customer(self, person, hashedPassword):
        if person in self.__customer:
            if self.__customer[person]['Passwort'] == hashedPassword:
                return True
        raise ValueError('Falscher Nutzername oder Passwort')

    def add_new_customer(self, person, hashedPasswort):
        if person not in self.__customer:
            self.__customer[person] = {'Konten': [], 'Passwort': hashedPasswort}
            return True
        raise ValueError('Dieser Nutzername existiert bereits')


    def __generate_IBAN(self):
        return 'CH' + ''.join(random.choices(string.digits, k=2)) + ' ' + ''.join(
            random.choices(string.digits, k=4)) + ' ' + ''.join(random.choices(string.digits, k=4)) + ' ' + ''.join(
            random.choices(string.digits, k=4)) + ' ' + ''.join(random.choices(string.digits, k=4)) + ' ' + ''.join(
            random.choices(string.digits, k=1))



    def show_accounts(self, person, hashed_password):
        try:
            if hashed_password == self.__customer[person]['Passwort']:
                accounts = []
                for account in self.__customer[person]['Konten']:
                   accounts.append(account)
                return accounts
            else:
                raise ValueError('Leider nicht eingeloggt.')
        except KeyError:
            print('Es ist ein Fehler unterlaufen. Bitte loggen Sie sich neu ein')

    def __create_initial_bankaccount(self):
        self.add_new_customer('Admin', hash('Admin'))
        self.__customer['Admin']['Konten'].append('CH00 0000 0000 0000 0000 0')
        self.__account['CH00 0000 0000 0000 0000 0'] = Jugendkonto(hash('Admin'))
