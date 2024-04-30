class Konto():
    def __init__(self, hashedPasswort):
        self.hashedPasswort = hashedPasswort
        self.__kontostand = 0
        self.__buchungen = []

    def einzahlen(self, betrag, art):
        self.__kontostand += betrag
        self.__buchungen.append({'Art': art, 'Betrag': betrag})

    def auszahlen(self, betrag, art, hashedPasswort):
        pass

    def kontostandAbfragen(self, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            return self.__kontostand
        else:
            print('Falsches Passwort, bitte neu einloggen.')

    def letzteBuchung(self, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            return self.__buchungen[-1]
        else:
            print('Falsches Passwort, bitte neu einloggen.')