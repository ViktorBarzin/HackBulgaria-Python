from bank_account import *

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
#True
print(rado.balance())
#500
print(ivo.balance())
#)500
print(rado.history())
#['Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500BGN']
print(ivo.history())
#['Account was created', 'Transfer from Rado for 500BGN', 'Balance check -> 500BGN']