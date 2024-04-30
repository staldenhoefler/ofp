from Jugendkonto import Jugendkonto
from Privatkonto import Privatkonto
import random
import string
class Bank():
    def __init__(self, name):
        self.name = name
        self.__Konten = dict()
        self.__Kunden = dict()
        self.__InitialBankenkontoErstellen()
        self.__BankenKonto = self.__Kunden['Admin']['Konten'][0]

    def kontoEröffnen(self, person, artDesKontos, hashedPasswort):
        iban = self.__generateIBAN()
        self.__Kunden[person]['Konten'].append(iban)

        if artDesKontos == 'Jugendkonto':
            self.__Konten[iban] = Jugendkonto(hashedPasswort)
        elif artDesKontos == 'Privatkonto':
            self.__Konten[iban] = Privatkonto(hashedPasswort, -1000)
        else:
            print('Diese Art von Konto gibt es nicht')

    def einzahlen(self, iban, betrag):
        if betrag > 0:
            self.__Konten[iban].einzahlen(betrag, 'Bareinzahlung')
        else:
            print('Betrag muss grösser als 0 sein')

    def buchung(self, iban, zielKonto, betrag, hashedPasswort):
        if betrag > 0:
            if self.__Konten[iban].auszahlen(betrag, f'Buchung an {zielKonto}', hashedPasswort):
                self.__Konten[self.__BankenKonto].einzahlen(betrag * 0.005, f'Gebühr für Buchung von {iban} an {zielKonto}')
                self.__Konten[zielKonto].einzahlen(betrag, f'Einzahlung von {iban}')
        else:
            print('Betrag muss grösser als 0 sein')

    def kontostandAbfragen(self, iban, hashedPasswort):
        return self.__Konten[iban].kontostandAbfragen(hashedPasswort)

    def letzteBuchung(self, iban, hashedPasswort):
        return self.__Konten[iban].letzteBuchung(hashedPasswort)

    def kontoSchliessen(self, person, iban, hashedPasswort):
        if self.__Konten[iban].hashedPasswort == hashedPasswort:
            if self.kontostandAbfragen(iban, hashedPasswort) == 0:
                self.__Konten.pop(iban)
                self.__Kunden[person]['Konten'].remove(iban)
            else:
                print('Konto kann nur geschlossen werden, wenn der Kontostand 0 ist')
        else:
            print('Falsches Passwort, bitte neu einloggen.')

    def interface(self):
        while True:
            passwortValidiert = False
            person = ''
            hashedPasswort = ''

            antwort = input(
                f'Willkommen bei der Bank {self.name}. \n' +
                'Wenn Sie bereits Kunde sind, können Sie das Single-Sign-On nutzen. Möchten Sie sich einloggen?\n' +
                '1: Ja\n' +
                '2: Ich bin ein neuer Kunde und möchte mich registrieren\n'
            )
            korrekteEingabe = False
            while not korrekteEingabe:
                if antwort == '1':
                    while not passwortValidiert:
                        person = input('Bitte geben Sie Ihren Namen ein: ')
                        passwort = input('Bitte geben Sie Ihr Passwort ein: ')
                        hashedPasswort = hash(passwort)
                        if person in self.__Kunden and self.__Kunden[person]['Passwort'] == hashedPasswort:
                            passwortValidiert = True
                            korrekteEingabe = True
                        else:
                            print('Passwort oder Nutzername falsch')
                            antwort = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                            if antwort == '2':
                                break
                elif antwort == '2':
                    person = input('Bitte geben Sie Ihren Namen ein: ')
                    passwort = input('Bitte geben Sie Ihr neues Passwort ein: ')
                    hashedPasswort = hash(passwort)
                    if self.__neuenKundenAnlegen(person, hashedPasswort):
                        print('Wilkommen bei der Bank', self.name, person)
                        passwortValidiert = True
                        korrekteEingabe = True
                    else:
                        antwort = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                        korrekteEingabe = False
                else:
                    print('Falsche Eingabe')
                    antwort = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                    korrekteEingabe = False

            while True:
                print('Sie haben folgende Konten bei uns:')
                self.__kontenAnzeigen(person)
                print('Sie haben folgende Möglichkeiten:')
                print('1: Konto eröffnen')
                print('2: Bareinzahlung')
                print('3: Buchung')
                print('4: Kontostand abfragen')
                print('5: Letzte Buchung abfragen')
                print('6: Konto schliessen')
                print('7: Beenden')
                antwort = input()

                if antwort == '1':
                    if passwortValidiert:
                        print('Welche Art von Konto möchten Sie eröffnen?')
                        print('1: Jugendkonto')
                        print('2: Privatkonto')
                        antwort = input()
                        if antwort == '1':
                            self.kontoEröffnen(person, 'Jugendkonto', hashedPasswort)
                        elif antwort == '2':
                            self.kontoEröffnen(person, 'Privatkonto', hashedPasswort)
                        else:
                            print('Falsche Eingabe')
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '2':
                    if passwortValidiert:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        betrag = input('Bitte geben Sie den Betrag ein: ')
                        try:
                            betrag = float(betrag)
                            self.einzahlen(iban, betrag)
                        except ValueError:
                            print('Falsche Eingabe')
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '3':
                    if passwortValidiert:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        zielIban = input('Bitte geben Sie die Ziel-IBAN ein: ')
                        betrag = input('Bitte geben Sie den Betrag ein: ')
                        try:
                            betrag = float(betrag)
                            self.buchung(iban, zielIban, betrag, hashedPasswort)
                        except ValueError:
                            print('Falsche Eingabe')
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '4':
                    if passwortValidiert:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        print(self.kontostandAbfragen(iban, hashedPasswort))
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '5':
                    if passwortValidiert:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        print(self.letzteBuchung(iban, hashedPasswort))
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '6':
                    if passwortValidiert:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        self.kontoSchliessen(person, iban, hashedPasswort)
                    else:
                        print('Sie müssen sich einloggen')
                elif antwort == '7':
                    print('Auf Wiedersehen')
                    break
                else:
                    print('Falsche Eingabe')

    def __generateIBAN(self):
        return 'CH' + ''.join(random.choices(string.digits, k=2)) + ' ' + ''.join(
            random.choices(string.digits, k=4)) + ' ' + ''.join(random.choices(string.digits, k=4)) + ' ' + ''.join(
            random.choices(string.digits, k=4)) + ' ' + ''.join(random.choices(string.digits, k=4)) + ' ' + ''.join(
            random.choices(string.digits, k=1))

    def __neuenKundenAnlegen(self, person, passwort):
        if person not in self.__Kunden:
            self.__Kunden[person] = {'Konten': [], 'Passwort': passwort}
            return True
        else:
            print('Dieser Nutzername ist bereits vergeben.')
            return False

    def __kontenAnzeigen(self, person):
        for konto in self.__Kunden[person]['Konten']:
            print(konto)

    def __InitialBankenkontoErstellen(self):
        self.__neuenKundenAnlegen('Admin', hash('Admin'))
        self.__Kunden['Admin']['Konten'].append('CH00 0000 0000 0000 0000 0')
        self.__Konten['CH00 0000 0000 0000 0000 0'] = Jugendkonto(hash('Admin'))
