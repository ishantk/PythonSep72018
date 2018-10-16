# User Defined Exception
class BankingException(Exception):
    pass

class Banking:

    attempts = 0

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amt):
        self.balance = self.balance - amt
        if self.balance < 0:
            Banking.attempts = Banking.attempts + 1
            self.balance = self.balance + amt
            print(">> Withdrawl Failure. Balance is LOW Rs.", self.balance)

            if Banking.attempts == 3:
                raise BankingException()
                # raise ZeroDivisionError() # Throwing an Exception Explicitly

        else:
            print(">> Withdrawl Successful. New Balance is Rs.",self.balance)


print("==Banking Started==")

b1 = Banking(10000)

for i in range(1,100):
    b1.withdraw(3000)

print("==Banking Finished==")



