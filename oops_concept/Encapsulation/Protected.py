class Bank:
    def __init__(self,b_name,b_transaction):
        self.name = b_name
        self._trans = b_transaction

bank = Bank('SBI',123456789)
print(bank._trans)
print(bank.name)