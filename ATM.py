import random 
cardnumber= random.randint(100000,999999)

pinnumber= random.randint(1000,9999)


class Atm(object):

    def __init__(self,ATMcardnumber,ATMpinnumber):
        self.ATMcardnumber=ATMcardnumber,
        self.ATMpinnumber=ATMpinnumber

    def CashWithdrawl(self):
        print("you have withdrawn some cash")

    def BalanceEnquiry(self):
        print("your balance is x$")
Atm1=Atm (cardnumber,pinnumber)
print("card number is ",Atm1.ATMcardnumber)
print("pin number is ",Atm1.ATMpinnumber)
 