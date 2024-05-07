class Konto():
    def __init__(self, hashed_password):
        self._hashed_password = hashed_password
        self._balance = 0
        self._transfer_info = []

    def deposit(self, value, account_type):
        if value > 0:
            self._balance += value
            self._transfer_info.append({'Art': account_type, 'Betrag': value})
        else:
            raise ValueError('Betrag muss grösser als 0 sein')

    def transfer(self, value, account_type, hashed_password):
        pass

    def get_account_balance(self, hashed_password):
        if self._hashed_password == hashed_password:
            return self._balance
        else:
            raise ValueError('Falsches Passwort, bitte neu einloggen.')

    def last_transfer_info(self, hashed_password):
        if self._hashed_password == hashed_password:
            return self._transfer_info[-1]
        else:
            raise ValueError('Falsches Passwort, bitte neu einloggen.')