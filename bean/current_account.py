from bean.account import Account


class CurrentAccount(Account):
    def __init__(self, account_balance, customer, overdraft_limit):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.account_balance + self.overdraft_limit >= amount:
            self.account_balance -= amount
            return f"Withdrawal successful. Updated balance: {self.account_balance}"
        else:
            return "Withdrawal amount exceeds available balance and overdraft limit."

    def __str__(self):
        return super().__str__() + f"\nOverdraft Limit: {self.overdraft_limit}"
