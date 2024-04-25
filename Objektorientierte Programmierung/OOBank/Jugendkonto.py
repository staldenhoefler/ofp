from Konto import Konto
class Jugendkonto(Konto):
    def __init__(self, person, hashedPasswort):
        super().__init__(person, hashedPasswort)

    def auszahlen(self, betrag, art, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            if self.kontostand - betrag >= 0:
                self.kontostand -= betrag
                self.buchungen.append({'Art': art, 'Betrag': -betrag})
                return True
            else:
                print('Nicht genügend Geld auf dem Konto')
                return False
        else:
            print('Falsches Passwort, bitte neu einloggen.')
            return False