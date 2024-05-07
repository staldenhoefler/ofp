
class Interface():
    def __init__(self, bank):
        self.bank = bank

    def start(self):
        while True:
            validated_password = False
            person = ''
            hashed_password = ''

            response = input(
                f'Willkommen bei der Bank {self.bank.name}. \n' +
                'Wenn Sie bereits Kunde sind, können Sie das Single-Sign-On nutzen. Möchten Sie sich einloggen?\n' +
                '1: Ja\n' +
                '2: Ich bin ein neuer Kunde und möchte mich registrieren\n'
            )
            correct_input = False
            while not correct_input:
                try:
                    if response == '1':
                        while not validated_password:
                            person = input('Bitte geben Sie Ihren Namen ein: ')
                            password = input('Bitte geben Sie Ihr Passwort ein: ')
                            hashed_password = hash(password)
                            if self.bank.login_customer(person, hashed_password):
                                validated_password = True
                                correct_input = True
                            else:
                                response = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                                if response == '2':
                                    break
                    elif response == '2':
                        person = input('Bitte geben Sie Ihren Namen ein: ')
                        password = input('Bitte geben Sie Ihr neues Passwort ein: ')
                        hashed_password = hash(password)
                        if self.bank.add_new_customer(person, hashed_password):
                            print('Wilkommen bei der Bank', person)
                            validated_password = True
                            correct_input = True
                        else:
                            response = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                            correct_input = False
                    else:
                        print('Falsche Eingabe')
                        response = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                        correct_input = False
                except ValueError as e:
                    print(e)
                    response = input('Möchten Sie es nochmals versuchen? 1: Ja, 2: Nein')
                    correct_input = False

            while True:
                print('Sie haben folgende Konten bei uns:')
                print(self.bank.show_accounts(person, hashed_password))
                print('Sie haben folgende Möglichkeiten:')
                print('1: Konto eröffnen')
                print('2: Bareinzahlung')
                print('3: Buchung')
                print('4: Kontostand abfragen')
                print('5: Letzte Buchung abfragen')
                print('6: Konto schliessen')
                print('7: Beenden')
                response = input()

                if response == '1':
                    if validated_password:
                        print('Welche Art von Konto möchten Sie eröffnen?')
                        print('1: Jugendkonto')
                        print('2: Privatkonto')
                        response = input()
                        if response == '1':
                            self.bank.open_new_account(person, 'Jugendkonto', hashed_password)
                        elif response == '2':
                            self.bank.open_new_account(person, 'Privatkonto', hashed_password)
                        else:
                            print('Falsche Eingabe')
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '2':
                    if validated_password:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        value = input('Bitte geben Sie den Betrag ein: ')
                        value = float(value)
                        self.bank.deposit(iban, value)
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '3':
                    if validated_password:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        target_iban = input('Bitte geben Sie die Ziel-IBAN ein: ')
                        value = input('Bitte geben Sie den Betrag ein: ')
                        value = float(value)
                        self.bank.transfer(iban, target_iban, value, hashed_password)
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '4':
                    if validated_password:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        print(self.bank.get_account_balance(iban, hashed_password))
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '5':
                    if validated_password:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        print(self.bank.last_transfer_info(iban, hashed_password))
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '6':
                    if validated_password:
                        iban = input('Bitte geben Sie Ihre IBAN ein: ')
                        self.bank.close_account(person, iban, hashed_password)
                    else:
                        print('Sie müssen sich einloggen')
                elif response == '7':
                    print('Auf Wiedersehen')
                    break
                else:
                    print('Falsche Eingabe')