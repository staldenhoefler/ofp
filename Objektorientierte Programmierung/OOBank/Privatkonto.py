from Konto import Konto
class Privatkonto(Konto):
    def __init__(self, hashed_password, withdrawal_limit):
        super().__init__(hashed_password)
        self._hashed_password = hashed_password
        self._withdrawal_limit = withdrawal_limit

    def transfer(self, value, account_type, hashed_password):
        if self._hashed_password == hashed_password:
            gebühren = value * 0.005
            if self._balance - (value+gebühren) >= self._withdrawal_limit:
                self._balance -= (value+gebühren)
                self._transfer_info.append({'Art': account_type, 'Betrag': -(value+gebühren)})
                return True
            else:
                raise ValueError('Nicht genügend Geld auf dem Konto')
                return False
        else:
            raise ValueError('Falsches Passwort, bitte neu einloggen.')
            return False