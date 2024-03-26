from typing import Dict
from bean.account import Account
from bean.customer import Customer
from service.icustomer_service_provider import ICustomerServiceProvider


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.account_map: Dict[int, Account] = {}

    def get_account_balance(self, account_number: int) -> float:
        account = self.account_map.get(account_number)
        if account:
            return account.get_balance()
        else:
            print("Account not found")
            return -1

    def deposit(self, account_number: int, amount: float) -> float:
        account = self.account_map.get(account_number)
        if account:
            current_balance = account.get_balance()
            current_balance += amount
            account.set_balance(current_balance)
            print(f"Rs.{amount} deposited successfully")
            print(f"The new balance is {current_balance}")
            return current_balance
        else:
            print("Account not found")
            return -1

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.account_map.get(account_number)
        if account:
            current_balance = account.get_balance()
            if current_balance >= amount:
                current_balance -= amount
                account.set_balance(current_balance)
                print(f"Rs.{amount} withdrawn successfully")
                print(f"The new balance is {current_balance}")
                return current_balance
            else:
                print("Insufficient funds")
                return -1
        else:
            print("Account not found")
            return -1

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        from_account = self.account_map.get(from_account_number)
        to_account = self.account_map.get(to_account_number)
        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_balance = from_account.get_balance() - amount
                to_balance = to_account.get_balance() + amount
                from_account.set_balance(from_balance)
                to_account.set_balance(to_balance)
                print("Transfer successful")
            else:
                print("Insufficient funds for transfer")
        else:
            print("One of the accounts not found")

    def get_account_details(self, account_number: int) -> str:
        account = self.account_map.get(account_number)
        if account:
            return str(account)
        else:
            return "Account not found"
