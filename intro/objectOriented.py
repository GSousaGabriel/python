class BankAccount:
    def __init__(self, iban: str, balance: float) -> None:
        self.iban = iban
        self.balance = balance
    
    def add_balance(self, amount):
        new_total = self.balance + amount
        self.balance = new_total
        return 'new balance is: ' + str(self.balance)
    
    def remove_balance(self, amount):
        new_total = self.balance - amount
        self.balance = new_total
        return 'new balance is: ' + str(self.balance)
    
    def __str__(self) -> str:
        return f"Iban: {self.iban}, balance: {self.balance} euros"
        

account1 = BankAccount('1', 42421)
account2 = BankAccount('2', 12394)

print(account1)
print('##')
print(account2)
print(account2.add_balance(31))
print(account2.remove_balance(4124))
print(account1)