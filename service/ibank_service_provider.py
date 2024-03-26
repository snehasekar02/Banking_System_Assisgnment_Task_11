
from abc import ABC, abstractmethod
from typing import List
from bean.customer import Customer
from bean.account import Account


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer: Customer, accType: str, balance: float) -> int:
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
