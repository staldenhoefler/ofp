from Konto import Konto
class Privatkonto(Konto):
    def __init__(self, person, hashedPasswort, bezugslimite):
        super().__init__(person, hashedPasswort)
        self.bezugslimite = bezugslimite

    def auszahlen(self, betrag, art, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            gebühren = betrag * 0.005
            if self.kontostand - (betrag+gebühren) >= self.bezugslimite:
                self.kontostand -= (betrag+gebühren)
                self.buchungen.append({'Art': art, 'Betrag': -(betrag+gebühren)})
                return True
            else:
                print('Nicht genügend Geld auf dem Konto')
                return False
        else:
            print('Falsches Passwort, bitte neu einloggen.')
            return False