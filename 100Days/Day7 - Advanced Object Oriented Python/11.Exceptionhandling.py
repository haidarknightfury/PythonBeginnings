class Amount():
    def __init__(self,amount,currency):
        self._amount = amount
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    @property
    def amount(self):
        return self._amount
    
    @currency.setter
    def currency(self, currency):
        self._currency = currency
    
    @amount.setter
    def amount(self, amount):
        self._amount= amount
    
    def add(self,amnt):
        if(self.currency != amnt.currency):
            raise CurrencyMatchException('currency doesnt match')
        else:
            self.amount += amnt.amount 

    def __repr__(self):
        return repr([self.currency, self.amount])


class CurrencyMatchException(Exception):
    def __init__(self,message):
        super().__init__(message)

if __name__ == "__main__":
    amnt = Amount(500, 'MUR')
    newAmnt = Amount(50,'MUR')
    amnt.add(newAmnt)
    print(amnt)