class Konto():
    def __init__(self, person, hashedPasswort):
        self.person = person
        self.hashedPasswort = hashedPasswort
        self.kontostand = 0
        self.buchungen = []

    def einzahlen(self, betrag, art):
        self.kontostand += betrag
        self.buchungen.append({'Art': art, 'Betrag': betrag})

    def auszahlen(self, betrag, art, hashedPasswort):
        pass

    def kontostandAbfragen(self, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            return self.kontostand
        else:
            print('Falsches Passwort, bitte neu einloggen.')

    def letzteBuchung(self, hashedPasswort):
        if self.hashedPasswort == hashedPasswort:
            return self.buchungen[-1]
        else:
            print('Falsches Passwort, bitte neu einloggen.')