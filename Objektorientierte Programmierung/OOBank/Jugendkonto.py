from Konto import Konto
class Jugendkonto(Konto):
    def __init__(self, hashed_password):
        super().__init__(hashed_password)

    def transfer(self, value, account_type, hashed_password):
        if self._hashed_password == hashed_password:
            if self._balance - value >= 0:
                self._balance -= value
                self._transfer_info.append({'Art': account_type, 'Betrag': -value})
                return True
            else:
                raise ValueError('Nicht genügend Geld auf dem Konto')
                return False
        else:
            raise ValueError('Falsches Passwort, bitte neu einloggen.')
            return False