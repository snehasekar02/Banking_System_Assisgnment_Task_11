from typing import List
from bean.account import Account
from bean.current_account import CurrentAccount
from bean.customer import Customer
from service.ibank_service_provider import IBankServiceProvider
from implementation.customer_service_provider_impl import CustomerServiceProviderImpl

from bean.savings_account import SavingsAccount
from bean.zero_balance_account import ZeroBalanceAccount


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.account_list: List[Account] = []
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer: Customer, acc_type: str, balance: float) -> None:
        if acc_type in ["Savings", "Current", "Zero Balance"]:
            if acc_type == "Savings":
                account = SavingsAccount(balance, customer, 0.05)  # interest rate
            elif acc_type == "Current":
                account = CurrentAccount(balance, customer, 1000)  # overdraft limit
            else:
                account = ZeroBalanceAccount(customer)
            acc_no = account.get_account_number()
            self.account_list.append(account)
            self.account_map[acc_no] = account
            print("Account created successfully.")
        else:
            print("Invalid account type.")

    def list_accounts(self) -> List[Account]:
        return self.account_list

    def calculate_interest(self) -> None:
        for account in self.account_list:
            if isinstance(account, SavingsAccount):
                balance = account.get_balance()
                interest_rate = account.get_interest_rate()
                interest_amount = balance * (interest_rate / 100)
                new_balance = balance + interest_amount
                account.set_balance(new_balance)
                print(f"Interest calculated and added to Savings Account {account.get_account_number()}")
