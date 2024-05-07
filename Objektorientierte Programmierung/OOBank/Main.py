from Bank import Bank
from Interface import Interface
bank = Bank('UBS')

interface = Interface(bank)
interface.start()
