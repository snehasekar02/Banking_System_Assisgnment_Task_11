from bean.account import Account


class SavingsAccount(Account):
    def __init__(self, account_balance, customer, interest_rate):
        super().__init__("Savings", account_balance, customer)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}%"
