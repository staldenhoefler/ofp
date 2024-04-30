# OOBank
OOBank ist eine kleine Übungsaufgabe für das Objektorientierte Programmieren.
## Themen
- [Usage](#usage)
- [Klassen](#klassen)


## Usage
Zum Starten des Programms muss nur das File `main.py` ausgeführt werden. 
```python
from Bank import Bank
bank = Bank('UBS')
bank.interface()
```
Jegliche Ein- und Ausgaben erfolgen über die Konsole. 

## Klassen
### Bank
Die Klasse `Bank` ist die Hauptklasse des Programms. Sie enthält alle Methoden, die für die Interaktion mit dem Benutzer notwendig sind.
Sie übernimmt ebenfalls die Verwaltung der Kunden und Konten sowie die Verschlüsselung der Passwörter.

### Konto
Die Klasse `Konto` repräsentiert ein Konto. Sie dient als Parent-Class für alle weiteren Kontotypen.


### Privatkonto
Die Klasse `Privatkonto` ist eine Subklasse von `Konto`. Sie enthält die spezifische implementierung für die Methode `auszahlen`.
Diese Methode überprüft anhand der Bezugslimite, ob der Betrag auf dem Konto ausbezahlt werden kann. Ebenfalls wird eine Gebühr von 0.5% des Betrags an ein Bankkonto der Bank überwiesen.

### Jugendkonto
Die Klasse `Jugendkonto` ist ebenfalls eine Subklasse von `Konto`. Auch hier wird nur die Methode `auszahlen` definiert.
Die Methode kontrolliert, ob der Betrag ausbezahlt werden darf, da ein Jugendkonto nicht ins negative Fallen darf.