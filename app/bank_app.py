from bean.customer import Customer
from bean.savings_account import SavingsAccount
from bean.current_account import CurrentAccount
from bean.zero_balance_account import ZeroBalanceAccount
from implementation.bank_service_provider_impl import BankServiceProviderImpl


class BankApp:
    @staticmethod
    def display_menu():
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Exit")

    @staticmethod
    def display_account_types_menu():
        print("Choose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Zero Balance Account")

    @staticmethod
    def create_customer():
        customer_id = int(input("Enter Customer ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        return Customer(customer_id, first_name, last_name, email, phone, address)

    @staticmethod
    def get_account_type_choice():
        ch = int(input("Enter your choice (1-3): "))
        if ch == 1:
            return "Savings"
        elif ch == 2:
            return "Current"
        elif ch == 3:
            return "Zero Balance"

    @staticmethod
    def get_account_number():
        return int(input("Enter Account Number: "))

    @staticmethod
    def get_amount():
        return float(input("Enter Amount: "))

    @staticmethod
    def perform_create_account(bank_service_provider):
        print("Creating Account...")
        customer = BankApp.create_customer()
        BankApp.display_account_types_menu()
        account_type_choice = BankApp.get_account_type_choice()
        balance = float(input("Enter Initial Balance: "))
        print(account_type_choice)
        bank_service_provider.create_account(customer, account_type_choice, balance)

    @staticmethod
    def perform_deposit(bank_service_provider):
        print("Depositing...")
        account_number = BankApp.get_account_number()
        amount = BankApp.get_amount()
        bank_service_provider.deposit(account_number, amount)

    @staticmethod
    def perform_withdraw(bank_service_provider):
        print("Withdrawing...")
        account_number = BankApp.get_account_number()
        amount = BankApp.get_amount()
        bank_service_provider.withdraw(account_number, amount)

    @staticmethod
    def perform_get_balance(bank_service_provider):
        print("Getting Balance...")
        account_number = BankApp.get_account_number()
        print("Balance:", bank_service_provider.get_account_balance(account_number))

    @staticmethod
    def perform_transfer(bank_service_provider):
        print("Transferring...")
        print("Sender:")
        from_account_number = BankApp.get_account_number()
        print("Receiver:")
        to_account_number = BankApp.get_account_number()
        amount = BankApp.get_amount()
        bank_service_provider.transfer(from_account_number, to_account_number, amount)

    @staticmethod
    def perform_get_account_details(bank_service_provider):
        print("Getting Account Details...")
        account_number = BankApp.get_account_number()
        print(bank_service_provider.get_account_details(account_number))

    @staticmethod
    def perform_list_accounts(bank_service_provider):
        print("Listing Accounts...")
        accounts = bank_service_provider.list_accounts()
        for account in accounts:
            print(account)

    @staticmethod
    def main():
        branch_name = input("Enter Branch Name: ")
        branch_address = input("Enter Branch Address: ")
        bank_service_provider = BankServiceProviderImpl(branch_name, branch_address)
        while True:
            BankApp.display_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                BankApp.perform_create_account(bank_service_provider)
            elif choice == 2:
                BankApp.perform_deposit(bank_service_provider)
            elif choice == 3:
                BankApp.perform_withdraw(bank_service_provider)
            elif choice == 4:
                BankApp.perform_get_balance(bank_service_provider)
            elif choice == 5:
                BankApp.perform_transfer(bank_service_provider)
            elif choice == 6:
                BankApp.perform_get_account_details(bank_service_provider)
            elif choice == 7:
                BankApp.perform_list_accounts(bank_service_provider)
            elif choice == 8:
                print("Thank You")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    BankApp.main()
